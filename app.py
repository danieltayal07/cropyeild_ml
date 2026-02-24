from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# LOAD FILES
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return "Crop Yield ML API Running 🚀"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json["features"]

    # convert input to numpy
    data = np.array(data).reshape(1, -1)

    # apply same scaling
    data = scaler.transform(data)

    # prediction
    prediction = model.predict(data)

    return jsonify({"prediction": float(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)