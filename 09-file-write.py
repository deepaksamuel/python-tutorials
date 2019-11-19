# file writing in python

import numpy as np 

# we will write numbers from 0-99 and the square of these numbers in a file (separated by a comma)

# opening a file is done by:
f = open("out.txt", "w") # w will write to a file and a will append to the file

for i in np.arange(0,100):
    f.write("{0},{1}\n".format(i,i**2))# i**2 means square of i, \n tells to write whatever follows, in the next line.

f.close() # do not put this inside the loop, the file will be closed in the first loop itself!
print("File written!")

# assignment
# See what happens if the character "\n" is removed
# instead of a comma, you can use a "\t" in which case the numbers are tab separated