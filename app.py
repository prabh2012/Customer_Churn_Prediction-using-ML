from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and training columns
model = joblib.load("models/churn_model.pkl")
model_columns = joblib.load("models/model_columns.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get form data
    gender = request.form["gender"]
    senior = int(request.form["SeniorCitizen"])
    partner = request.form["Partner"]
    dependents = request.form["Dependents"]
    tenure = int(request.form["tenure"])
    phone = request.form["PhoneService"]
    multiple = request.form["MultipleLines"]
    internet = request.form["InternetService"]
    online_security = request.form["OnlineSecurity"]
    online_backup = request.form["OnlineBackup"]
    device = request.form["DeviceProtection"]
    tech = request.form["TechSupport"]
    tv = request.form["StreamingTV"]
    movies = request.form["StreamingMovies"]
    contract = request.form["Contract"]
    paperless = request.form["PaperlessBilling"]
    payment = request.form["PaymentMethod"]
    monthly = float(request.form["MonthlyCharges"])
    total = float(request.form["TotalCharges"])

    # Create dataframe
    data = {
        "SeniorCitizen": senior,
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "gender": gender,
        "Partner": partner,
        "Dependents": dependents,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device,
        "TechSupport": tech,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment
    }

    df = pd.DataFrame([data])

    # Convert to dummy variables
    df = pd.get_dummies(df)

    # Add missing columns
    for col in model_columns:
        if col not in df.columns:
            df[col] = 0

    # Keep the same column order
    df = df[model_columns]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1] * 100

    if prediction == 1:
        result = "Customer is likely to Churn"
    else:
        result = "Customer is NOT likely to Churn"

    return render_template(
        "result .html",
        prediction=result,
        probability=round(probability, 2)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)