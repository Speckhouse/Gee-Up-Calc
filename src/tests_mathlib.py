#!/usr/bin/env python

##
# @file tests_mathlib.py
# PyUnit test for mathlib.py library
#
# @author Igor Ignác xignac00@stud.fit.vutbr.cz

from mathlib import add, subtract, multiply, divide, factorial, power, root, logn

import math
import unittest

## Class for constructor
#
# Constructor with data for tests
class SimpleConstructorTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 50
        self.b = 20
        self.c = -30
        self.d = -10
        self.e = 0.52
        self.f = 12.487
        self.g = 0

## Class for add function
#
# Checks for correct functionality of Add function with multiple input data
class AddFunctionTestCase(SimpleConstructorTestCase):

    ## The constructor
    def runTest(self):
        self.assertEqual(self.a + self.b, add(self.a, self.b))
        self.assertEqual(self.c + self.d, add(self.c, self.d))
        self.assertEqual(self.e + self.f, add(self.e, self.f))

## Class for substract function
#
# Checks for correct functionality of Substract function with multiple input data
class SubtractFunctionTestCase(SimpleConstructorTestCase):

    ## The constructor
    def runTest(self):
        self.assertEqual(self.a - self.b, subtract(self.a, self.b))
        self.assertEqual(self.c - self.d, subtract(self.c, self.d))
        self.assertEqual(self.e - self.f, subtract(self.e, self.f))

## Class for multiply function
#
# Checks for correct functionality of Multiply function with multiple input data
class MultiplyFunctionTestCase(SimpleConstructorTestCase):

    # The constructor
    def runTest(self):
        self.assertEqual(self.a * self.b, multiply(self.a, self.b))
        self.assertEqual(self.c * self.d, multiply(self.c, self.d))
        self.assertEqual(self.e * self.f, multiply(self.e, self.f))

## Class for divide function
#
# Checks for correct functionality of Divide function
class DivideFunctionTestCase(SimpleConstructorTestCase):

    ## The constructor
    def runTest(self):
        self.assertEqual(self.a / self.b, divide(self.a, self.b))
        self.assertEqual(self.c / self.d, divide(self.c, self.d))
        self.assertEqual(self.e / self.f, divide(self.e, self.f))
        self.assertEqual(self.g / self.g, divide(self.g, self.g))

    ## The constructor, raise of an error expected
    def runTest(self):
        self.assertRaises(ZeroDivisionError, divide, self.a, self.g)
        self.assertRaises(ZeroDivisionError, divide, self.e, self.g)

## Class for factorial function
#
# Checks for correct functionality of Factorial function
class FactorialFunctionTestCase(SimpleConstructorTestCase):

    ## The constructor
    def runTest(self):
        self.assertEqual(math.factorial(self.a),factorial(self.a))
        self.assertEqual(factorial(self.g), 1)

    ## The constructor, raise of an error expected
    def runTest(self):
        self.assertRaises(ValueError, factorial, self.c)
        self.assertRaises(ValueError, factorial, self.e)

## Class for power function
#
# Checks for correct functionality of Power function
class PowerFunctionTestCase(SimpleConstructorTestCase):

    # The constructor
    def runTest(self):
        self.assertEqual((power(self.a, self.b)), float((pow(self.a, self.b))))
        self.assertEqual((power(self.b, self.a)), float((pow(self.b, self.a))))
        self.assertEqual((power(self.c, self.a)), float((pow(self.c, self.a))))
        self.assertEqual(power(self.g, self.a), 0)

    ## The constructor, raise of an error expected
    def runTest(self):
        self.assertRaises(ValueError, power, self.a, self.f)
        self.assertRaises(ValueError, power, self.c, self.f)
        self.assertRaises(ValueError, power, self.a, self.c)
        self.assertRaises(ValueError, power, self.a, self.g)

## Class for root function
#
# Checks for correct functionality of Root function
class RootFunctionTestCase(SimpleConstructorTestCase):

    # The constructor
    def runTest(self):
        self.assertEqual(pow(self.a, (1. / self.b)), root(self.a, self.b))
        self.assertEqual(pow(self.a, (1. / self.c)), root(self.a, self.c))
        self.assertEqual(pow(self.f, (1. / self.a)), root(self.f, self.a))
        self.assertEqual(pow(self.a, (1. /self.f)), root(self.a, self.f))

    ## The constructor, raise of an error expected
    def runTest(self):
        self.assertRaises(ZeroDivisionError, root, self.a, self.g)
        self.assertRaises(ValueError, root, self.c, self.a)

## Class for logn function
#
# Checks for correct functionality of Logn function
class LognFunctionTestCase(SimpleConstructorTestCase):

    # The constructor
    def runTest(self):
        self.assertEqual(math.log1p(self.a - 1), logn(self.a))
        self.assertEqual(math.log1p(self.f - 1), logn(self.f))
        self.assertEqual(math.log1p(self.e - 1), logn(self.e))

    ## The constructor, raise of an error expected
    def runTest(self):
        self.assertRaises(ValueError, logn, self.d - 1)
        self.assertRaises(ValueError, logn, self.g - 1)

## Main
#
# Run all tests simultaneously
if __name__ == "__main__":
     unittest.main()

## End of file
