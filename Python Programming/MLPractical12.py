
# density plot
from matplotlib import pyplot as plt

import pandas

filename = 'indians-diabetes.data.csv'

headingnames = ['preg', 'plas', 'pres', 'skin', 'test',
                'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(filename, names=headingnames)
# shareX= false use for separate x axise for every plot and image
dataframe.plot(kind='density', subplots=True, layout=(5,2), sharex=False )

plt.show()
