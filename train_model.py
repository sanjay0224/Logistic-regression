import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv("student_data.csv")

X = df[['StudyHours', 'SleepHours', 'Attendance']]
y = df['Pass']

model = LogisticRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("working succesfully")