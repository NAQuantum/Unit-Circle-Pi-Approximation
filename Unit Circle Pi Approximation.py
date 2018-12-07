from random import *
import numpy as np
import matplotlib.pyplot as plt
def pair():
    return (random(),random())
def dart(x):
    (a,b)=x
    return (a**2+b**2)<=1.0

# Dart creation and counting
def add(darts,length):
    for x in range(length):
        darts += [dart()]
    return darts
def approx(darts):
    c = 0
    length = len(darts)
    for i in range(length):
        if darts[i]<=1.0:
            c+=1
    return 4*c/length
def error(darts):
    return abs(approx(darts)-np.pi)

# Iterations
I = 7

# Generation of approximations
returns = [dart()]
errors = []
for i in range(1,I+1):
    returns = add(returns,10**i-10**(i-1))
    errors += [error(returns)]
    
# Simple generation for graph
mylistylist = []
for i in range(1,I+1):
    mylistylist += [10**i]
# Graph
plt.xscale('log')
plt.yscale('log')
plt.plot(mylistylist, errors, 'o')
plt.xlabel("Darts")
plt.ylabel("Error in Approximation")

