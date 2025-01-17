# **Investment Prediction Application**

This project leverages machine learning to predict stock price movements using historical data. The solution includes data preprocessing, a trained machine learning model, and a web-based user interface for testing and interaction. 

## **Features**
- **Data Analysis**: Explored and processed stock market data to identify patterns and correlations.
- **Machine Learning Model**: Built using a linear regression algorithm to predict the adjusted closing price.
- **Cloud Integration**: Hosted on Google Cloud (or alternative free platforms).
- **Cassandra Database**: Used to store and manage stock market data.
- **Logging**: Implemented for tracking actions and debugging.
- **User Interface**: A web-based UI created using Flask to allow users to test the model.

---

## **Technologies Used**

### **Programming Languages and Frameworks**
- **Python**: Core programming language for data processing and model development.
- **Flask**: Web framework for creating APIs and the user interface.

### **Libraries**
- **Data Analysis**:
  - `numpy`: Numerical computations.
  - `pandas`: Data manipulation and preprocessing.
  - `matplotlib`: Data visualization.
- **Machine Learning**:
  - `scikit-learn`: Linear regression model and data splitting.
- **Database Integration**:
  - `astrapy`: Cassandra database client for connecting to Astra DB.
- **Utilities**:
  - `pickle`: Model serialization for saving and loading the trained model.
  - `logging`: For tracking and debugging application actions.

### **Cloud Platform**
- **Google Cloud Platform (GCP)**: Deployment and hosting of the solution.

### **Database**
- **Cassandra (Astra DB)**: NoSQL database for handling large datasets efficiently.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/Vedkhajone/Investement_Prediction.git

cd investment-prediction
```
## **2.Install required libraries:**


Install the necessary Python libraries including scikit-learn for machine learning models:

```bash

pip install -r requirements.txt
```

If you don't have a requirements.txt file, you can manually install the necessary packages:

```bash
pip install scikit-learn pandas numpy flask
```
### **Ensure that the model file exists:**

Make sure that the model.pkl file is present in the same directory as app.py. If it's missing, ensure that you train and save the model as model.pkl using your .ipynb notebook.

### **Run the app:**

Run the ```app.py``` file:

```bash

python app.py
```
This should start the Flask app and you can access it through the browser or postman.

Access the app in the browser:

Open the following URL in your browser:

<herf>http://127.0.0.1:5000/

### **Troubleshooting:**

If you encounter any issues such as missing modules or files, ensure all necessary dependencies are installed and that the correct model file (model.pkl) is present.