# -*- coding: utf-8 -*-
"""bisection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17IXNJ9Rii6Knl1AUSls8x8Ac2Q2k_ltp
"""

# The bisection method is an approximation method to find the roots of the given
# function by repeatedly dividing the interval.
# The module contains the function bisection
# The function 'bisection' takes the initial value x_L ,final value x_R of interval
# and tolerance error 'eps'
# The function 'bisection' repeatedly calculate the middle point 'x_M' of interval
# The following function calculates the approximate root of function 'f'.
import numpy as np
import matplotlib.pyplot as plt


# Define bisection method
def bisection(f, x_L, x_R, eps):
    f_L = f(x_L)  # value of the function at x = x_L
    x_M = (x_L + x_R) / 2.0  # find middle point
    f_M = f(x_M)  # value of the function at midpoint
    f_R = f(x_R)  # value of the function at x = x_R
    c = 0
    s = np.array([0])
    y = open("bisection.txt", 'w')   
    while abs(x_R - x_L) > eps and c < 5000:
        # Decide the side to repeat the steps
        k = x_M
        if f_L * f_M > 0:  # i.e. same sign
            x_L = x_M
            f_L = f_M
        else:
            x_R = x_M
        x_M = (x_L + x_R) / 2
        f_M = f(x_M)
        print('{:15d}{:14.5f}{:14.5f} {:14.5f} {:15.5f}'.format(c, k, x_M, f(k), f(x_M)), file =y)
        s = np.append(s, x_M)
        c = c + 1
    s = np.delete(s, 0)
    l = np.linspace(0, c, c)
     
    plt.plot(l, s, 'r*')
    plt.xlabel('l(number of iteration)')  # Iteration iin x-axis
    plt.ylabel('x(Approximated root)')  # Approximation is taking at y-axis
    plt.grid('on')
    plt.show()  # Plotting the graph of approximation vs iteration
    
    return x_M, c
    y.close()



