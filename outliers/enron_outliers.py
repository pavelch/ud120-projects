#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from tools.feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

salaries = []
bonuses = []
for item in data:
    salary = item[0]
    bonus = item[1]
    salaries.append(salary)
    bonuses.append(bonus)
max_salary = max(salaries)
for k, v in data_dict.iteritems():
    if v['salary'] == max_salary:
        owner = k
print 'max salarie is: {}, of : {}'.format(max_salary, owner)

### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    if salary != max_salary:
        matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


