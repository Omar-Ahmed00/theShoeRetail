# import os
# import pandas as pd
# import mlflow
# import mlflow.sklearn
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_absolute_error, r2_score

# # Disable autologging for stability (optional)
# mlflow.autolog(disable=True)

# # Load the dataset
# data = pd.read_csv(r"D:\DEPI\NewSim_version3.11\appp\app\sales_data.csv")
# print(data.head())  # Debugging: Verify data

# # Feature Engineering: Extract month from the date column
# data['month'] = pd.to_datetime(data['date'], errors='coerce').dt.month

# data['day_of_week'] = pd.to_datetime(data['date']).dt.dayofweek
# data['is_weekend'] = data['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)
# data = pd.get_dummies(data, columns=['category'], drop_first=True)
# data['sales_lag_1'] = data['sales'].shift(1).fillna(0)
# data['rolling_avg_7d'] = data['sales'].rolling(window=7, min_periods=1).mean()


# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import train_test_split

# # Define features and target
# X = data[['discount', 'stock', 'month', 'day_of_week', 'is_weekend']]
# y = data['sales']

# # Split the data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train the Random Forest model
# model = RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Evaluate the model
# y_pred = model.predict(X_test)
# from sklearn.metrics import mean_absolute_error, r2_score
# mae = mean_absolute_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print(f"MAE: {mae}, R²: {r2}")





# # # Drop rows with missing date values (if any)
# # data = data.dropna(subset=['month'])

# # # Define features (X) and target (y)
# # X = data[['discount', 'stock', 'month']]
# # y = data['sales']


# # import seaborn as sns
# # import matplotlib.pyplot as plt

# # # Check correlation
# # corr = data[['discount', 'stock', 'month', 'sales']].corr()
# # print(corr)

# # # Visualize correlation
# # sns.heatmap(corr, annot=True, cmap='coolwarm')
# # plt.show()



# # # Split the data into training and testing sets
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # Train the model
# # model = LinearRegression()
# # model.fit(X_train, y_train)

# # # Make predictions and evaluate the model
# # y_pred = model.predict(X_test)
# # mae = mean_absolute_error(y_test, y_pred)
# # r2 = r2_score(y_test, y_pred)

# # print(f"MAE: {mae}, R²: {r2}")

# # # Start an MLflow run
# # mlflow.set_tracking_uri("http://127.0.0.1:5001")  # Ensure MLflow server is running

# # with mlflow.start_run() as run:
# #     # Log model parameters
# #     mlflow.log_param("model_type", "LinearRegression")

# #     # Log metrics
# #     mlflow.log_metric("mae", mae)
# #     mlflow.log_metric("r2", r2)

# #     # Log the model
# #     mlflow.sklearn.log_model(model, "sales_forecasting_model")

# #     print(f"Model logged in run: {run.info.run_id}")



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score

# Load the dataset
sales_data = pd.read_csv(r"D:\DEPI\NewSim_version3.11\appp\app\sales.csv")

# Drop irrelevant or empty columns
sales_data = sales_data.drop(columns=['Unnamed: 3', 'Unnamed: 12'], errors='ignore')

# Preprocessing
# Encoding categorical variables: Customer Gender, Location, Delivery Type, Category, Product Name, Status
sales_data = pd.get_dummies(sales_data, columns=['Customer Gender', 'Location', 'Delivery Type', 'category', 'product_name', 'Status'], drop_first=True)

# Impute missing values
imputer = SimpleImputer(strategy='mean')
sales_data_imputed = pd.DataFrame(imputer.fit_transform(sales_data), columns=sales_data.columns)

# Define features (X) and target (y)
X = sales_data_imputed.drop(columns=['Sale Price'])  # Exclude Sale Price (our target)
y = sales_data_imputed['Sale Price']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize models
linear_reg = LinearRegression()
decision_tree = DecisionTreeRegressor(random_state=42, max_depth=10, min_samples_split=10)
random_forest = RandomForestRegressor(random_state=42, n_estimators=100, max_depth=10)
gradient_boost = GradientBoostingRegressor(random_state=42, n_estimators=100, learning_rate=0.1)

# Train models
linear_reg.fit(X_train, y_train)
decision_tree.fit(X_train, y_train)
random_forest.fit(X_train, y_train)
gradient_boost.fit(X_train, y_train)

# Make predictions
y_pred_linear = linear_reg.predict(X_test)
y_pred_tree = decision_tree.predict(X_test)
y_pred_forest = random_forest.predict(X_test)
y_pred_boost = gradient_boost.predict(X_test)

# Calculate R-squared for each model
r2_linear = r2_score(y_test, y_pred_linear)
r2_tree = r2_score(y_test, y_pred_tree)
r2_forest = r2_score(y_test, y_pred_forest)
r2_boost = r2_score(y_test, y_pred_boost)

# Display the R-squared values
print('R-squared scores:')
print(f'Linear Regression: {r2_linear}')
print(f'Decision Tree: {r2_tree}')
print(f'Random Forest: {r2_forest}')
print(f'Gradient Boosting: {r2_boost}')
