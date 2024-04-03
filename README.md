# Customer Churn Analysis and Prediction

# Overview
This project aims to analyze customer churn and develop a predictive model to identify customers who are likely to churn in the future. Customer churn refers to the phenomenon where customers discontinue their services with a company, which can lead to revenue loss and decreased customer satisfaction. By understanding the factors influencing churn and building a predictive model, businesses can take proactive measures to retain customers and improve customer loyalty.

# Objectives
- Exploratory Data Analysis (EDA): Understand the dataset's structure, identify key features, and explore relationships between variables.
- Data Preprocessing: Handle missing values, convert data types, and prepare the dataset for modeling.
- Model Development: Train and evaluate machine learning models to predict customer churn.
- Model Interpretation: Analyze the model's performance and interpret the results to understand factors contributing to churn.
- Model Deployment: Save the trained model for future use in making predictions on new data.

# Data Source
The dataset used in this project is sourced from Kaggle and consists of Telco customer data. It includes various features such as customer demographics, services subscribed, account information, and churn status.

# Project Structure
- Importing Libraries: Import necessary libraries for data analysis and visualization.
- Loading the Dataset: Load the Telco customer dataset into a Pandas DataFrame.
- Exploratory Data Analysis (EDA): Visualize the distribution of numerical and categorical features.
- Data Cleaning: Correct data types and handle missing values in the dataset.
- Data Transformation: Divide customers into tenure groups based on their length of subscription. Drop unnecessary columns like customerID. Convert the target variable 'Churn' into binary numeric format. Convert categorical variables into dummy variables for modeling.
- Data Visualization: Visualize the distribution of numerical and categorical features. Examine correlations between features using heatmaps.
- Modeling: Define a preprocessing pipeline for numerical and categorical features. Select classifiers and evaluate their performance using cross-validation. Train logistic regression model as it showed the highest average accuracy. Evaluate the trained model on the training data.
- Prediction on Sample Data: Use the trained model to make predictions on sample customer data. Display the predictions indicating whether each customer is likely to churn.
- Save the Model: Save the trained logistic regression model for future use in predicting customer churn.

# Conclusions
- Insights from EDA: Identified factors influencing churn such as tenure, monthly charges, and total charges. Discovered patterns in customer behavior based on demographics and services subscribed.
- Model Performance: Trained a logistic regression model with an accuracy of 81% on the training data. Evaluated the model's performance using classification metrics such as precision, recall, and F1-score.
- Recommendations for Business: Provided strategies for customer retention based on insights from the analysis, including personalized offers, onboarding programs, and price optimization. Suggested approaches for bringing back churned customers through win-back campaigns and reactivation offers.
