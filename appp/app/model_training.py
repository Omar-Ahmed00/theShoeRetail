
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

sales_data = pd.read_csv(r'D:\DEPI\Graduation-Project\DataBase\datasets\Done_data\sales.csv')
summary_stats = sales_data.describe()

missing_values = sales_data.isnull().sum()

# Convert 'Delivery Date' to datetime format and extract useful components
sales_data['Delivery Date'] = pd.to_datetime(sales_data['Delivery Date'], errors='coerce')
sales_data['Delivery Month'] = sales_data['Delivery Date'].dt.month
sales_data['Delivery Day'] = sales_data['Delivery Date'].dt.day

# Drop non-numeric columns
numeric_data = sales_data.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix
correlation_matrix = numeric_data.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)




# Drop irrelevant or empty columns
sales_data = sales_data.drop(columns=['Unnamed: 3', 'Unnamed: 12'], errors='ignore')

# Preprocessing
# Encoding categorical variables: Customer Gender, Location, Delivery Type, Category, Product Name, Status
sales_data = pd.get_dummies(sales_data, columns=['Customer Gender', 'Location', 'Delivery Type', 'category', 'product_name', 'Status'], drop_first=True)


from sklearn.impute import SimpleImputer

# Separate numeric and non-numeric columns
numeric_data = sales_data.select_dtypes(include=['float64', 'int64'])
non_numeric_data = sales_data.select_dtypes(exclude=['float64', 'int64'])

# Impute missing values only for numeric data
imputer = SimpleImputer(strategy='mean')
numeric_data_imputed = pd.DataFrame(imputer.fit_transform(numeric_data), columns=numeric_data.columns)

# Recombine the imputed numeric data with the non-numeric data
sales_data_imputed = pd.concat([numeric_data_imputed, non_numeric_data], axis=1)

# Display the first few rows of the imputed data to verify
print(sales_data_imputed.head())



# Define features (X) and target (y)
X = sales_data_imputed.drop(columns=['Sale Price'])  # Exclude Sale Price (our target)
y = sales_data_imputed['Sale Price']



# Convert 'Delivery Date' to datetime format and extract useful features
sales_data['Delivery Date'] = pd.to_datetime(sales_data['Delivery Date'], errors='coerce')
sales_data['Delivery Month'] = sales_data['Delivery Date'].dt.month
sales_data['Delivery Day'] = sales_data['Delivery Date'].dt.day

# Drop non-numeric columns that can't be scaled
non_numeric_columns = ['ID', 'OrderID', 'CustomerID', 'Location', 'Zone', 
                       'category', 'product_name', 'Status', 'Reason', 'Delivery Date']
numeric_data = sales_data.drop(columns=non_numeric_columns, errors='ignore')

# Check if any columns are still non-numeric
print("Data types after dropping non-numeric columns:")
print(numeric_data.dtypes)

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(numeric_data)

# Display the shape of the scaled data
print(f'Scaled data shape: {X_scaled.shape}')


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


# Step 7: Initialize models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42, max_depth=10),
    "Random Forest": RandomForestRegressor(random_state=42, n_estimators=100),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42, n_estimators=100, learning_rate=0.1)
}


# Step 8: Train and evaluate models with additional metrics
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    # Store results
    results[name] = {'R²': r2, 'MAE': mae}

    # Step 9: Display all metrics
print("Model Performance Metrics:")
for name, metrics in results.items():
    print(f"\n{name}:")
    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.4f}")


        