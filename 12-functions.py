# In this tutorial, you will learn how to write functions in python 
# Lets write a function that will return the square, square root and the cube of the number that is passed to it

import numpy as np 


# This is how a function is defined:
def my_func(val): # the colon works the same way it did in for loops, the indenting begins after that (Do not delete the indenting)
    sq = val*val
    sqrt = np.sqrt(val)
    cube = val*val*val
    return sq,sqrt,cube

# you press shift+tab to come out of the indent (or loop)

v =100
print(my_func(100))

# or you can also do:
val1, val2, val3 = my_func(v) # in this case, val1 contains sq, val2 contains sqrt and val3 contains cube

print("value of val1 is {0}".format(val1))
print("value of val2 is {0}".format(val2))
print("value of val3 is {0}".format(val3))
