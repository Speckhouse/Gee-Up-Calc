##
# @file CalcLogic.py
# @author Václav Doležal xdolez76@stud.fit.vutbr.cz
# @brief Module defining behavior of calculator
#

from PyQt5.QtWidgets import QWidget
from KeyEnum import KeyEnum
import KeyOperations

##
# @class CalcLogic
# @brief State and behavior of calculator
#
class CalcLogic(object):
    ##
    number1 = 0
    ##
    string = ""
    ##
    pending_op = None

    ##
    # @brief Evaluates pending binary operation
    #
    # Takes `self.number1' as first parameter and `self.string' as second
    # parameter to function `self.pending_op'.
    #
    # If operation is None, converts `self.string' to float.
    #
    # @post
    #   - result is saved to `self.number1'
    #   - `self.string' is cleared
    #
    def evaluate(self):
        if self.string:
            if self.pending_op:
                self.number1 = self.pending_op(self.number1, float(self.string))
            else:
                self.number1 = float(self.string)
            self.string = ""

    ##
    # @brief Evaluates unary operation
    #
    # @param op function representing unary operation
    # @post
    #   - result is saved to `self.number1'
    #   - `self.string' is cleared
    #
    def evaluate_unary(self, op):
        if op:
            self.number1 = op(self.number1)
        self.string = ""

    ##
    # @brief Evaluates pending binary operation
    #
    # Takes `self.number1' as first parameter and `self.string' as second
    # parameter to function `self.pending_op'
    #
    # @param key button ID
    # @return string representing result, error message or input string
    # @post
    #   - on error resets state
    #
    def getkey(self, key):
        try:
            # numerals
            if key < 10:
                self.string = self.string + str(key)
                return self.string
            elif KeyEnum(key) == KeyEnum.DOT:
                if not self.string:
                    self.string = '0.'
                # ignore any extra dots
                elif not '.' in self.string:
                    self.string = self.string + '.'
                return self.string
            elif KeyOperations.binary(key):
                self.evaluate()
                self.pending_op = KeyOperations.getfn(key)
                return str(self.number1)
            # on unary ops, evaluate any pending binary operation, then
            # perform unary operation on result
            elif KeyOperations.unary(key):
                self.evaluate()
                self.evaluate_unary(KeyOperations.getfn(key))
                self.pending_op = None
                return str(self.number1)
        except Exception as e:
            self.pending_op = None
            self.string = ""
            self.number1 = 0
            return 'Error: ' + str(e)

# End of file: CalcLogic.py
