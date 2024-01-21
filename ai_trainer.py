import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn import preprocessing
import joblib

read_from_csv = pd.read_csv('Remi++.csv')
#remove the spaces from the column names
read_from_csv = read_from_csv.rename(columns=lambda name: name.strip())


variables = read_from_csv[["MATCHMAKING_ATTEMPT_START_TIME_UTC","MATCHMAKING_DAY_OF_WEEK", "PLAYER_ROLE", "PARTY_SIZE", "SERVER_NAME", "MMR_GROUP_DECILE"]].values
time_estimate = read_from_csv["QUEUE_DURATION_IN_SECS"].values

#encode the variables into numerical values
le_list_x = []
for i in range(len(variables[0])):
    le = preprocessing.LabelEncoder()
    variables[:, i] = le.fit_transform(variables[:, i])
    le_list_x.append(le)


#encode the time estimate into numerical values
le_y = preprocessing.LabelEncoder()
time_estimate = le_y.fit_transform(time_estimate)


#split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(variables, time_estimate, test_size=0.2, random_state=0)


model = LinearRegression()

model.fit(x_train, y_train)

# Here we are using the model to predict the result using the same variables that it was trained with
predictions = model.predict(x_test)
#convert the predictions into integers
predictions = predictions.astype(int)

#decode the predictions
predictions = le_y.inverse_transform(predictions)
print("Predictions: ", predictions)

# Here we will see how good our project is working by calculating the 
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')


#Here we will see the accuracy of our model
accuracy = model.score(x_test, y_test)
print("Number of tests: ", len(x_test))

print("Testing set accuracy: {:.2f}%".format(accuracy * 100))

#Here we will save the model we have made and this will allow us to do all the operations on flask
joblib.dump(model, 'your_model.pkl')
joblib.dump(le_list_x, 'le_list_x.pkl')
joblib.dump(le_y, 'le_y.pkl')

