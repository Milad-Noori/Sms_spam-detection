from flask import Flask, request, jsonify
import pickle
from nltk.corpus import stopwords

app = Flask(__name__)

def text_process(mess: str):
    import string

    mess = mess.lower()

    nopuct = [char for char in mess if char not in string.punctuation]
    nopuct = ''.join(nopuct)

    return [
        word
        for word in nopuct.split()
        if word.lower() not in stopwords.words('english')
    ]

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


if __name__ == "__main__":
    app.run(debug=True)