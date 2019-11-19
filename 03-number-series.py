# you will often need in your calculation to generate a series of numbers
# from say, 0 to 100 in steps of 1 (i.e, 0,1,2,3,4,5...100)
# or 1 to 10 in steps of 0.1 (i.e, 1,1.1,1.2,1.3,1.4...10 )
# This example shows you how to do it

# for this you need to install numpy module (in case you have not installed it)
# to know how to install it using anaconda navigator, go to https://github.com/deepaksamuel/python-tutorials and see the README.md

# In c/c++, we use the #include statement. In python we use import statement to include modules
# the numpy module contains important mathematical functions that you will learn soon.
# First step is to import numpy as np (np will now be a shortcut for numpy)

import numpy as np

# in python variables have no identifiers like we have in C/C++ (int, float, double etc.) They are automatically done by the interpreter for you 
# Here ser is a variable, arange is a function in the numpy module (np is the shortcut for numpy as specified in line 13)
# The following statements will print numbers from 0-99 in steps of 1. The third argument is the step size, which if you omit, will be taken as 1.

ser = np.arange(0,100)
print(ser)

# The following statements will print numbers from 1-9 in steps of 0.1

ser = np.arange(1,10,0.1)
print(ser)

# Assignment:
# generate a series of numbers between 100 and 1000 with a step size of 100
# generate a series of numbers between 1000 and 100 with a step size of 100