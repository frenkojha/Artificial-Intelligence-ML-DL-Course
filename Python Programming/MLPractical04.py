# Provide headings in the row data set 

import pandas
pandas.set_option('display.width', 1000)
pandas.set_option('display.max_column', 9)

filename = 'indians-diabetes.data.csv'

# hnames denots for the heading of the data
hnames = ['preg', 'plas', 'pres',
          'skin', 'test','mass',
          'pedi', 'age', 'class']

df = pandas.read_csv(filename, names = hnames)

# df.shape use for the data shape like how manys rows and columns it content
print( "pandas Data : " , df.shape  )

print( df.dtypes )

print( df  )
