import pandas as pd
import numpy as np
from os.path import join
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('C:\Users\lbarry\Dropbox\Programming Notes\Thinkful\data sci\data_files\loanStats3b.csv', header=0, low_memory=False)

df = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
#converts string to datetime object in pandas
df['list_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('list_d_format')
year_month_summary = dfts.groupby(lambda x: x.year*100+x.month).count()
loan_count_summary = year_month_summary['issue_d']
print(plt.plot(loan_count_summary))
print(plt.show())

'''The graph appears very zig-zagged. It could be due to the fact that there are few data-points. To answer if a series is stationary or not, we need a much larger data-set to see if the graph is smooth or if it has noises and spikes. There are many ways to transform a series to stationary series; we can divide each data-point by the median or mean of the set, and that will make the series stationary. This is one way.'''


fig = sm.graphics.tsa.plot_acf(df['loan_amnt'])
fig.set_size_inches(18.5, 10.5)
fig.savefig('C:/Users/lbarry/Desktop/acf.png', dpi=100)
fig2 = sm.graphics.tsa.plot_pacf(df['loan_amnt'])
fig2.set_size_inches(18.5, 10.5)
fig.savefig('C:/Users/lbarry/Desktop/pacf.png', dpi=100)


'''the images show that there are some correlation as both the auto and partial correlation values are greater or less than zero. If all the values were zeros, then there were no correlation. Since that's the case here, thus there are correlation between the points at time = t and time = t + dt.'''

