import sys
import PyQt5
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QGridLayout, QSizePolicy)
from functools import partial
from KeyEnum import KeyEnum

class Mathpad(QWidget):

    ## @var eventhandler
    # @brief pointer at function used to handle onclickevents of buttons
    eventhandler = None

    ## @brief the constructor
    # @param self Object pointer
    # @param func Pointer at function which handles Onclick Events of buttons
    # @param offsetx X Offset within the parent
    # @param offsety Y Offset within the parent
    # @param width Width of the widget
    # @param height Height of the widget
    # @param parnt Parent of the widget
    def __init__(self, func, offsetx=None, offsety=None, width=None, height=None, parent = None):
        super().__init__(parent);

        self.eventhandler = func

        if offsetx != None and offsety != None and width != None and height != None:
            self.setGeometry(offsetx, offsety, width, height)

        grid = QGridLayout()
        
        button = QPushButton('+')
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(partial(self.EventHandlerForward,KeyEnum.PLUS.value))
        grid.addWidget(button,1,1)
        button = QPushButton('-')
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(partial(self.EventHandlerForward,KeyEnum.MINUS.value))
        grid.addWidget(button,1,2)

        button = QPushButton('*')
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(partial(self.EventHandlerForward,KeyEnum.MULTIPLICATION.value))
        grid.addWidget(button,2,1)
        button = QPushButton('/')
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(partial(self.EventHandlerForward,KeyEnum.DIVISION.value))
        grid.addWidget(button,2,2)

        button = QPushButton('=')
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(partial(self.EventHandlerForward,KeyEnum.EQUALS.value))
        grid.addWidget(button,3,1,1,2)
        
        self.setLayout(grid)

    ## @brief Function that forwards OnClick events of buttons to Mathpad.eventhandler 
    # @param self Object pointer
    # @param n button pressed, refer to KeyEnum enumerator for values
    def EventHandlerForward(self,n):
        self.eventhandler(n)


