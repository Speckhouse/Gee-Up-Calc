from KeyEnum import KeyEnum

_unary = {
    KeyEnum.EQUALS: None,
}

_binary = {
    KeyEnum.PLUS: None,
    KeyEnum.MINUS: None,
    KeyEnum.MULTIPLICATION: None,
    KeyEnum.DIVISION: None,
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
