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
def collect_svalues(data):
    svals = []
    for i in range(1, data.shape[1]):
        column = data[:, i]
        d = np.abs(column - np.median(column))
        mdev = np.median(d)
        s = d / mdev if mdev else 0.
        svals.append(s)

    return svals


def drop_outliers(data):
    svals = collect_svalues(data)
    leavein = []
    out = []
    for inx, item in enumerate(svals[0]):
        compare_with = [row[inx] for row in svals]
        compare = map(lambda x: x < 10, compare_with)
        print '{}, {}'.format(compare_with, compare)
        if False not in compare:
            leavein.append(data[inx])
        else:
            out.append(data[inx])

    return np.array(leavein), np.array(out)


features_list = ['poi', 'salary', 'bonus']
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)
data = featureFormat(data_dict, features_list)

svalues = collect_svalues(data)

data_cleaned, outliers = drop_outliers(data)
for point in outliers:
    salary = point[1]
    bonus = point[2]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
