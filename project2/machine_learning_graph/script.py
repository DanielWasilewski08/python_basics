import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


music_data = pd.read_csv("project2/machine_learning_graph/music.csv")
X = music_data.drop(columns="genre")
y = music_data["genre"]

model = DecisionTreeClassifier()
model.fit(X, y)

tree.export_graphviz(model, out_file="project2/machine_learning_graph/music-recommender.dot",
                     feature_names=["age","gender"],
                     class_names=sorted(y.unique()),
                     label='all',
                     rounded=True,
                     filled=True)