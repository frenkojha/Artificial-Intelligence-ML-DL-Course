
# MinMax Scaler use to perform min and max operations
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# numpy array use for advance calculation of arrays
data = np.array( [[-1,    2],
                  [-0.5,  6],
                  [0,    10],
                  [1,    18] ]  )

print( data )

scaler = MinMaxScaler(feature_range=(1, 5))
scaler.fit(data)
print("Minimum Values : " , scaler.data_min_)
print("Maximum Values : " , scaler.data_max_)
# re scaled the data between 1 to 5
rescaledX = scaler.transform(data)
print( rescaledX )
