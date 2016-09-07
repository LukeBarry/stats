import pandas as pd
import numpy as np
import statsmodels.api as sm
from math import e
import pylab
import matplotlib.pyplot as plt
''' Cleaning the data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Loan.Length'] = cleanLoanLength
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
loansData['constant'] = 1
IR_TF = loansData['Interest.Rate'].map(lambda x: int(x >= .12))
loansData['IR_TF'] = IR_TF
loansData.to_csv('loansData_clean.csv', header=True, index=False)
'''

# What is the probability of getting a loan from the Lending Club for $10,000
# at an interest rate less than or equal to 12% with a FICO score of 750?

df = pd.read_csv("loansData_clean.csv")  # cleaning data wasn't needed, loading clean data here
ind_vars = ['Amount.Funded.By.Investors', 'FICO.Score', 'constant']
logit = sm.Logit(df['IR_TF'], df[ind_vars])
result = logit.fit()

coeff = result.params
print coeff

FicoScore = 720
LoanAmount = 10000

def logistic_function(LoanAmount, FicoScore, coeff):
    px = 1 / (1 + e **(coeff[2] + coeff[1]*(FicoScore) + coeff[0]*(LoanAmount)))
    print (coeff[2] + coeff[1]*(FicoScore) + coeff[0]*(LoanAmount))
    return px

print(logistic_function(LoanAmount, FicoScore, coeff))








