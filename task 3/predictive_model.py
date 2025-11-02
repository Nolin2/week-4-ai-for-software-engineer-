# Task 3: Predictive Analytics for Resource Allocation
# Author: Nolin Masai
# Dataset: Breast Cancer (from sklearn)
# Goal: Predict issue priority using ML

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Load dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

print("✅ Dataset Loaded Successfully")
print("Total Records:", X.shape[0])
print("Total Features:", X.shape[1])

# 2️⃣ Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3️⃣ Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4️⃣ Predict
y_pred = model.predict(X_test)

# 5️⃣ Evaluate
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n📊 Model Performance:")
print(f"Accuracy: {accuracy:.2f}")
print(f"F1 Score: {f1:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 6️⃣ Visualize metrics
metrics = {'Accuracy': accuracy, 'F1 Score': f1}
plt.bar(metrics.keys(), metrics.values(), color=['#007BFF', '#00C851'])
plt.title("Model Performance Metrics")
plt.ylim(0, 1)
plt.ylabel("Score")
plt.savefig("task3_metrics_chart.png")
plt.show()

print("✅ Chart saved as task3_metrics_chart.png")

