'''
Flash_episode	Flash_us_viewers	GoT_episode	GoT_us_viewers
1	4.83	1	2.84
2	4.27	2	2.32
3	3.59	3	2.55
4	3.53	4	2.49
5	3.46	5	2.73
6	3.73	6	2.6
7	3.47	7	2.64
8	4.34	8	3.92
9	4.66	9	3.06

import re
f = open('LR_Episodes.csv' ,"r")

lines = f.readlines()
for i in range( len(lines) ):
    print( re.sub("\s+", "," , lines[i])

f.close()


Step by steps to solving this problem:
First we have to convert our data to x_parameters and y_parameters but here we have two x_parameters and y_parameters so lets name them as flash_x_parameter, flash_y_parameter, arrow_x_parameter , arrow_y_parameter.
Then we have to fit our data to two different  linear regression models first for flash and other for arrow.
Then we have to predict the number of viewers for next episode for both of the Tv shows.
Then we can compare the results and we can guess which Tv Shows will have more viewers.

num1=11
class Calculator:
    num2=22     #Class Variable
    def funcA(self):
        self.x = 5   #Instance variable
        y= 66        #Local variable
        print("functionA is working.")

    def funcB(self):
        print("FunctionB: a=", self.x)

obj = Calculator()
print("Calculator code loaded successfully.")
obj.funcA()

Calculator.funcA(obj)

obj.funcB()
print( "Last line : x=", obj.x)



'''








import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

datas = pd.read_csv('LR_Episodes.csv')
print(datas)

print(datas.shape)    #(9,4)

X1 = datas.iloc[:, 0:1].values
Y1 = datas.iloc[ : , 1].values    # [ rows , cols ]

print("X1= \n", X1)
print("y1= \n", Y1)
print("\n\n")



X2 = datas.iloc[ : , 2:3].values    # [ rows , cols ]
Y2 = datas.iloc[: , 3].values

print("X2= \n",X2)
print("Y2= \n",Y2)
print("\n\n")


print("\nX1.shape = ", X2.shape , "\n X2=\n" , X1)
print("\ny1.shape = ", Y2.shape , "\n Y2=" , Y1 )





from sklearn.linear_model import LinearRegression

lin1 = LinearRegression()
lin1.fit(X1, Y1)

plt.scatter(X1, Y1, color='blue')
y1_pred = lin1.predict(X1)
plt.plot(X1, y1_pred, color='red')
plt.title('Flash Viewers')
plt.show()

# Predicting a new result with Linear Regression
print( "1.Expected Flash Viewers: ", lin1.predict([[10.0]])  )






lin2 = LinearRegression()
lin2.fit(X2, Y2)

plt.scatter(X2, Y2, color='blue')

y2_pred = lin2.predict(X2)
plt.plot(X2, y2_pred, color='red')
plt.title('GoT Viewers')
plt.show()

# Predicting a new result with Linear Regression
print( "2.Expected GoT Viewers: ", lin2.predict([[10.0]])  )







from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
X1_poly = poly.fit_transform(X1)

lin3 = LinearRegression()
lin3.fit(X1_poly, Y1)


plt.scatter(X1, Y1, color='blue')
y_pred = lin3.predict(X1_poly)
plt.plot(X1, y_pred, color='red')
plt.title('Flash')
plt.xlabel('Episode No')
plt.ylabel('Viewers')

plt.show()

# Predicting a new result with Linear Regression
print( "3.Expected Flash Viewers: ", lin3.predict( poly.transform( [[10.0]]) )  )




'''


from sklearn.preprocessing import PolynomialFeatures

print("Before ", X1)
poly = PolynomialFeatures(degree=4)
X1_poly = poly.fit_transform(X1)


lin3 = LinearRegression()
lin3.fit(X1_poly, Y1)

plt.scatter(X1, Y1, color='blue')
y1_pred = lin3.predict(X1_poly )
plt.plot(X1, y1_pred, color='red')
plt.title('Flash Viewers')
plt.show()

# Predicting a new result with Linear Regression
print( "3.Expected Flash Viewers: ", lin3.predict( [[10.0]] )  )









'''




















'''



# Required Packages
import pandas as pd
from sklearn.linear_model import LinearRegression

# Function to get data
def collect_data(file_name):
    data = pd.read_csv(file_name)
    flash_x_parameter = []
    flash_y_parameter = []
    got_x_parameter = []
    got_y_parameter = []
    for x1, y1, x2, y2 in zip(data['Flash_episode_number'],
                              data['Flash_us_viewers'],
                              data['GoT_episode_number'],
                              data['GoT_us_viewers'] ) :

        flash_x_parameter.append([ float(x1) ])
        flash_y_parameter.append(float(y1))
        got_x_parameter.append([ float(x2) ])
        got_y_parameter.append(float(y2))
    return flash_x_parameter, flash_y_parameter,\
           got_x_parameter, got_y_parameter

# Function to know which Tv series will have more viewers
def applyMLAlgorithm(x1, y1, x2, y2):
    regr1 = LinearRegression()
    regr1.fit(x1, y1)  #Train the machine
    predicted_value1 = regr1.predict(  [ [10] ]  )
    print( "Prediction of Flash : " , predicted_value1 )
    regr2 = LinearRegression()
    regr2.fit(x2, y2)
    predicted_value2 = regr2.predict([[10]])
    print( "Prediction of GOT : " , predicted_value2 )

    if (predicted_value1 > predicted_value2) :
        print( "Next episode of Flash Tv Show will have"
                          " more viewers for next week")
    else:
        print( "Next episode of Game of Thrones Tv Show"
                 " will have more viewers for next week")



if __name__ == "__main__":
    x1, y1, x2, y2 = collect_data('LR_Episodes.csv')
    # Call the function more_viewers to predict the more viewers television show
    applyMLAlgorithm(x1, y1, x2, y2)



'''

