import pandas as pd
from sklearn import datasets
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import svm
iris = datasets.load_iris()
digits = datasets.load_digits()
clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
jpdata=pd.read_csv("E:/all03.csv")