#!/usr/bin/python

#%%

from sklearn.metrics import mean_squared_error, mean_absolute_error
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """


    ### your code goes here
    e = (net_worths - predictions)**2
    # print(sorted(e, reverse=True))
    cleaned_data = zip(ages, net_worths, e)
    cleaned_data = sorted(cleaned_data, key = lambda x:x[2], reverse=True) #sort based on 3rd column
    tenpercent = int(len(cleaned_data)*.1) #remove top 10 percent


    return cleaned_data[tenpercent:]
