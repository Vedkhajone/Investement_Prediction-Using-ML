from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))  # Load your trained model


@app.route('/')
def index():
    # Render the home page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Extract input values from the form
    val1 = request.form['Open']
    val2 = request.form['High']
    val3 = request.form['Low']
    val4 = request.form['Volume']

    # Convert inputs into a 2D array
    arr = np.array([[val1, val2, val3, val4]], dtype=np.float64)

    # Convert the array into a DataFrame with proper feature names
    input_df = pd.DataFrame(arr, columns=['Open', 'High', 'Low', 'Volume'])

    # Predict using the loaded model
    pred = model.predict(input_df)

    # Render the result
    return render_template('index.html', data=float(pred[0]))


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
