import numpy
import urllib.request

web_path = urllib.request.urlopen( "https://goo.gl/QnHW4g" )

dataset = numpy.genfromtxt(web_path,   delimiter=",")

print( dataset)

print( "Shape of Data from Url : " ,   dataset.shape  )

for l in dataset  :
    print( l  )
