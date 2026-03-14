let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

// white background
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);

let drawing = false;

canvas.addEventListener("mousedown", () => drawing = true);
canvas.addEventListener("mouseup", () => drawing = false);
canvas.addEventListener("mouseleave", () => drawing = false);
canvas.addEventListener("mousemove", draw);

function draw(e) {
  if (!drawing) return;

  ctx.fillStyle = "black";
  ctx.beginPath();
  ctx.arc(e.offsetX, e.offsetY, 9, 0, Math.PI * 2);
  ctx.fill();
}

function clearCanvas() {
  ctx.fillStyle = "white";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  document.getElementById("result").innerText = "";
}

function predict() {
  let tempCanvas = document.createElement("canvas");
  tempCanvas.width = 28;
  tempCanvas.height = 28;
  let tctx = tempCanvas.getContext("2d");

  // fill background
  tctx.fillStyle = "white";
  tctx.fillRect(0, 0, 28, 28);

  // scale down drawing
  tctx.drawImage(canvas, 0, 0, 28, 28);

  let image = tempCanvas.toDataURL("image/png");

  fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText =
      "Prediction: " + data.prediction;
  });
}
