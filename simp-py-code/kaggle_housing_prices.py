import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
# open the csv file unsing pandas

train_data_path = 'C:/Users/user/kaggle_price_of_bulding_project/train.csv'
train_data = pd.read_csv(train_data_path)

# some values are missing,to drop them use the code below

# create a list of features from the 'train.csv' file which the model can be trained from
house_features = ['MSSubClass' ,'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', '1stFlrSF', '2ndFlrSF', 'TotRmsAbvGrd']

X= train_data[house_features]

y = train_data.SalePrice

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)
housing_price_model = RandomForestRegressor(random_state = 1)

# fit the features and the prices of the houses

housing_price_model.fit(X, y)

prediction = housing_price_model.predict(val_X)

print(mean_absolute_error(val_y, prediction))

# after the features and the prices have been fit we need to test our model
# the test data is what is being used to test the model

test_data_path = 'C:/Users/user/kaggle_price_of_bulding_project/test.csv'
test_data = pd.read_csv(test_data_path)

test_X = test_data[house_features]

# predict the house prices in the test_data using the val_X

predicted_sale_prices_for_test_data = housing_price_model.predict(test_X)
print(predicted_sale_prices_for_test_data)