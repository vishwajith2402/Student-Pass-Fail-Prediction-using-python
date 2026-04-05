# Student Pass/Fail Predictor

import pandas as pd
from sklearn.linear_model import LogisticRegression

# -----------------------------
# STEP 1: Create Dataset
# -----------------------------
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [50, 55, 60, 65, 70, 80, 90, 95],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1]  # 0 = Fail, 1 = Pass
}

df = pd.DataFrame(data)

# -----------------------------
# STEP 2: Prepare Data
# -----------------------------
X = df[["StudyHours", "Attendance"]]
y = df["Result"]

# -----------------------------
# STEP 3: Train Model
# -----------------------------
model = LogisticRegression()
model.fit(X, y)

# -----------------------------
# STEP 4: Take User Input
# -----------------------------
print("=== Student Pass/Fail Predictor ===")

study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance (%): "))

# -----------------------------
# STEP 5: Prediction
# -----------------------------
prediction = model.predict([[study_hours, attendance]])
probability = model.predict_proba([[study_hours, attendance]])

# -----------------------------
# STEP 6: Output Result
# -----------------------------
if prediction[0] == 1:
    print("\n✅ Prediction: PASS")
else:
    print("\n❌ Prediction: FAIL")

print(f"📊 Probability of Passing: {probability[0][1]*100:.2f}%")