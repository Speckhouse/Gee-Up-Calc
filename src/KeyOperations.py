from KeyEnum import KeyEnum
import mathlib

_unary = {
    KeyEnum.EQUALS: None,
    KeyEnum.FACTORIAL: mathlib.factorial,
    KeyEnum.LOGN: mathlib.logn,
}

_binary = {
    KeyEnum.PLUS: mathlib.add,
    KeyEnum.MINUS: mathlib.subtract,
    KeyEnum.MULTIPLICATION: mathlib.multiply,
    KeyEnum.DIVISION: mathlib.divide,
    KeyEnum.POWER: mathlib.power,
    KeyEnum.ROOT: mathlib.root,
}

def getfn(key):
    op = KeyEnum(key)
    if op in _unary:
        return _unary[op]
    if op in _binary:
        return _binary[op]
    return None

def unary(key):
    return KeyEnum(key) in _unary

def binary(key):
    return KeyEnum(key) in _binary
