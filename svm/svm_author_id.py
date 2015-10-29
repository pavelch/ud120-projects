#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from tools.email_preprocess import  preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def timing(f):
    def wrap(*args):
        time1 = time()
        ret = f(*args)
        time2 = time()
        print '{} function took {} ms'.format(f.func_name, (time2-time1))
        return ret
    return wrap

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

x=10000
clf = SVC(C=x, kernel="rbf")
timing(clf.fit)(features_train, labels_train)

pred = timing(clf.predict)(features_test)
accuracy = accuracy_score(labels_test, pred)

a=0
i=0
while i < len(pred):
    if pred[i] == 1:
       a +=1
    i +=1


print 'x={}, accuracy={}'.format(x, accuracy)
# print '10 is {}, 26 is {}, 50 is {}'.format(pred[10], pred[26], pred[50])
print 'in the Cris(1) class predicted to be {} events'.format(a)


#########################################################


