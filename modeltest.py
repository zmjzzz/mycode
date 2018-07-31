from sklearn import datasets
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn import svm
iris = datasets.load_iris()
digits = datasets.load_digits()
clf = RandomForestClassifier(n_estimators=2000, verbose=1)
clf.fit(iris.data, iris.target)
print(clf.feature_importances_)
print(clf.n_features_)
print(clf.n_outputs_)
print(clf.estimators_)
param_dist = {"max_depth": (3, None),
              "max_features": (1,2,3,4),
              "min_samples_split": (1,2,3,4),
              "min_samples_leaf": (1,5,10,15),
              "bootstrap": (True, False),
              "criterion": ('gini', 'entropy'),
              "n_estimators": range(10,200,1)}
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
GS = GridSearchCV(clf, param_grid=param_dist)
GS.fit(iris.data, iris.target)


