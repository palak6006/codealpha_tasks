# TASK 1: Iris Flower Classification using CSV file

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("Iris.csv")

X = data[['SepalLengthCm', 'SepalWidthCm', 
          'PetalLengthCm', 'PetalWidthCm']]
y = data['Species']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Iris Classification Accuracy:", accuracy)
