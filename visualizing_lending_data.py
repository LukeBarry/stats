import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')  # load the data

loansData.dropna(inplace=True)  # remove rows with null values

loansData.boxplot(column='Amount.Funded.By.Investors')  # box plot
plt.show()

loansData.hist(column='Amount.Funded.By.Investors')  # histogram
plt.show()

# generate a qq plot
import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()