from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
from logging_config import logger  # Import the logger

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))  # Load your trained model

@app.route('/')
def index():
    logger.info("Home page rendered")  # Log when home page is accessed
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    logger.info("Prediction route accessed")  # Log when the prediction route is accessed

    try:
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

        logger.info(f"Prediction: {pred[0]}")  # Log the prediction result
        return render_template('index.html', data=float(pred[0]))
    except Exception as e:
        logger.error(f"Error during prediction: {e}")  # Log any errors during prediction
        return "An error occurred while making the prediction."

if __name__ == '__main__':
    logger.info("App started")  # Log when the app starts
    app.run(debug=True, host='0.0.0.0')
