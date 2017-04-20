import sys
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QGridLayout, QSizePolicy, QLineEdit, QMessageBox)
from PyQt5.QtGui import QIcon
from functools import partial
from KeyEnum import KeyEnum
from Numpad import Numpad
from Mathpad import Mathpad
from CalcLogic import CalcLogic

class Calculator(QWidget):
    ## @var eventhandler
    # @brief pointer at function used to handle onclickevents of buttons
    eventhandler = None
    ## @var npad
    # @the Numpad widget
    npad = None
    ## @var mpad
    # @brief Mathpad widget
    mpad = None
    ## @var lineedit
    # @brief QLineEdit widget
    lineedit = None
    ## @var helplabel
    # @brief help title
    helptitle = "Nápoveda"
    ## @var helptext
    # @brief help message
    helptext = """Táto kalkulačka poskytuje binárne a unárne operácie.

Binárne operácie: +, -, *, /, prirodzená mocnina a všeobecná odmocnina.
Zadajte číslo, stlačte tlačidlo operácie, zadajte druhé číslo a stlačte tlačidlo =.

Unárne operácie: Faktoriál a prirodzený logaritmus.
Zadajte číslo a stlačte tlačidlo operácie."""
    
    ## @brief the constructor
    # @param self Object pointer
    # @param func Pointer at function which handles Onclick Events of buttons
    # @param offsetx X Offset within the parent
    # @param offsety Y Offset within the parent
    # @param width Width of the widget
    # @param height Height of the widget
    # @param parnt Parent of the widget
    def __init__(self, func, offsetx=None, offsety=None, width=None, height=None, parent = None):
        super().__init__(parent)

        self.eventhandler = func

        if offsetx != None and offsety != None and width != None and height != None:
            self.setGeometry(offsetx, offsety, width, height)

        grid = QGridLayout()

        self.lineedit = QLineEdit()
        self.lineedit.setReadOnly(True)
        self.lineedit.setMinimumSize(50,20)
        self.lineedit.setAlignment(Qt.AlignRight)
        self.lineedit.setStyleSheet("border: 1px solid gray; width: 25px; height:25px;");
        self.lineedit.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        grid.addWidget(self.lineedit,1,1,2,6)

        self.npad = Numpad(self.EventHandlerForward)
        self.npad.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        grid.addWidget(self.npad,4,1,4,3)
        
        self.mpad = Mathpad(self.EventHandlerForward)
        self.mpad.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        grid.addWidget(self.mpad,4,5,4,2)
        
        button = QPushButton(self.helptitle)
        button.clicked.connect(self.HelpHandler)
        grid.addWidget(button,8,1)

        self.setLayout(grid)
    
    ## @brief Function that handles OnClick events of Help Button
    # @param self Object pointer
    def HelpHandler(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(self.helptext)
        msg.setWindowTitle(self.helptitle)
        retval = msg.exec_()

    ## @brief Function that forwards OnClick events of buttons to Kalkulacka.eventhandler 
    # @param self Object pointer
    # @param n button pressed, refer to KeyEnum enumerator for values
    def EventHandlerForward(self,n):
        self.eventhandler(self,n)

    ## @brief Function that handles OnClick events of buttons
    # @param self Object pointer
    # @param n button pressed, refer to KeyEnum enumerator for values
    def setText(self,text):
        self.lineedit.setText(text)

logic = CalcLogic()

def f(kalkulacka,i):
    kalkulacka.setText(logic.getkey(i))

app = QApplication(sys.argv)

w = Calculator(f)
w.setWindowTitle('Gee Up Calc')
w.setWindowIcon(QIcon('geeupcalc_icon.png'))
w.show()

sys.exit(app.exec_())
