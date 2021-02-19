# Read data from the csv file in python
import numpy

filename = 'indians-diabetes.data.csv'

raw_data = open(filename , 'r')
data = numpy.loadtxt(raw_data, delimiter=",")
raw_data.close()

print( "Numpy loadtxt : " ,data.shape )    #(768,9)

print("\n\n\n")

print( data  )

print("-*-"  * 30 )

for l in data :
    print(l)
