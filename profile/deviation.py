#!/usr/bin/python3

##
# @file deviation.py
# Compute Standard deviation
#
# @author Simeon Borko xborko02@stud.fit.vutbr.cz

import sys
sys.path.append('../')
import mathlib

average = 0   ## arithmetic average
total = 0     ## sum of squares of items
number = 0    ## number of items

for item in sys.stdin:
  x = int(item)
  average = mathlib.add(average, x)
  total = mathlib.add(total, mathlib.power(x, 2))
  number = mathlib.add(number, 1)
  
average = mathlib.divide(average, number)

fraction = mathlib.subtract(number, 1)
fraction = mathlib.divide(1, fraction)

difference = mathlib.power(average, 2)
difference = mathlib.multiply(number, difference)
difference = mathlib.subtract(total, difference)

product = mathlib.multiply(fraction, difference)
result = mathlib.root(product, 2)

print(result)

## End of file
