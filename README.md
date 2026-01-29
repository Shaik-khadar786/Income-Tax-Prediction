# Income Tax Prediction using Machine Learning

## Project Overview
This project predicts the **income tax paid by an individual** based on structured financial data such as:
- Age
- Annual Income
- Investments
- Deductions

A **Linear Regression** model is trained to learn patterns between financial attributes and tax liability.

---

## Problem Statement
Manual estimation of income tax can be time-consuming and error-prone.  
This project aims to **automate tax prediction** using machine learning for faster and data-driven insights.

---

## Machine Learning Approach
- Type: Supervised Learning
- Algorithm: Linear Regression
- Target Variable: Tax_Paid

---

## Project Workflow
1. Data generation & storage
2. Data preprocessing
3. Train-test split
4. Model training
5. Model evaluation (R², MAE)
6. Tax prediction on new inputs
7. Model persistence using Joblib
8. Version control using Git & GitHub

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Git & GitHub

---

## Model Performance
- R² Score: ~0.92  
- Mean Absolute Error: Low prediction error

---

## How to Run the Project
```bash
pip install -r requirements.txt
python income_tax_analysis.py