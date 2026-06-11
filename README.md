# Medical Cost Prediction

## Project Overview

This project predicts individual medical insurance charges based on demographic and health-related information. The goal is to build an end-to-end machine learning solution that can estimate insurance costs using features such as age, BMI, number of children, smoking status, gender, and geographic region.

## Dataset

The project uses the insurance.csv dataset, which contains information about individuals and their corresponding medical insurance charges.

### Features

* Age
* Sex
* BMI (Body Mass Index)
* Number of Children
* Smoker Status
* Region

### Target Variable

* Insurance Charges

## Project Workflow

1. Data Loading and Exploration
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing and Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Comparison
7. Model Deployment using Streamlit

## Models Used

### Linear Regression

Used as a baseline model for comparison.

### Random Forest Regressor

Selected as the final model because it achieved better performance than Linear Regression.

## Results

The Random Forest Regressor achieved an R² score of approximately 0.78, meaning the model was able to explain about 78% of the variation in insurance costs.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

## Running the Application

1. Activate the virtual environment:

```bash
.\venv\Scripts\activate
```

2. Start the Streamlit application:

```bash
streamlit run app/app.py
```

3. Open the browser and navigate to:

```text
http://localhost:8501
```

## Project Structure

```text
medical-cost-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── insurance.csv
│
├── models/
│   └── medical_cost_model.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   └── model_training.ipynb
│
├── notes/
│
├── requirements.txt
└── README.md
