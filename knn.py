import pandas as pd
import numpy as np
import math


def knn(k):
    """Finds the majority class for the k nearest neighbors"""
    nearestK = data.sort_values('distance')[['class', 'distance']][1:k]
    majority_class = nearestK.groupby('class').count().idxmax()[0]
    print("kNN({}) = {}".format(k, majority_class))

data = pd.read_csv('iris.data.csv', sep=',', header=None, engine='python')
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

# data.plot.scatter('sepal length', 'sepal width')

rand = np.random.randint(0,data.__len__())
rand_point = data.ix[rand]
rp_x = rand_point['sepal length']
rp_y = rand_point['sepal width']

data['distance'] = data.apply(lambda x: math.sqrt((rp_x - x['sepal length'])**2 + (rp_y - x['sepal width'])**2), axis=1)

# commenting 3 rows out since they are included in knn(k) function
# nearest10 = data.sort_values('distance')[['class', 'distance']][1:11]
# majority_class = nearest10.groupby('class').count().idxmax()[0]
# print(majority_class)

knn(10)
knn(144)
knn(3)