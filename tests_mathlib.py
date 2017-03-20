#!/usr/bin/env python

from mathlib import add, subtract, multiply, divide, factorial, power, root, logn

import math
import unittest

class SimpleConstructorTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 50
        self.b = 20
        self.c = -30
        self.d = -10
        self.e = 0.52
        self.f = 12.487
        self.g = 0

"""Checks for correct functionality of Add function"""
class AddFunctionTestCase(SimpleConstructorTestCase):
    def runTest(self):
        self.assertEqual(self.a + self.b, add(self.a, self.b))
        self.assertEqual(self.c + self.d, add(self.c, self.d))
        self.assertEqual(self.e + self.f, add(self.e, self.f))

"""Checks for correct functionality of Substract function"""
class SubtractFunctionTestCase(SimpleConstructorTestCase):
    def runTest(self):
        self.assertEqual(self.a - self.b, subtract(self.a, self.b))
        self.assertEqual(self.c - self.d, subtract(self.c, self.d))
        self.assertEqual(self.e - self.f, subtract(self.e, self.f))

"""Checks for correct functionality of Multiply function"""
class MultiplyFunctionTestCase(SimpleConstructorTestCase):
    def runTest(self):
        self.assertEqual(self.a * self.b, multiply(self.a, self.b))
        self.assertEqual(self.c * self.d, multiply(self.c, self.d))
        self.assertEqual(self.e * self.f, multiply(self.e, self.f))

"""Checks for correct functionality of Divide function"""
class DivideFunctionTestCase(SimpleConstructorTestCase):
    def runTest(self):
        self.assertEqual(self.a / self.b, divide(self.a, self.b))
        self.assertEqual(self.c / self.d, divide(self.c, self.d))
        self.assertEqual(self.e / self.f, divide(self.e, self.f))

        self.assertEqual(self.g / self.g, divide(self.g, self.g))
    def runTest(self):
        self.assertRaises(ZeroDivisionError, divide, self.a, self.g)
        self.assertRaises(ZeroDivisionError, divide, self.e, self.g)

"""Checks for correct functionality of Factorial function"""
class FactorialFunctionTestCase(SimpleConstructorTestCase):

    def runTest(self):
        self.assertEqual(math.factorial(self.a),factorial(self.a))
        self.assertEqual(factorial(self.g), 1)
    def runTest(self):
        self.assertRaises(ValueError, factorial, self.c)
        self.assertRaises(ValueError, factorial, self.e)

"""Checks for correct functionality of Power function"""
class PowerFunctionTestCase(SimpleConstructorTestCase):
    def runTest(self):

        self.assertEqual(round((power(self.a, self.b)), 20), round((pow(self.a, self.b)), 20))
        self.assertEqual(round((power(self.b, self.a)), 20), round((pow(self.b, self.a)), 20))
        self.assertEqual(round((power(self.c, self.a)), 20), round((pow(self.c, self.a)), 20))
        self.assertEqual(power(self.g, self.a), 0)

        self.assertRaises(ValueError, power, self.a, self.f)
        self.assertRaises(ValueError, power, self.c, self.f)
        self.assertRaises(ValueError, power, self.a, self.c)
        self.assertRaises(ValueError, power, self.a, self.g)

"""Checks for correct functionality of Root function"""
class RootFunctionTestCase(SimpleConstructorTestCase):
    def runTest(self):
        self.assertEqual(pow(self.a, (1. / self.b)), root(self.a, self.b))
        self.assertEqual(pow(self.a, (1. / self.c)), root(self.a, self.c))
        self.assertEqual(pow(self.f, (1. / self.a)), root(self.f, self.a))
        self.assertEqual(pow(self.a, (1. /self.f)), root(self.a, self.f))

        self.assertRaises(ZeroDivisionError, root, self.a, self.g)
        self.assertRaises(ValueError, root, self.c, self.a)

"""Checks for correct functionality of Logn function"""
class LognFunctionTestCase(SimpleConstructorTestCase):
    def runTest(self):
        self.assertEqual(math.log1p(self.a - 1), logn(self.a))
        self.assertEqual(math.log1p(self.f - 1), logn(self.f))
        self.assertEqual(math.log1p(self.e - 1), logn(self.e))

        self.assertRaises(ValueError, logn, self.d - 1)
        self.assertRaises(ValueError, logn, self.g - 1)

"""Run all tests"""
if __name__ == "__main__":
     unittest.main()
