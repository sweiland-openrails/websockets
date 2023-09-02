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
        document.getElementById("currentTime").innerHTML = data;
    };
});

window.addEventListener("input", ({ target }) => {
    const event = {
      type: "temperature",
      value: parseInt(target.value, 10),
    };
    websocket.send(JSON.stringify(event));
});

