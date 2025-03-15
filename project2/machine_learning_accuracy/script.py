#might be done on jupyter. Machine learning data from course. 
import pandas as pd #imported library to open csv
from sklearn.tree import DecisionTreeClassifier #machine learning library
from sklearn.model_selection import train_test_split #machine learning library to split data for training and testing
from sklearn.metrics import accuracy_score #machine learning library to evaluate accuracy

#deviding data for training and testing (% can be changed in 11th line)
music_data = pd.read_csv("project2/machine_learning_accuracy/music.csv")
X = music_data.drop(columns="genre")
y = music_data["genre"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

#making predictions
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

#results evaluation
score = accuracy_score(y_test, predictions)
print(score)