import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib
from sklearn.tree import DecisionTreeRegressor

# Load our data set
# df = pd.read_csv("../../Downloads/house_data.csv")
df = pd.read_csv(r"house_data.csv")
# Create the X and y arrays
X = df[["sq_feet", "num_bedrooms", "num_bathrooms"]]
y = df["sale_price"]
# Split the data set in a training set (75%) and a test set (25%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
# Create the Linear Regression model
linear_model = LinearRegression()

decision_model = DecisionTreeRegressor()
# Train the model
linear_model.fit(X_train, y_train)
decision_model.fit(X_train, y_train)
# Save the trained model to a file so we can use it to make predictions later
joblib.dump(linear_model, 'linear_house_value_model.pkl')
joblib.dump(decision_model, 'decision_house_value_model.pkl')
# Report how well the model is performing
print("Linear Regression Model training results:")
# Report an error rate on the training set
mse_train = mean_absolute_error(y_train, linear_model.predict(X_train))
print(f" - Training Set Error: {mse_train}")
# Report an error rate on the test set
mse_test = mean_absolute_error(y_test, linear_model.predict(X_test))
print(f" - Test Set Error: {mse_test}")

# Report how well the model is performing
print("Decision Tree Model training results:")
# Report an error rate on the training set
mse_train = mean_absolute_error(y_train, decision_model.predict(X_train))
print(f" - Training Set Error: {mse_train}")
# Report an error rate on the test set
mse_test = mean_absolute_error(y_test, decision_model.predict(X_test))
print(f" - Test Set Error: {mse_test}")
