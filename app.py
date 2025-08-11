from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    status = None

    if request.method == 'POST':
        try:
            study = float(request.form['study'])
            sleep = float(request.form['sleep'])
            attendance = float(request.form['attendance'])

            input_data = np.array([[study, sleep, attendance]])
            pred = model.predict(input_data)[0]
            prediction = "Pass" if pred == 1 else "Fail"
            status = "success" if pred == 1 else "danger"
        except:
            prediction = "Invalid Input"
            status = "warning"

    return render_template("index.html", prediction=prediction, status=status)

if __name__ == '__main__':
    app.run(debug=True)
