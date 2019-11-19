# In many physics studies, you will need random numbers to be generated from a gaussian (normal) or uniform distribution
# this tutorial shows you how to do it using numpy
# for this you need to install numpy module (in case you have not installed it)
# to know how to install it using anaconda navigator, go to https://github.com/deepaksamuel/python-tutorials and see the README.md

# In c/c++, we use the #include statement. In python we use import statement to include modules
# the numpy module contains important mathematical functions that you will learn soon.
# First step, as always is to import numpy as np (np will now be a shortcut for numpy)

import numpy as np


# generate a series of 1000 random numbers from a gaussian distribution with mean 0, sigma 1 
ran = np.random.normal(0,1,1000) #(mean, sigma, number of samples)
print(ran)

# generate a series of 1000 random numbers from a uniform number between 0 and 1 
ran = np.random.uniform(0,1,1000) #(low, high, number of samples)
print(ran)

# assignment: generate a series of random numbers from an exponential distribution
# You can refer to https://docs.scipy.org/doc/numpy-1.14.1/reference/routines.random.html