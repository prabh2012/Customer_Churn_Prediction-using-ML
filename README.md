# 📊 Customer Churn Prediction using Machine Learning

Predict whether a telecom customer is likely to churn using Machine Learning. This project is built with **Python**, **Flask**, **Scikit-learn**, and **Bootstrap**, providing a modern web interface where users can enter customer details and receive real-time churn predictions with a confidence score.

---

## 🚀 Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. Retaining existing customers is often more cost-effective than acquiring new ones.

This application predicts customer churn based on demographic information, account details, subscribed services, contract type, and billing information.

---

## ✨ Features

- 🤖 Machine Learning-based churn prediction
- 🌐 Interactive Flask web application
- 🎨 Modern and responsive user interface
- 📈 Displays prediction confidence
- 🧹 Data preprocessing and feature engineering
- 💾 Trained model saved using Joblib
- ⚡ Real-time customer prediction

---

## 🛠 Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest Classifier

### Data Processing
- Pandas
- NumPy

### Web Framework
- Flask

### Frontend
- HTML5
- CSS3
- Bootstrap 5

### Model Serialization
- Joblib

---

## 📂 Project Structure

```text
Customer-Churn-Prediction/
│
├── models/
│   ├── churn_model.pkl
│   └── model_columns.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── Customer-Churn.csv
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The project uses the **Telco Customer Churn Dataset**.

### Dataset Features

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges
- Churn (Target Variable)

---

## ⚙️ Machine Learning Workflow

- Data Collection
- Data Cleaning
- Missing Value Handling
- Feature Encoding
- Train-Test Split
- Model Training
- Model Evaluation
- Model Saving
- Flask Deployment

---

## 📈 Model Used

**Random Forest Classifier**

The model is trained using Scikit-learn and evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 💻 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Customer-Churn-Prediction.git
```

### Navigate to the Project Folder

```bash
cd Customer-Churn-Prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Train the model:

```bash
python train_model.py
```

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📷 Application Preview

### Home Page

- Customer Information Form
- Interactive Input Fields
- Predict Churn Button

### Result Page

- Prediction Result
- Confidence Score
- Professional Dashboard UI

> *(Add screenshots here after uploading them to GitHub.)*

---

## 📌 Future Enhancements

- Explainable AI (SHAP)
- Interactive Analytics Dashboard
- Prediction History
- User Authentication
- Cloud Deployment
- REST API
- Model Comparison (XGBoost, Logistic Regression)

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Machine Learning Model Development
- Data Preprocessing
- Feature Engineering
- Flask Web Development
- Model Deployment
- Responsive Frontend Design
- Git & GitHub Version Control

---

## 👩‍💻 Author

**Prabhleen Kaur**

B.Tech Computer Science Engineering (AI & ML)

---

## ⭐ If you like this project

If you found this project useful, consider giving it a ⭐ on GitHub!
