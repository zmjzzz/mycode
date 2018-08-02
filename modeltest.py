from sklearn import datasets
import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn import svm
iris = datasets.load_iris()
digits = datasets.load_digits()
clf = RandomForestClassifier(n_estimators=10, verbose=1, n_jobs=-1)
clf.fit(iris.data, iris.target)
param_dist = {#"max_depth": (3, None),
              #"max_features": (1,2,3,4),
              #"min_samples_split": (2,3,4),
              #"min_samples_leaf": (1,5,10,15),
              "bootstrap": (True, False),
              "criterion": ('gini', 'entropy'),
              "n_estimators": range(10, 200, 1)
             }
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
start_time = time.time()
GS = GridSearchCV(clf, param_grid=param_dist, verbose=1)
GS.fit(iris.data, iris.target)
end_time = time.time()
print("time cost:", end_time-start_time)
print(clf.feature_importances_)
print(GS.best_estimator_)
print(GS.best_params_)
print(GS.best_score_)

