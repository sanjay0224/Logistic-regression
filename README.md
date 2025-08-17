Logistic Regression – Student Exam Pass Prediction
📌 Project Overview

This project is a Machine Learning web application built with Flask (backend) and HTML/CSS (frontend).
It uses Logistic Regression to predict whether a student will pass or fail an exam based on study hours and sleep hours.

Users can enter details in the web form, and the model will output either "Pass" or "Fail".

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/logistic_exam_prediction.git
cd logistic_exam_prediction

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train the Model
python train_model.py

4️⃣ Run the Application
python app.py


The app will run on http://127.0.0.1:5000/.

🧠 Model Details

Algorithm: Logistic Regression

Library: scikit-learn

Dataset Features:

Study Hours — Hours spent studying per day

Sleep Hours — Average sleep duration per day

Exam Result — Target variable (Pass/Fail)

📊 Prediction Flow

User enters study hours and sleep hours.

Flask sends the input to the trained Logistic Regression model.

Model predicts whether the student will pass or fail.

Result is displayed on the output page.

📸 Screenshots
<img width="1600" height="794" alt="image" src="https://github.com/user-attachments/assets/06a9c529-4ffe-4dd7-a325-8898ab6ae0ca" />


📌 Requirements
Flask
scikit-learn
pandas
numpy


Install with:

pip install Flask scikit-learn pandas numpy

🚀 Future Improvements

Collect real-world data (attendance, assignments, etc.).

Improve accuracy using Random Forest or Neural Networks.

Deploy the model on Heroku/Render for public use.
