
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import pandas

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres', 'skin',
        'test', 'mass', 'pedi', 'age', 'class']

df = pandas.read_csv(filename, names=hnames)

print( df )
# hist use for visualize data
df.hist()
# tight_layout use for giving sufficient space for every plot
plt.tight_layout()
plt.show()
