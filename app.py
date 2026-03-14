from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import base64, io

app = Flask(__name__)
model = tf.keras.models.load_model("handwritten_digit_model3.h5")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["image"]
    image = base64.b64decode(data.split(",")[1])

    img = Image.open(io.BytesIO(image)).convert("L")
    img = np.array(img)

    # Convert background to black, digit to white
    img = np.where(img > 200, 0, 255).astype(np.uint8)

    # Get bounding box of digit
    coords = np.column_stack(np.where(img > 0))
    if coords.size == 0:
        return jsonify({"prediction": 0})

    y_min, x_min = coords.min(0)
    y_max, x_max = coords.max(0)
    digit = img[y_min:y_max+1, x_min:x_max+1]

    # Resize digit to 20x20
    digit = Image.fromarray(digit).resize((20, 20))

    # Center digit in 28x28 canvas
    canvas_28 = Image.new("L", (28, 28), 0)
    canvas_28.paste(digit, (4, 4))

    # Normalize
    digit = np.array(canvas_28) / 255.0
    digit = digit.reshape(1, 28, 28, 1)

    prediction = model.predict(digit)
    result = int(np.argmax(prediction))

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
