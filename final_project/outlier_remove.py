#!/usr/bin/python
import pickle
import numpy as np
from sympy.physics.quantum.circuitplot import matplotlib

from tools.feature_format import featureFormat, targetFeatureSplit


# def outlier_remove(data, features):
#     assert data.shape[1] == len(features)
#     target = data[:, 0]
#     features = data[:, 1:]
#     return target, features
def reject_outliers(data, m = 2):
    svals = []
    for i in range(1, data.shape[1]):
        column = data[:, i]
        d = np.abs(column - np.median(column))
        mdev = np.median(d)
        s = d/mdev if mdev else 0.
        svals.append(s)




features_list = ['poi', 'salary', 'bonus']
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)
data = featureFormat(data_dict, features_list)

data_cleaned = reject_outliers(data)
for point in data:
    salary = point[1]
    bonus = point[2]
    matplotlib.pyplot.scatter(salary, bonus)


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()