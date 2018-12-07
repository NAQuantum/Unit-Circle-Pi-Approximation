from random import *
import numpy as np
import matplotlib.pyplot as plt
def pair():
    return (random(),random())
def dart():
    (a,b)=pair()
    return (a**2+b**2)<=1.0

# Iterations
# CHANGE THIS to determine the accuracy of the approximation
I = 5

def create(newdarts): # Generates newdarts more darts and returns how many fall inside the circle
    i=newdarts
    c=0
    while i>0:
        if dart():
            c+=1
        i-=1
    return c

def approx(circledarts,totaldarts): # Gives final approximation of pi
    return 4*circledarts/totaldarts

def error(circledarts, totaldarts):
    return abs(approx(circledarts,totaldarts)-np.pi) # Objective error of approximation

# Generation of approximations
c = create(1)
errors = []
i=1
while i<=I:
    c+=create(10**i-10**(i-1))
    errors+=[error(c,10**i)]
    i+=1
    
# Generation of graph, don't touch this vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

# Getting the x-values list going
mylistylist = []
for i in range(1,I+1):
    mylistylist += [10**i]
    
# Actual graphing
plt.xscale('log')
plt.yscale('log')
plt.plot(mylistylist, errors, 'o')
plt.xlabel("Darts")
plt.ylabel("Error in Approximation")
