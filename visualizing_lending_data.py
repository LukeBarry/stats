import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections


loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')  # load the data

loansData.dropna(inplace=True)  # remove rows with null values

loansData.boxplot(column='Amount.Funded.By.Investors')  # box plot
plt.show()

loansData.hist(column='Amount.Funded.By.Investors')  # histogram
plt.show()

# generate a qq plot
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()

# apply chi squared test to lending data
# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)
# Apply the collections.Counter() method on the number of open credit lines in the Loans data (Open.CREDIT.Lines)
# to get counts of observations for each number of credit lines.
freq = collections.Counter(loansData['Open.CREDIT.Lines'])
#print (freq)

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

chi, p = stats.chisquare(freq.values())
print (p)
print(chi)







