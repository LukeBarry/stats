import pandas as pd
import numpy as np
import statsmodels.api as sm

key = pd.read_csv('C:\Users\lbarry\Desktop\keystone.csv')
#print(key[0:2])


subject=key['subject']
grade_level=key['grade_level']
year=key['year']
retest=key['First Time Or Re-Test']
score=key['score']
score_level=key['score_level']
multiple_choice=key['multiple_choice']
constructed_response=key['constructed_response']
gender=key['gender']
ethnicity=key['ethnicity']
iep=key['iep']
poverty=key['poverty']
underperforming_subgroup=key['underperforming_subgroup']
recently_enrolled=key['recently enrolled']
enrolled_year_ago=key['enrolled_year_ago']
type=key['type']
teacher_number=key['teacher_number']


y1 = np.matrix(score).transpose()
y2 = np.matrix(score_level).transpose()
y3 = np.matrix(multiple_choice).transpose()
y4 = np.matrix(constructed_response).transpose()

x1 = np.matrix(subject).transpose()
x2 = np.matrix(grade_level).transpose()
x3 = np.matrix(year).transpose()
x4 = np.matrix(retest).transpose()
x5 = np.matrix(gender).transpose()
x6 = np.matrix(ethnicity).transpose()
x7 = np.matrix(iep).transpose()
x8 = np.matrix(poverty).transpose()
x9 = np.matrix(underperforming_subgroup).transpose()
x10 = np.matrix(recently_enrolled).transpose()
x11 = np.matrix(enrolled_year_ago).transpose()
x12 = np.matrix(type).transpose()
x13 = np.matrix(teacher_number).transpose()

x = np.column_stack([x1,x7,x9,x13])
X = sm.add_constant(x)
model = sm.OLS(y1, X)
f = model.fit()
print (f.summary())

# x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13



