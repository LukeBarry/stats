import pandas as pd

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East_Midlands,4.89,3.34
West_Midlands,5.63,3.47
East_Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern_Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]
column_names = data[0]  # this is the first row
data_rows = data[1::]  # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)
print ('Alcohol average',df['Alcohol'].mean())
print ('Alcohol median',df['Alcohol'].median())import pandas as pd

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East_Midlands,4.89,3.34
West_Midlands,5.63,3.47
East_Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51import pandas as pd

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East_Midlands,4.89,3.34
West_Midlands,5.63,3.47
East_Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern_Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]
column_names = data[0]  # this is the first row
data_rows = data[1::]  # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)
print ('Alcohol average',df['Alcohol'].mean())
print ('Alcohol median',df['Alcohol'].median())
#  mode print (stats.mode(df['Alcohol']))
print('Tobacco average',df['Tobacco'].mean())
print ('Tobacco median',df['Tobacco'].median())
#  print(stats.mode(df['Tobacco']))
print ('Alcohol range',max(df['Alcohol']) - min(df['Alcohol']))
print ('Alcohol std dev',df['Alcohol'].std())
print ('Alcohol variance',df['Alcohol'].var())
print ('Tobacco range',max(df['Tobacco']) - min(df['Tobacco']))
print ('Tobacco std dev',df['Tobacco'].std())
print ('Tobacco var',df['Tobacco'].var())

Northern_Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]
column_names = data[0]  # this is the first row
data_rows = data[1::]  # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)
print ('Alcohol average',df['Alcohol'].mean())
print ('Alcohol median',df['Alcohol'].median())
#  mode print (stats.mode(df['Alcohol']))
print('Tobacco average',df['Tobacco'].mean())
print ('Tobacco median',df['Tobacco'].median())
#  print(stats.mode(df['Tobacco']))
print ('Alcohol range',max(df['Alcohol']) - min(df['Alcohol']))
print ('Alcohol std dev',df['Alcohol'].std())
print ('Alcohol variance',df['Alcohol'].var())
print ('Tobacco range',max(df['Tobacco']) - min(df['Tobacco']))
print ('Tobacco std dev',df['Tobacco'].std())
print ('Tobacco var',df['Tobacco'].var())

#  mode print (stats.mode(df['Alcohol']))
print('Tobacco average',df['Tobacco'].mean())
print ('Tobacco median',df['Tobacco'].median())
#  print(stats.mode(df['Tobacco']))
print ('Alcohol range',max(df['Alcohol']) - min(df['Alcohol']))
print ('Alcohol std dev',df['Alcohol'].std())
print ('Alcohol variance',df['Alcohol'].var())
print ('Tobacco range',max(df['Tobacco']) - min(df['Tobacco']))
print ('Tobacco std dev',df['Tobacco'].std())
print ('Tobacco var',df['Tobacco'].var())
