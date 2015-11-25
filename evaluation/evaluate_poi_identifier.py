#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, precision_recall_fscore_support
from sklearn.tree import tree

sys.path.append("../tools/")
from tools.feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(labels_test, pred)
print 'accuracy:{}'.format(acc)
nopoi = [0]*29
acc_nopoi = accuracy_score(labels_test, nopoi)
print 'accuracy1:{}'.format(acc_nopoi)

prec = precision_score(labels_test, pred)
print 'precision score: {}'.format(prec)

rec = recall_score(labels_test, pred)
print 'recall score: {}'.format(rec)

predictions =  [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
pr, re, fb, su = precision_recall_fscore_support(true_labels, predictions)
print '{}\n{}\n{}\n{}'.format(pr, re, fb, su)



