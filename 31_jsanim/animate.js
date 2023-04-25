var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "lightblue";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 0;
var growing = true;

var drawCircle = (radius) => {
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
}

var drawDot = () => {
    clear();

    if (growing) {
        radius += 1
    } else {
        radius -= 1
    }
    

    if (radius >= 250) {
        growing = false
    } else if (radius <= 0 ) {
        growing = true
    }

    drawCircle(radius)
    
    requestID = window.requestAnimationFrame(drawDot);
}

var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);
    requestID = window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", () => {
    window.cancelAnimationFrame(requestID);
    drawDot();
    requestID = window.requestAnimationFrame(growDot);

});
stopButton.addEventListener("click", stopIt);