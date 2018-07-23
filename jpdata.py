import pandas as pd
from sklearn import datasets
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn import svm
iris = datasets.load_iris()
digits = datasets.load_digits()
param_dist = {"max_depth": [3, None],
              "max_features": [range(1, 11,1)],
              "min_samples_split": [range(2, 11,1)],
              "min_samples_leaf": [range(1, 11,1)],
              "bootstrap": [True, False],
              "criterion": ['gini', 'entropy']}
clf=RandomForestClassifier(n_estimators=20)
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
jpdata=pd.read_csv("E:/all03.csv")
print(jpdata)
GS=GridSearchCV(param_dist)
GS.fit(iris.data,iris.target)