# To fetch the Data on live server by python

import numpy
import urllib.request

# live url path
web_path = urllib.request.urlopen( "https://goo.gl/QnHW4g" )

# delimiter use of separate the columns by the comma
dataset = numpy.genfromtxt(web_path,   delimiter=",")

print( dataset)

print( "Shape of Data from Url : " ,   dataset.shape  )

for l in dataset  :
    print( l  )
