import sys
import PyQt5
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QGridLayout, QSizePolicy)
from functools import partial
from KeyEnum import KeyEnum

class Numpad(QWidget):
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
        
        for y in range(1,4):
            for x in range(1,4):
                num = (3-y)*3 + x
                button = QPushButton(str(num))
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.clicked.connect(partial(self.EventHandlerForward,num))
                grid.addWidget(button,y,x)
        button = QPushButton('0')
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(partial(self.EventHandlerForward,0))
        grid.addWidget(button,4,1,1,2)
        button = QPushButton('.')
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(partial(self.EventHandlerForward,KeyEnum.DOT.value))
        grid.addWidget(button,4,3)

        self.setLayout(grid)

    ## @brief Function that forwards OnClick events of buttons to Numpad.eventhandler 
    # @param self Object pointer
    # @param n button pressed, refer to KeyEnum enumerator for values
    def EventHandlerForward(self,n):
        self.eventhandler(n)


