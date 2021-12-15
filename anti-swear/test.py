import joblib
import time
import os
loaded_model = joblib.load(os.path.dirname(os.path.realpath(__file__)) + "\\model.joblib")
vectoriser = joblib.load(os.path.dirname(os.path.realpath(__file__)) + "\\vectorizer.joblib")

while True:
    text = input("string: ")
    pretime = time.time()
    text = [text]
    vText = vectoriser.transform(text)
    prob = loaded_model.predict(vText)
    print(prob)
    print(f"Calculated in {(time.time() - pretime)*100} ms")