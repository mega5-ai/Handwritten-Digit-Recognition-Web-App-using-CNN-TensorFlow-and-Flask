import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("handwritten_digit_model2.h5")

# fake test
img = np.zeros((1,28,28,1))
print(model.predict(img))
