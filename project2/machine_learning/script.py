#script with already trained model. To train it once more, code from 7-14 lines is needed 
import pandas as pd 
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.model_selection import train_test_split
import joblib

#music_data = pd.read_csv("project2/machine_learning/music.csv") # opening data to needed to train
#X = music_data.drop(columns="genre")  # deviding data for training
#y = music_data["genre"]               # -||- for testing

#model = DecisionTreeClassifier()      # machine learning model
#model.fit(X_train, y_train)           # training with input data and output data

#joblib.dump(model, "project2/machine_learning/music-recommender.joblib") #sending trained model to music-recommender.joblib 

model = joblib.load("project2/machine_learning/music-recommender.joblib") #loading model that was trained
predictions = model.predict([[21, 1] ] ) #giving him a task
print(predictions) # output of our model