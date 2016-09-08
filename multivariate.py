import pandas as pd
import numpy as np
import statsmodels.api as sm

key = pd.read_csv('C:\Users\lbarry\Desktop\keystone.csv')
print(key[0:2])


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


y = np.matrix(score).transpose()
x1 = np.matrix(subject).transpose()
x2 = np.matrix(grade_level).transpose()
x3 = np.matrix(year).transpose()
x4 = np.matrix(retest).transpose()
x5 = np.matrix(score_level).transpose()
x6 = np.matrix(multiple_choice).transpose()
x7 = np.matrix(constructed_response).transpose()
x8 = np.matrix(gender).transpose()
x9 = np.matrix(ethnicity).transpose()
x10 = np.matrix(iep).transpose()
x11 = np.matrix(poverty).transpose()
x12 = np.matrix(underperforming_subgroup).transpose()
x13 = np.matrix(recently_enrolled).transpose()
x14 = np.matrix(enrolled_year_ago).transpose()
x15 = np.matrix(type).transpose()
x16 = np.matrix(teacher_number).transpose()

x = np.column_stack([x1, x16, x15])
X = sm.add_constant(x)
model = sm.OLS(y, X)
f = model.fit()
print (f.summary())






