🩺 Diabetes Data Analysis & Prediction
📌 Project Overview

This project focuses on analyzing a diabetes dataset to identify key health factors and understand patterns related to diabetes. It includes data preprocessing, visualization, statistical testing, and a basic machine learning model.

🎯 Objectives
Analyze medical dataset related to diabetes
Perform Exploratory Data Analysis (EDA)
Identify important features affecting diabetes
Apply statistical testing (T-test)
Build a regression model to study relationships
Identify high-risk and low-risk patients
📂 Dataset Information
Rows: 768 patients
Columns: 9 features
Target Variable: outcome
0 → Non-diabetic
1 → Diabetic
Features:
Pregnancies
Glucose
Blood Pressure
Skin Thickness
Insulin
BMI
Diabetes Pedigree Function
Age
🧹 Data Preprocessing
Cleaned column names
Checked missing values
Identified unrealistic values (e.g., glucose = 0)
Outlier awareness (IQR concept)
📊 Exploratory Data Analysis (EDA)
Visualizations:
Glucose Distribution (Histogram + KDE)
BMI vs Outcome (Box Plot)
Age vs Glucose (Scatter Plot)
Insulin vs Outcome (Box Plot)
Correlation Heatmap
Pairplot
Key Insights:
Glucose has the strongest correlation with diabetes
BMI and Age also influence diabetes
Dataset shows slight class imbalance
🧪 Hypothesis Testing
Performed T-test to compare BMI between:
Low glucose group
High glucose group

👉 Helps check if differences are statistically significant

🤖 Model Used
Linear Regression
Input: Glucose
Output: BMI

👉 Purpose:

To analyze the relationship between glucose and BMI

⚠️ Note:
This is not a classification model. For predicting diabetes outcome, Logistic Regression is more appropriate.

📈 Model Evaluation
Used R² Score to measure model performance
🚨 Scenario Analysis

Identified:

High-risk patients:
Glucose > 140
BMI > 30
Low-risk patients:
Glucose < 100
BMI < 25
🛠️ Technologies Used
Python 🐍
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
SciPy



📌 Conclusion

Glucose is the most important factor in diabetes prediction
BMI and Age also contribute
Data visualization and statistical analysis provide meaningful insights
Linear Regression helps understand relationships, but classification models are better for prediction

🔮 Future Scope

Implement Logistic Regression for prediction
Improve accuracy using advanced models
Handle outliers and feature scaling
Deploy as a web application


👩‍💻 Author

Kimaya Shree Saminathan
