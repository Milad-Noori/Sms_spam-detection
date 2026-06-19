from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('spam_detector.pkl', 'rb') as model_file:
    pipeline = pickle.load(model_file)

@app.route('/')
def home():
    return {
"message": "Spam Detection API is Running"
}

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    text_message = data.get("message", "")

    prediction = pipeline.predict([text_message])[0]

    probability = pipeline.predict_proba([text_message])[0]

    return jsonify({
    "message": text_message,
    "prediction": prediction,
    "ham_probability": float(probability[0]),
    "spam_probability": float(probability[1])
})

    if name == "main":
        app.run(debug=True)

