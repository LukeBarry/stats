import pandas as pd
import csv
import matplotlib.pyplot as plt
import scipy.stats as stats
import collections
import statsmodels.api as sm
import numpy as np



predict = pd.read_csv('C:/Users/lbarry/Desktop/stats data/predicting pssa/prediction.csv')
predict.dropna(inplace=True)

predict.boxplot(column='pvaas')
plt.show()

predict.hist(column='pvaas')
plt.show()


plt.figure()
graph = stats.probplot(predict['pvaas'], dist="norm", plot=plt)
plt.show()

freq = collections.Counter(predict['pvaas'])
print freq

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

p=stats.chisquare(list(freq.values()))
print p

a = pd.scatter_matrix(predict, alpha=0.05, figsize=(10,10), diagonal='hist')
print a

pvaas = predict['pvaas']
bm = predict['bm']
passtest = predict['passtest']

y = np.matrix(passtest).transpose()
# The independent variables shaped as columns
x1 = np.matrix(pvaas).transpose()
x2 = np.matrix(bm).transpose()

x = np.column_stack([x1,x2])
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
f.summary()

ind_vars=['pvaas', 'bm']
logit = sm.Logit(predict['passtest'], predict[ind_vars])
result = logit.fit()

coeff = result.params
print(coeff)

# Here is the logistic function with the pvaas and bm coefficients added in.  I set the y int = 1 in the excel sheet.
# p(x) = 1/(1 + e^(intercept + 0.079806(pvaas) − 0.069370(bm))