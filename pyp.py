import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# =========================
# 1. LOAD DATASET

df = pd.read_csv(r"D:\4sem\pyproject\diabetes.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

print("Columns:", df.columns.tolist())

# =========================
# 2. EDA

print("Shape:", df.shape)

print("Info:")
df.info()

print("Summary:")
print(df.describe())

print("Missing Values:")
print(df.isnull().sum())

# =========================
# 3. BASIC ANALYSIS

print("###########################")

print("Glucose Mean:", df['glucose'].mean())
print("BMI Mean:", df['bmi'].mean())
print("Age Mean:", df['age'].mean())

print("###########################")

print("Outcome Count:\n", df['outcome'].value_counts())

# =========================
# 4. VISUALIZATION

sns.set_style("whitegrid")

# 1. Glucose Distribution
plt.figure()
sns.histplot(df['glucose'], kde=True, color='blue')
plt.title("Glucose Distribution")

# 2. BMI vs Outcome (FIXED)
plt.figure()
sns.boxplot(x='outcome', y='bmi', hue='outcome', data=df, palette='Set2', legend=False)
plt.title("BMI vs Diabetes Outcome")

# 3. Age vs Glucose
plt.figure()
sns.scatterplot(x='age', y='glucose', data=df, color='green')
plt.title("Age vs Glucose")

# 4. Insulin vs Outcome (FIXED - removed duplicate)
plt.figure()
sns.boxplot(x='outcome', y='insulin', hue='outcome', data=df, palette='coolwarm', legend=False)
plt.title("Insulin vs Outcome")

# 5. Correlation Heatmap
plt.figure()
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='viridis')
plt.title("Correlation Heatmap")

# 6. Pairplot
sns.pairplot(df[['glucose','bmi','age','insulin','outcome']], hue='outcome')

plt.show()


# 5. HYPOTHESIS TEST

low_glucose = df[df['glucose'] < 120]['bmi']
high_glucose = df[df['glucose'] >= 120]['bmi']

t_stat, p_val = stats.ttest_ind(low_glucose, high_glucose)

print("###########################")
print("T-Test Result")
print("t:", t_stat)
print("p:", p_val)

# =========================
# 6. REGRESSION

X = df[['glucose']]
y = df['bmi']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("###########################")
print("Regression Equation:")
print(f"BMI = {model.coef_[0]:.2f} * Glucose + {model.intercept_:.2f}")
print("R2 Score:", r2_score(y, y_pred))

# =========================
# 7. SCENARIO ANALYSIS

high_risk = df[
    (df['glucose'] > 140) &
    (df['bmi'] > 30)
]

low_risk = df[
    (df['glucose'] < 100) &
    (df['bmi'] < 25)
]

print("###########################")
print("High Risk Patients:", len(high_risk))
print("Low Risk Patients:", len(low_risk))
