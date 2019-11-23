# In this tutorial we will see how to fit curves to give set of data points
# In the first part, we will see how to make a linear fit

import numpy as np
import matplotlib.pyplot as plt

# lets create an artificial data set of x and y points to which we will fit a straight line
# We will make x=y in which case the slope =1 and intercept will be 0


x = np.arange(0,10,1)
# you can also add some variations to y to simulate an experimental datapoint.
# one way is to add gaussian noise by sampling a number from a gaussian distribution and adding it to y.
# like this:
noise = np.random.normal(0,1,10)# check tutorials 04 to learn about random number generatio 
y =  x+noise # in case noise is zero, y = x will be a straight line with slope exactly equal to 1 and intercept exaclty 0

plt.scatter(x,y)


fit_res = np.polyfit(x, y, 1) # 1 is the degree of fit, 1 is for linear fit, 2 for quadratic plot and so on

# z contains the results of the fit
# This is how you get the slope and intercept

print("The fit results are:{0}".format(fit_res)) # the first element in the array is the slope and the second element is the intercept
print("The first value is the slope and the second is the intercept")
#Now lets plot the line as estimated by the linear fit:
y_fit = fit_res[0]*x + fit_res[1] # y=mx + c
# enable the line below to see the fitted line
plt.plot(x,y_fit)

plt.show()





# assignments
# # in many cases, one might require the error on the slope and intercept
# in which case one can do the following:

# fit_res, error= np.polyfit(x, y, 1,full=False, cov=True) # 1 is the degree of fit, 1 is for linear fit, 2 for quadratic plot and so on
# print("The error matrix is {0}".format(error))
# print("The diagonal elements are the errors") # The first element in the diagonal is that of slope and the second element in the diagonal is that of the intercept 
# Try the above code

# In case you want to fit a second order polynomial  change np.polyfit(x,y,1) to np.polyfit(x,y,2)

# Change the mean and sigma in the gaussian distribution and see how the error matrix changes.