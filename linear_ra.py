import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

drc = pd.read_csv('C:\Users\lbarry\Dropbox\Programming Notes\Thinkful\data sci\data_files\drc.csv')
print(drc[0:3])  # reference 3 rows of data

#drc = drc[drc["Grade"] == 8]  # filter the data
#drc = drc[drc["subject"] == 1]
#drc = drc[drc["Type"] == 1]
'''
teachers = {}  # take teacher and assign a number to that teacher
def teacher_index(tchr):
    if tchr not in teachers:
        print("%3d: %s" % (len(teachers), tchr))  # prints teachers
        teachers[tchr] = len(teachers)
    return teachers[tchr]
drc["Teachers Name"] = drc["Teachers Name"].map(teacher_index)  # assigns teachers to number
'''

plt.figure()
a = pd.scatter_matrix(drc, alpha=0.05, figsize=(10,10), diagonal='hist')  # multiple scatter matrix - all columns must be number
plt.show()

#type = drc["Type"]
pl = drc["pl"]
grade = drc["FinalGrade"]

# The dependent variable
y = np.matrix(pl).transpose()
# The independent variables shaped as columns
x1 = np.matrix(grade).transpose()
#x2 = np.matrix(type).transpose()


x = np.column_stack([x1])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print (f.summary())




