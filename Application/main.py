# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 19:32:49 2025

@author: wahhab
"""

def euclidean(dividend, divisor): # Initializing the function which encapsulates and implements the Euclidean Algorithm to find the GCD
    while divisor > 0: # This while loop will continue running until the remainder is zero, adhering to the Euclidean algorithm by changing the value of the divisor to the remainder until it is equal to zero, the GCD of both positive integers will be the latest dividend
        remainder = dividend % divisor # The math operator uses the modulo symbol to get the remainder of two valid values that can either be integers or floats
        dividend = divisor # The value of the dividend will continue to be set as the value of the divisor to continue searching for the GCD
        divisor = remainder # The value of the divisor will continue to be set as the value of the remainder to continue the process of calculating the GCD
    gcd = dividend # The value of the GCD of the two integers will be the latest value of the dividend. In more detail it is that value of the dividend when the divisor is equal to zero
    return gcd # The function returns the GCD when the divisor is equal to zero, by returning a value of a local variable instead of printing it to the console, this leverages from the use of encapsulation in numerous ways as we can set a new variable to be equal to the return value of the function, in this case it is the GCD of two positive integers 

integer_01 = 67 # Initializing the first positive integer to be used in the function
integer_02 = 3 # Initializing the second positive integer to be used in the function

print(f"The GCD of {integer_01} and {integer_02} is equal to the following value: {euclidean(integer_01, integer_02)}") # By utilizing the use of an "f-string" in Python 3, it is possible to print in a convenient manner that represents different values of different variables in a print statement
        

"""
Please note the following statements related to the program:

The purpose of both integers (refer to line 1, 2), was to demonstrate how the euclidean() function can take two positive integers as arguments.
    
Alternatively, in this program it is possible to insert positive integers as arguments for the euclidean() function.

Both integers could be initialized before or after the initialization of the euclidean() function, it is crucial to ensure that they are intialized before being used as arguments for the function.

In line 12, it was feasible to substitute the return value with a variable that is equal to the return value.
"""