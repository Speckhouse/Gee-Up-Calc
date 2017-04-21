##
# @file KeyOperations.py
# @brief Module mapping buttons to their respective operations
#

from KeyEnum import KeyEnum
import mathlib

# dictionary for unary functions
_unary = {
    KeyEnum.EQUALS: None,
    KeyEnum.FACTORIAL: mathlib.factorial,
    KeyEnum.LOGN: mathlib.logn,
}

# dictionary for binary functions
_binary = {
    KeyEnum.PLUS: mathlib.add,
    KeyEnum.MINUS: mathlib.subtract,
    KeyEnum.MULTIPLICATION: mathlib.multiply,
    KeyEnum.DIVISION: mathlib.divide,
    KeyEnum.POWER: mathlib.power,
    KeyEnum.ROOT: mathlib.root,
}

##
# @brief Searches for function corresponding to `key'
# @param key button ID
# @return function reference or None
#
def getfn(key):
    op = KeyEnum(key)
    if op in _unary:
        return _unary[op]
    if op in _binary:
        return _binary[op]
    return None

##
# @brief Test if key represents unary function
# @param key button ID
# @return boolean
#
def unary(key):
    return KeyEnum(key) in _unary

##
# @brief Test if key represents binary function
# @param key button ID
# @return boolean
#
def binary(key):
    return KeyEnum(key) in _binary

# End of file: KeyOperations.py
