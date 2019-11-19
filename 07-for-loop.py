# in this tutorial, you will learn how to use for loop statement in python

import numpy as np 


# Aim: We want to print "Hello" 10 times:

# np.arange creates a sequence from 0-9.
# in each loop i is given a number in the sequence (in order)
# the ":" is the beginning of the loop"
# The moment you press enter after the ":", a tab space (indent) is created for you in Spyder (and most python IDEs)
#  All statments with an indent are considered to be a part of that loop.
# One should be careful no to create/delete extra spaces in the beginning of such statements. This will lead to problems.
# To come out of the loop, at the end of the last statement of the loop, press shift + tab

for i in np.arange(0,10): 
    print("{0} Hello".format(i))
print("loop over")

# Assignment
# write a python code using loops to print out series like: 
# 1,1
# 1,2
# 1,4
# 1,5
# 2,1
# 2,2
# 2,3
# 2,4
# 2,5
# Hint: You will require a loop inside a loop. The second for loop statement must be singe indented and the content of the second for loop must be double indented.
# In case, you could not do it, the answer is given below.
# 
# 
# 
# 
#  
#
# 
# for i in np.arange(1,3): 
#     for j in np.arange(1,6):
#             print("{0},{1}".format(i,j))
# print("loop over")


