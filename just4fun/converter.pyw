"""Currency Converter with GUI

Based on the examples of the book "Rapid GUI programming with Python and Qt" by
Mark Summerfield.

Further reference see:
- http://doc.qt.io/qt-4.8/qobject.html#connect

@author: Mario Garcia
www.mayitzin.com
"""

import sys
import urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Retrieve data from internet
        date = self.getdata()
        # Sort this data in a dictionary
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)
        # Add widget with combined button and popup list
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        # Add a spin box widget that provides doubles
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)
        # Add widget with combined button and popup list
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        # Add text display
        self.toLabel = QLabel("1.00")
        # Lay out widgets in a Grid
        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)
        # Set Connections
        self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.fromSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
        self.setWindowTitle("Currency")

    def updateUi(self):
        # Read the "to" currency
        to = unicode(self.toComboBox.currentText())
        # Read the "from" currency (from is a keyword in Python)
        from_ = unicode(self.fromComboBox.currentText())
        # Calculate the "to" amount
        amount = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()
        # Set the "toLabel" text with the computed amount
        self.toLabel.setText("%0.2f" % amount)

    def getdata(self):
        # Create empty dictionary
        self.rates = {}
        try:
            date = "Unknown"
            fh = urllib2.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")
            for line in fh:
                # Avoid lines starting with # or Non-currency values
                if not line or line.startswith(("#", "Closing ")):
                    continue
                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]
                else:
                    try:
                        # Dictionary with curenncy's name for key and exchange rate as value
                        value = float(fields[-1])
                        self.rates[unicode(fields[0])] = value
                    except ValueError:
                        pass
            return "Exchange Rates Date: " + date
        except Exception, e:
            return "Failed to download:\n%s" % e

# Create QApplication
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
