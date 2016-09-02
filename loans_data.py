import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

loansData = pd.read_csv('C:\Users\lbarry\Dropbox\Programming Notes\Thinkful\data sci\data_files\loansData.csv')
plt.figure()
p = loansData['FICO.Score'].hist()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print(f.summary())






