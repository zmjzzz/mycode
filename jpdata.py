import pandas as pd
from sklearn import datasets
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn import svm
jpdata=pd.read_csv("E:/all03.csv")
print(jpdata)
