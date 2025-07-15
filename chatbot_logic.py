import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load intents
with open("intents.json") as f:
    data = json.load(f)

# Prepare training data
tags = []
patterns = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

# Train a simple classifier
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)
clf = MultinomialNB()
clf.fit(X, tags)

# Response function
def get_response(user_input):
    X_test = vectorizer.transform([user_input])
    predicted_tag = clf.predict(X_test)[0]
    for intent in data["intents"]:
        if intent["tag"] == predicted_tag:
            return random.choice(intent["responses"])
    return "Sorry, I didn't understand that."
