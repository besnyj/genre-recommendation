import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# cleaning the data
data = pd.read_csv('genre.csv')
input = data.drop(columns='country')
output = data['country']

# train our model
input_train, input_test, output_train, output_test = train_test_split(input, output, train_size=0.2)

# algorithms
classifier2 = KNeighborsClassifier(n_neighbors=3)
classifier2.fit(input, output)
predictions2 = classifier2.predict([[23, 0, 1, 1, 0, 0, 0, 1, 1]])
print(predictions2)

levelOfCertainty2 = classifier2.score(input_test, output_test)
print(levelOfCertainty2)

# gender: men 0, women 1
# data: no 0, yes 1