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
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)
        # self.connect(dial,    SIGNAL("valueChanged(int)"),  spinbox.setValue)
        # self.connect(spinbox, SIGNAL("valueChanged(int)"),  dial.setValue)
        self.connect(dial,    SIGNAL("valueChanged(int)"),  spinbox, SLOT("setValue(int)"))
        self.connect(spinbox, SIGNAL("valueChanged(int)"),  dial,    SLOT("setValue(int)"))
        self.setWindowTitle("Signals and Slots")

# Create QApplication
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
