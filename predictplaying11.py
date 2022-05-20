

import pandas as pd

dataset=pd.read_excel('batting.xlsx')
a=input("No of Batsman:\n")
a=int(a)
c= int(11 - a)

    
x= dataset.iloc[1:101,[1,4,6,8]].values
y= dataset.iloc[1:101,0].values
               
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
x=sc.fit_transform(x)

from sklearn.svm import SVC
df=SVC(kernel='rbf',random_state=0)
df.fit(x,y)
y_pred=df.predict(x)

s= []
for i in y_pred:
    if i not in s:
        s.append(i)
batsman=[]

for i in range(0,a):
    batsman.append(s[i])
    
datas = pd.read_csv('bowling.csv')

d= datas.iloc[1:78,[2,3,5,8]].values
e= datas.iloc[1:78,0].values
                 
             
from sklearn.preprocessing import StandardScaler
 
sc=StandardScaler()
d=sc.fit_transform(d)
 
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(d,e)
e_pred=classifier.predict(d)                        
                         
f = []
for i in e_pred:
    if i not in f:
        f.append(i)
bowler=[]
for i in range(0,c): 
    bowler.append(f[i])
                             
best=[]
for i in range(0,a):
    best.append(batsman[i])
    
for i in range(0,c):
    best.append(bowler[i])
    
print('Playing 11: \n' )
for i in range(0,11):
    print(best[i])  