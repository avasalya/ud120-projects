#!/usr/bin/python
#%%
import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

from sklearn import linear_model

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

#pop out outlier
data_dict.pop('TOTAL',0)


for key in data_dict.keys():
    if data_dict[key]['bonus'] > 5000000 and data_dict[key]['bonus'] != 'NaN' :
        if data_dict[key]['salary'] > 1000000 and data_dict[key]['salary'] != 'NaN' :
            print(key, data_dict[key]['bonus'], data_dict[key]['salary'])


features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

#%%

