import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import joblib

#Read data
data = pd.read_csv('clean_data.csv')

#Process data
texts = data['text'].astype(str)
y = data['is_offensive']
vectorizer = CountVectorizer(min_df=0.0001)
X = vectorizer.fit_transform(texts)

#Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)

#Train
print("Training...")
model = XGBClassifier()
model.fit(X_train, y_train)
print("Done.")

#Test
preds = model.predict(X_test)
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

#Save models
joblib.dump(vectorizer, 'vectorizer.joblib')
joblib.dump(model, 'model.joblib')

'''
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
#from sklearn.externals import joblib
import joblib

# Read in data
data = pd.read_csv('clean_data.csv')
#print(data)

texts = data['text'].astype(str)
y = data['is_offensive']

# Vectorize the text
vectorizer = CountVectorizer(stop_words='english', min_df=0.0001)
X = vectorizer.fit_transform(texts)

# Train the model
print("Beginning fit")
model = LinearSVC(class_weight="balanced", dual=False, tol=1e-2, max_iter=1e5)
model.fit(X, y)

#cclf = CalibratedClassifierCV(base_estimator=model)
cclf = CalibratedClassifierCV(base_estimator=model)
cclf.fit(X, y)
print("End fit")

# Save the model
joblib.dump(vectorizer, 'vectorizer.joblib')
joblib.dump(cclf, 'model.joblib')
'''