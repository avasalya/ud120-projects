#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

#%%
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score
from matplotlib import style
import matplotlib.pyplot as plt

# print(features_train.shape)
# plt.(features_train)

clf = svm.SVC(kernel="rbf", C=10000)

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]


clf.fit(features_train, labels_train)

#%%

pred = clf.predict(features_test)
# print(pred[10])
# print(pred[26])
# print(pred[50])

acc = accuracy_score(pred, labels_test)
print(acc) #.98407


c = 0
s = 0
for i in range(len(pred)):

    if pred[i] == 1:
        c += 1
    else:
        s += 1

print('chris', c)
print('sara', s)


#########################################################


