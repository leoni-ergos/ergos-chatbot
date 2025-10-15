import pickle
from googletrans import Translator

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "intent_model.pkl")

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)


def get_intent_and_entities(text):
    intentPredicted = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities)
    print(confidence)
    if confidence < 0.8:
        intentPredicted = "out_of_scope"
    return intentPredicted


def process(text):
    translated = Translator().translate(text, src='auto', dest='en')
    print("Translated: ", translated.text, translated.src)
    intent = get_intent_and_entities(translated.text)
    return intent, translated.src
