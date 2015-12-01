#!/usr/bin/python
import pickle

from tools.feature_format import featureFormat


def outlier_remove(data, features):
    assert data.shape[1] == len(features)
    target = data[:, 0]
    features = data[:, 1:]
    return target, features


features_list = ['poi', 'salary', 'bonus', 'expenses', 'exercised_stock_options']
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)
data = featureFormat(data_dict, features_list)

foo, bar = outlier_remove(data, features_list)

print 'end'
