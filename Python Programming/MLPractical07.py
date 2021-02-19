from sklearn.preprocessing import StandardScaler
from pandas import read_csv
import numpy as np

filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test',
         'mass', 'pedi', 'age', 'class']

dataframe = read_csv(filename, names=names)
array = dataframe.values

# separate array into input and output components
X = array[: , 0:8]
Y = array[:,8]

scaler = StandardScaler()
rescaledX = scaler.fit_transform(X)

print( rescaledX[ :30 , :] )

print( "\n\nMean of First coloum=" , end="")
print( np.mean(rescaledX[ : , 0]) )



print("\n\n")
print("Mean = \n", np.mean(rescaledX, axis=0)  )
