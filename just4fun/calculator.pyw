"""Calculator GUI
@author: Mario Garcia
www.mayitzin.com
"""

from __future__ import division
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create a Widget to display text and HTML
        self.browser = QTextBrowser()
        # Create a Widget to receive and display text (with initial text)
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        # Create a Vertical Box layout to put a widget on top of the other
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        # Layout manager gives ownership of widgets and itself to the form
        self.setLayout(layout)
        # The foucs starts in the QLineEdit
        self.lineedit.setFocus()
        # When pressed Enter (returnPressed() is emmited) call the method updateUi()
        self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            # Convert input text to a Unicode object
            text = unicode(self.lineedit.text())
            # use eval() to evaluate string as an expression
            result = eval(text)
            self.browser.append("%s = <b>%s</b>" % (text, result))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)

# Create the QApplication object
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
