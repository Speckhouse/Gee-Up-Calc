from PyQt5.QtWidgets import QWidget
from KeyEnum import KeyEnum
import KeyOperations

class CalcLogic(object):
    number1 = 0
    string = ""
    pending_op = None

    def evaluate(self):
        if self.string:
            if self.pending_op:
                self.number1 = self.pending_op(self.number1, float(self.string))
            else:
                self.number1 = float(self.string)
            self.string = ""
        else:
            if self.pending_op:
                self.number1 = self.pending_op(self.number1, self.number1)


    def getkey(self, key):
        if key < 10:
            self.string = self.string + str(key)
            return self.string
        elif KeyEnum(key) == KeyEnum.DOT:
            self.string = self.string + '.'
            return self.string
        elif KeyOperations.binary(key):
            self.evaluate()
            self.pending_op = KeyOperations.getfn(key)
            return str(self.number1)
        elif KeyOperations.unary(key):
            self.evaluate()
            self.pending_op = KeyOperations.getfn(key)
            self.evaluate()
            self.pending_op = None
            return str(self.number1)
