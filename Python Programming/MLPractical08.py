
import numpy as np
from sklearn.preprocessing import Normalizer
X = np.array( [ [4, 1, 2, 2],
                [1, 3, 9, 3],
                [5, 7, 5, 1]  ]  )

transformer = Normalizer()
transformer = transformer.fit(X)  # fit does nothing.

transformed_Xdata = transformer.transform(X)
print( transformed_Xdata )









