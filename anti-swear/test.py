import joblib
loaded_model = joblib.load("model.joblib")
vectoriser = joblib.load("vectorizer.joblib")
while True:
    text = input("string: ")
    text = [text]
    vText = vectoriser.transform(text)
    prob = loaded_model.predict(vText)
    print(prob)