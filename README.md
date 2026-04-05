# Student-Pass-Fail-Prediction-using-python
This project is a simple Machine Learning application that predicts whether a student will Pass or Fail based on study hours and attendance. It uses Logistic Regression and takes user input from the console to generate predictions.
A simple Streamlit-based machine learning app that predicts whether a student will pass or fail based on study hours and attendance. It uses Logistic Regression and provides real-time predictions with confidence scores through an interactive and user-friendly interface.

**Features**
Predict Pass/Fail using ML
Displays probability (confidence score)
Simple console-based input/output
Lightweight and beginner-friendly

**Technologies Used**
Python
Pandas
Scikit-learn

**Project Structure**
project/
│── main.py       # Main Python script
│── README.md     # Project documentation

**How It Works**
A dataset is created with study hours and attendance.
Logistic Regression model is trained.
User enters study hours and attendance via console.
The model predicts Pass/Fail along with probability.

**Installation**
Install required libraries:
pip install pandas scikit-learn

**Run the Project**
python main.py

**Example**
Input:
Enter Study Hours: 5
Enter Attendance (%): 80
Output:
PASS
Probability of Passing: 85%

**Future Improvements**
Add graphical user interface (Streamlit/Tkinter)
Use real-world dataset
Add more features (sleep, assignments, marks)
