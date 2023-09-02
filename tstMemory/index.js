//
// Odroid fan control
//
// index.js
//

let websocket = 0;

window.addEventListener("DOMContentLoaded", () => {
    const messages = document.createElement("ul");
    document.body.appendChild(messages);

    port = parseInt(document.location.port) + 1;
    const uri = "ws://" + document.location.hostname + ':' + port;
    console.log(uri);
    websocket = new WebSocket(uri);

    websocket.onmessage = ({ data }) => {
    
        // document.getElementById("temperature").value = "55";
        document.getElementById("currentTime").innerHTML = data;
    };
});

function sendTemperature(temparature) {
    const event = {
      type: "temperature",
      value: parseInt(temparature, 10),
    };
    websocket.send(JSON.stringify(event));
}

window.addEventListener("input", ({ target }) => {
    sendTemperature(target.value);
});

function sleep(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}

for (let i = 1; i < 8; i++) {
    setTimeout(() => sendTemperature(i * 100), i * 1000);
}
 
// Refresh the page
setTimeout(() => location.reload(), 10000);

