import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

# Read the CSV file
file_path = 'path/to/your/data.csv'  # Replace with the actual file path
df = pd.read_csv(file_path)

# Define independent (X) and dependent (y) variables
X = df[['Property Area (ftÂ²)', 'Temperature', 'Humidity (%)', 'No. of Occupants']]  # Example columns, modify as needed
y = df['Electricity Use - (kWh)']  # Dependent variable

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Validate the model on the test set
y_pred = model.predict(X_test)

# Metrics for model evaluation
print('R-squared:', r2_score(y_test, y_pred))
print('RMSE:', np.sqrt(mean_squared_error(y_test, y_pred)))

# Statsmodels summary for detailed statistics
X_train_sm = sm.add_constant(X_train)
stats_model = sm.OLS(y_train, X_train_sm).fit()
print(stats_model.summary())