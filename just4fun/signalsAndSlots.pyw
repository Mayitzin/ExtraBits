# -*- coding: utf-8 -*-
"""Signals and Slots

Based on the examples of the book "Rapid GUI programming with Python and Qt" by
Mark Summerfield.

@author: Mario Garcia
www.mayitzin.com
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Widgets
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()
        zerospinbox = ZeroSpinBox()
        # Layout
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        layout.addWidget(zerospinbox)
        self.setLayout(layout)
        # Connections
        # self.connect(dial,    SIGNAL("valueChanged(int)"),  spinbox.setValue)
        # self.connect(spinbox, SIGNAL("valueChanged(int)"),  dial.setValue)
        self.connect(dial,    SIGNAL("valueChanged(int)"),  spinbox, SLOT("setValue(int)"))
        self.connect(spinbox, SIGNAL("valueChanged(int)"),  dial,    SLOT("setValue(int)"))
        self.connect(zerospinbox, SIGNAL("atzero"), self.announce)
        self.setWindowTitle("Signals and Slots")

    def announce(self, zeros):
        print "ZeroSpinBox has been at zero %d times" % zeros

class ZeroSpinBox(QSpinBox):
    zeros = 0
    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)
        self.connect(self, SIGNAL("valueChanged(int)"), self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atzero"), self.zeros)

# Create QApplication
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
