# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(shashiraj)sip
"""

list1 = [1,2,3,4,5]
list1
type(list1)
#%%
list2=[6,7,8,9]
list2
type(list2)
#%%
list3 = ['a','c','d','e']
list3
type(list3)
#%%
tuple1 = (1,2, 'a', 'b')
tuple1
type(tuple1)
#%%
tuple2=[3,4,'c','d']
tuple2
type(tuple2)
#%%
dict1 = {1:'Ramesh', 2:'Suresh', 3:'Priyanka'}
dict1
type(dict1)
#%%
set1 =['india', 'pakistan', 'england', 'australia','india']
set1
type(set1)
#%%
str1 = 'Python Programming'
type(str1)
#%%
list1
for i in list1:
    print(i)
tuple1
for i in tuple1:
    print(i)
for i in range(1, 10, 2):
    print(i, end=' ')
 #%%
 tupleFZ1 = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
type(tupleFZ1)    
#%%
frozenset1 = frozenset(tupleFZ1) 
frozenset1
type(frozenset1)

dict1
frozenset2 = frozenset(dict1)
type(frozenset2)
frozenset2
#%%
name = [ "Dhiraj", "Kounal", "Akhil", "Pooja" ] 
rollno = [ 4, 1, 3, 2 ] 
marks = [ 90, 50, 60, 70 ]
mapped = zip(name, rollno, marks)
mapped = set(mapped) 
mapped
namez, rollnoz, marksz = zip(*mapped)
namez
#%%
import numpy as np
np1 = np.arange(1,10)
np1
type(np1)
np
np2 = np.array([ 90, 50, 60, 70 ])
np2
np.sort(np2)

np3 = np.array([[1,4],[3,1]])
np3
np3.shape
#%%
import pandas as pd
pd
df1 = pd.DataFrame({'rollno':[1,2,3,4], 'name': [ "Dhiraj", "Kounal", "Akhil", "Pooja" ], 'marks':[ 40, 50, 60, 70 ], 'gender':['M','M','M','F']})
df1
type(df1) 

df1.columns
df1.describe
df1.dtypes
df1.shape
df1.groupby('gender').size()
df1.groupby('gender')['marks'].mean()
df1.groupby('gender').aggregate({'marks': [np.mean, 'max']})
#%%
import matplotlib.pyplot as plt
df1.groupby('gender').size().plot(kind='bar')
import seaborn as sns
iris = sns.load_dataset("iris")
sns.pairplot(iris)
#%%
import statsmodels.api as sm
mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
mtcars.data.head()
data = mtcars.data
data.head()
data.to_csv('exportcsv1.csv')
data.to_excel('exportexcel1.xlsx','sheet1', header=False)
data2a = pd.read_csv('exportcsv1.csv')
data2a.head()

data2b = pd.read_excel('exportexcel1.xlsx','sheet1')
data2b.head()