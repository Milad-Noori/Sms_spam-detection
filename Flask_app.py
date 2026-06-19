from flask import Flask, request, jsonify
import pickle

app = Flask("sms spam ")

with open('spam_detector.pkl', 'rb') as model_file:
pipeline = pickle.load(model_file)

