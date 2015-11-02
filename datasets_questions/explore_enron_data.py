#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

def to_key(name):
    return ' '.join([' '.join(name.upper().split(' ')[::-1])])


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

a=0
b=0
c=0
d=0
e=0
for k,v in enron_data.items():
    if v['poi'] == 1: a +=1
    if v['salary'] != 'NaN': b +=1
    if v['email_address'] != 'NaN': c +=1
    if v['total_payments'] == 'NaN': d +=1
    if v['poi'] == 1 and v['total_payments'] == 'NaN': e +=1

print 'total data points: {} features: {}, pois: {}'.format(len(enron_data), len(enron_data.itervalues().next()), a)

with open('../final_project/poi_names.txt') as poi_names:
    for i, l in enumerate(poi_names):
        pass
    print 'there are {} names in the list'.format(i-1)

print 'James Prentice got {} stocks'.format(enron_data['Prentice James'.upper()]['total_stock_value'])

person = to_key('Wesley Colwell')
print '{} sent {} emails to POIs'.format(person,
                                         enron_data[person]['from_this_person_to_poi'])

person = to_key('Jeff Skilling')
print '{} has {} exercised_stock_options'.format(person,
                                         enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
print 'salary have: {} persons, email {}'.format(b,c)
print '{} percent of records have NaN in total payments'.format(d*100/len(enron_data))
print '{} pois with NaN total payments'.format(e*100/len(enron_data))
