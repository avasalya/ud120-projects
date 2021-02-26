#!/usr/bin/python

#%%
"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
# print(len(features), len(labels))

### it's all yours from here forward!
from sklearn.cross_validation import train_test_split, StratifiedKFold
import numpy as np 
#%%

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)

from sklearn import tree

clf = tree.DecisionTreeClassifier()
# clf = tree.DecisionTreeClassifier(min_samples_split=40)

clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print(acc)

#%%

skf = StratifiedKFold(labels,n_folds=2, shuffle=True)
# print(skf)
for train_idx, test_idx in skf:
    # print(train_idx, test_idx)
    features_train, features_test = np.array(features)[train_idx.astype(int)], np.array(features)[test_idx.astype(int)]

    labels_train, labels_test = np.array(labels)[train_idx.astype(int)], np.array(labels)[test_idx.astype(int)]


from sklearn import tree

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print(acc)

