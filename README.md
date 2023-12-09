# websockets

I searched the internet for a long time for a websocket server written in Python. A server which would push messages to the client at a regular basis. Or if something on the server would change. And in the meantime could handle requests from the client.

Think I found the solution. To test this example save the 3 files into a directory on the server. Then start in that directory a http server, for instance with a command like this:

python -m http.server

In a second terminal in the above mentioned directory start a comand like this:

python server.py

And in a browser on the server or on another system:

http://odroid:8000 or http:/localhost:8000

Webpage should display this:

- first line the time in seconds, this is the push from the server
- second line an input number field, this is the push from the client. Changes can be seen in the log of the second python command.

Please comment as I'm not sure if I got the correct solution. However it tested ok.

I plan to use this to see the temperature of my Odroid system and regulate the fan. Having the user interface on another system.

The directory tstMemory contains a set of files which I used for testing memory usage. A refresh of the webpage is done every 10 seconds and in between 7 sends from client to server is done. Webpage can be openend in different webbrowser on different systems simultaneously. No memory leak was detected during this test.

This is not a secure solution. So use it whithin your own network only, not to service requests from the outside hostile world. And ofcourse use at your OWN RISK.

Saterday, 9 december 2023 16:34
