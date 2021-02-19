

import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test',
          'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)

array = dataframe.values
# separate array into input and output components
# 0:8 in this case last value 8 is exclude it include only 7 values (0 to 7)
X = array[ : , 0:8]   # [ row , cols ]
# when we pass single 8 it means it include 8 values
Y = array[ : , 8]
scaler = MinMaxScaler( feature_range=(1,5) )   #Range

#First Method
rescaledX = scaler.fit_transform(X)

#Second Method
scaler = scaler.fit(X)
rescaledX = scaler.transform(X)

# summarize transformed data
set_printoptions(precision=2)

print( rescaledX [ 0:30 , : ]   )  # [ row , cols ]

print("Print the dimension of the matrix" ,data.shape)