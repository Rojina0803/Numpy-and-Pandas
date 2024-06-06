import numpy as np
import pandas as pd
#LABELINGG
# lables=['a','b','c']
# my_data=[1,2,3]
# print(pd.Series(data=my_data))
# llb=pd.Series(data=my_data,index=lables)
# print(llb)

# lablee=["USA","UK","UAE"]
# datas=["1.3M","4.6M","5.7M"]
# print(pd.Series(data=datas, index=lablee))

# ser1=pd.Series(data=[1,2,3,4],index=["AUS","NEP","GER","EUR"])
# print(ser1)
# print(ser1["AUS"])

# df= pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
# print(df)
# print(df['W']['A'])
# print("COLUMN: ",df['W'])
# print("COLUMN: ",df['X'])
# print("ROW:",df.loc['A']) # indexing of row
# print(df.loc['A']['W'])
# print(df[['W','X']])
# print(df[['W','X']].loc[['A','B']])
# print(df.loc[['A','B'],['W','X']])
# print(df.loc[['A','B'],['Y','Z']])
# print(df.loc[['C','E'],['W','Z']])
# print(df>0)
# print(df[df>0])
# print(df[df['X']<0])
# print(df[df['X']>0][['X','Y']])

#MISSING DATAS
d={
    'A':[1,np.nan,3],
    'B':[4, np.nan,5],
    'C':[6,7,8]
    
}
data=pd.DataFrame(d)
print(data)
print(data.dropna()) #default=0, works in row,drops the whole row if it contains nan
print(data.dropna(axis=1)) #works in column,drops the whole column if it contains nan

d1={
    'A':[1,np.nan,3],
    'B':[4, np.nan,5],
    'C':[6,7,np.nan]
}
data1=pd.DataFrame(d1)
print(data1)
print(data1.dropna())
print(data1.dropna(axis=1))
# print(data1.dropna(inplace=True))
print(data1.fillna(value=1))
print(data1.describe())
print(data1.info())
print(data1.groupby("A"))



