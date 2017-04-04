#!/usr/bin/python3

##
# @file mathlib.py
# Library for mathematical calculations
#
# @author Simeon Borko xborko02@stud.fit.vutbr.cz

import math

##
# @brief Compute sum.
# @param a Float number.
# @param b Float number.
# @return a + b
def add(a, b):
    return a + b

##
# @brief Compute difference.
# @param a Float number.
# @param b Float number.
# @return a - b
def subtract(a, b):
    return a - b

##
# @brief Compute product.
# @param a Float number.
# @param b Float number.
# @return a * b
def multiply(a, b):
    return a * b

##
# @brief Compute quotient.
# @param a Float number.
# @param b Float number.
# @return a / b
# @exception ZeroDivisionError if 'b' is 0.
def divide(a, b):
    return a / b

##
# @brief Compute factorial.
# @param a Natural number > 0.
# @return a!
# @exception ValueError if 'a' is not natural number greater than 0.
def factorial(a):
    return float(math.factorial(a))

##
# @brief Compute natural power.
# @param a Float number.
# @param b
# @return a^b
# @exception ValueError if 'b' is not natural number greater than 0.
def power(a, b):
    if not float(b).is_integer() or b < 1:
      raise ValueError('power(a, b) b have to be natural number')
    return float(pow(a, b))

##
# @brief  Get bth root from a.
# @param a Base - float number.
# @param b Which root - float number.
# @return bth root from a.
# @exception ZeroDivisionError if 'b' is 0.
# @exception ValueError if root is not real (is complex).
def root(a, b):
    res = pow(a, 1. / b)
    if isinstance(res, complex):
        raise ValueError('root() root is not real (is complex)')
    return res

##
# @brief Compute natural logarithm
# @param a Float number > 0.
# @return log(e)(a)
# @exception ValueError if 'a' is less than 0.
def logn(a):
    return math.log1p(a - 1)

## End of file
