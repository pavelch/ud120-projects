#!/usr/bin/python

import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for age, net, prediction in zip(ages, net_worths, predictions):
        error = math.fabs(prediction - net)
        data = (age, net, error)
        cleaned_data.append(data)

    cleaned_data = sorted(cleaned_data, key=lambda cleaned: cleaned[2])

    cleaned_data = cleaned_data[:int(len(cleaned_data)*0.9)]
    # cleaned_data = cleaned_data[10:]
    print 'cleaned data lenght is: {}'.format(len(cleaned_data))

    return cleaned_data

