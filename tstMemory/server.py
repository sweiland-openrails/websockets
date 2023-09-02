#!/usr/bin/env python

#
# Odroid fan control
#
# server.js
#

import asyncio
import websockets
import datetime
import socket

def nowTime():
    return datetime.datetime.now().strftime("%H:%M:%S")

async def consumer(message): 
    print("consumer: ", message)

async def producer():
    now = nowTime()
    print("producer: ", now)
    return(now)

async def consumer_handler(websocket):
    try:
        while True:
            async for message in websocket:
                await consumer(message)
    except websockets.exceptions.ConnectionClosedOK:
        pass        
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("End consumer_handler")

async def producer_handler(websocket):
    try:
        while True:
            message = await producer()
            await websocket.send(message)
            await asyncio.sleep(1.0)
    except websockets.exceptions.ConnectionClosedOK:
        pass        
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("End producer_handler")

async def handler(websocket, path):
    connectionId = websocket.remote_address[0]
    try:
        connectionId = format(socket.gethostbyaddr(connectionId))
    except socket.herror:
        pass
    connectionId = nowTime() + " " + connectionId
    
    print("Start connection: " + connectionId)
    producer_task = asyncio.ensure_future(producer_handler(websocket))
    consumer_task = asyncio.ensure_future(consumer_handler(websocket))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()
    print("End connection: " + connectionId)

if __name__ == '__main__':
    try:
        start_server = websockets.serve(handler, "", 8001)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("Keyboard interrupt, stopped.")

