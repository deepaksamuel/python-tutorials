# Often you will have to include variables while printing
# This example will show you how to do it.

#number of apples
napp =11
#price of one apple
pp = 15

#the {} is a place holder for the value. In place of {0}, the first argument of format is inserted and in place of {1}, the second argument of format is inserted and so on...
print("The price of {0} apples is {1}".format(napp,napp*pp))

#Look what happens if the indexes are reversed....
print("{1} apples cost {0}".format(napp,napp*pp))