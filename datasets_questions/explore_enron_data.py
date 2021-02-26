#!/usr/bin/python

#%%
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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

keys = enron_data.keys()
print(keys)
# print(enron_data["SKILLING JEFFREY K"]['poi'])

#%%
c = 0
pois = []
for i in range(len(enron_data)):
    if enron_data[keys[i]]['poi'] == 1:
        pois.append(keys[i])
        c +=1
print('pois', c)

names = []
with open("../final_project/poi_names.txt", "r") as f:
    for line in f.readlines():
        data = line.split()
        names.append(data[2])
print('list names', len(names))

# print(names[1].lower())
# print(pois[0].split()[1].lower())

list_common = []
for i in range(0, len(names)):
    for j in range(0, len(pois)):
        if names[i].lower() == pois[j].split()[1].lower():
            list_common.append(names[i])

print('common names', len(list_common))
print(sorted(list_common))

list_common = sorted(list_common)
# sort the list 1st

d = 0
for i in range(len(list_common)-1):
    if list_common[i] == list_common[i+1]:
        d += 1
print('duplicate', d)

# removeduplicate = list(dict.fromkeys(list_common))
# print(len(removeduplicate))
# print(removeduplicate)


#%%

print(enron_data['PRENTICE JAMES']['total_stock_value'])

#%%














































