from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# cleaning the data
data = pd.read_csv('music_data.csv')
inputData = data.drop(columns='suggested_genre')
output = data['suggested_genre']

musicDict = {
    "0":"Rock",
    "1":"Metal",
    "2":"Punk",
    "3":"Grunge",
    "4":"Alternative",
    "5":"Pop",
    "6":"K-Pop",
    "7":"Indie Pop",
    "8":"Synthpop",
    "9":"Pop Rock",
    "10":"Hip Hop",
    "11":"Rap",
    "12":"Trap",
    "13":"R&B",
    "14":"Trap Soul",
    "15":"Electronic",
    "16":"EDM",
    "17":"Techno",
    "18":"House",
    "19":"Trance",
    "20":"Country",
    "21":"Folk",
    "22":"Bluegrass",
    "23":"Jazz",
    "24":"Blues",
    "25":"Fusion",
    "26":"Classical",
    "27":"Orchestral",
    "28":"Chamber Music",
    "29":"Reggae",
    "30":"Ska",
    "31":"Dancehall",
    "32":"Latin",
    "33":"Salsa",
    "34":"Bachata",
    "35":"Reggaeton",
    "36":"World",
    "37":"Ethnic",
    "38":"None"
}

class User:
    def __init__(self, age, gender, firstGenre, secondGenre, thirdGenre):
        self.age = int(age)
        self.gender = int(gender)
        self.firstGenre = int(firstGenre)
        self.secondGenre = int(secondGenre)
        self.thirdGenre = int(thirdGenre)

def genreRecommender(age, gender, firstGenre, secondGenre, thirdGenre):
    global inputData
    global output
    global musicDict
    
    # train our model
    inputData_train, inputData_test, output_train, output_test = train_test_split(inputData, output, test_size=0.2)
    # algorithms
    classifier2 = LinearRegression()
    classifier2.fit(inputData_train, output_train)
    score = classifier2.score(inputData_test, output_test)

    predictions = round(float(np.array([classifier2.predict([[age, gender, firstGenre, secondGenre, thirdGenre]])])))

    print(f'We are {round(score*100)}% confident you would like to listen to some {musicDict[str(predictions)]}')

def start():
    
    age = input("Throw how many summers have you been through?\n")
    gender = input("What is your gender?\n 0. Man\n 1. Woman\n")
    for item in musicDict:
        print(item)
    print("Choose three options from the above:\n")
    firstGenre = input("First option:\n")
    secondGenre = input("Second option:\n")
    thirdGenre = input("Third option:\n")
    
    user = User(age, gender, firstGenre, secondGenre, thirdGenre)
    
    genreRecommender(user.age, user.gender, user.firstGenre, user.secondGenre, user.thirdGenre)
    
start()