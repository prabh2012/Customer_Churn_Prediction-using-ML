import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(r"/Users/semitithappa/Desktop/Customer Churn Prediction/Customer-Churn.csv")
print("First 5 Rows:")
print(df.head())

# -----------------------------
# Data Cleaning
# -----------------------------

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill missing values
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# Remove Customer ID
if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)

# -----------------------------
# Encode Categorical Columns
# -----------------------------
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

for column in df.select_dtypes(include=["object"]).columns:
    df[column] = label_encoder.fit_transform(df[column].astype(str))
# Features and Target
# -----------------------------
X = df.drop("Churn", axis=1)
y = df["Churn"]
print(df.dtypes)
# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -----------------------------
# Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# -----------------------------
# Feature Importance
# -----------------------------
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop Features:")
print(importance)

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "models/churn_model.pkl")
joblib.dump(X.columns.tolist(), "models/model_columns.pkl")

print("Model and columns saved successfully!")