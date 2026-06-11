## Data Preparation

- X contains the features (inputs).
- y contains the target variable (output).
- The target must be removed from X to avoid data leakage.
- axis=1 means operate on columns.

- X is a DataFrame because it contains multiple feature columns.
- y is a Series because it contains a single target column.
- DataFrames are two-dimensional (rows and columns).
- Series are one-dimensional (single column).

## Encoding

- Machine learning models require numerical inputs.
- Categorical features must be converted into numbers.
- One-hot encoding creates binary (0/1) columns.
- drop_first=True removes redundant columns.

## Train/Test Split

- Data is split into training and testing sets.
- Training data is used to learn patterns.
- Testing data evaluates model performance on unseen data.
- This prevents overfitting.
- random_state ensures reproducibility.

## Linear Regression Model

- Linear Regression learns relationships between features and target.
- The model is trained using training data only.
- Predictions are made on unseen test data.
- Real vs predicted values help evaluate performance.

## Model Evaluation

- MAE measures average prediction error.
- RMSE penalizes large errors more heavily.
- R² measures how well the model explains variance in data.
- Actual vs predicted plot helps visually assess model quality.

## Model Evaluation Insights

- MAE shows average prediction error in dollars.
- RMSE highlights larger prediction mistakes.
- R² measures how well the model explains variance.
- Linear Regression works as a baseline model.
- Medical cost data has strong non-linear patterns (especially smoker effect).

## Model Comparison

- Multiple models should be trained and compared.
- Linear Regression is a baseline model.
- Random Forest captures non-linear patterns better.
- Final model is selected based on evaluation metrics, not complexity.