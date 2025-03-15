import pandas as pd #import csv library
from sklearn.tree import DecisionTreeClassifier #importing machine-learning model
from sklearn import tree #importing tree concerning machine-learning proccesses


music_data = pd.read_csv("project2/machine_learning_graph/music.csv") #importing csv file
X = music_data.drop(columns="genre") #data for input
y = music_data["genre"] #data for output

model = DecisionTreeClassifier() #machine-learning model
model.fit(X, y)
#creating a graph with given features
tree.export_graphviz(model, out_file="project2/machine_learning_graph/music-recommender.dot",
                     feature_names=["age","gender"],
                     class_names=sorted(y.unique()),
                     label='all',
                     rounded=True,
                     filled=True)