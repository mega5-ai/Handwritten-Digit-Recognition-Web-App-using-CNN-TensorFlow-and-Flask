# Handwritten-Digit-Recognition-Web-App-using-CNN-TensorFlow-and-Flask
This project is a web-based handwritten digit recognition system that allows users to draw digits on a canvas and receive real-time predictions using a deep learning model.

The system uses a Convolutional Neural Network (CNN) trained on the MNIST Dataset to recognize digits from 0–9. The web interface is built using HTML, CSS, and JavaScript, where users can draw a digit and send it to the backend for prediction.

The backend is developed using Flask. It processes the image by converting it to grayscale, resizing it to 28×28 pixels, and normalizing it before passing it to the TensorFlow/Keras model.

The trained model predicts the digit and returns the result instantly. This project demonstrates how deep learning models can be integrated with web applications to create interactive AI-based systems.
