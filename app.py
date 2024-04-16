import sys
from PyQt5.QtWidgets import ( QApplication, QDialog, QMainWindow, QMessageBox, QCalendarWidget)
from PyQt5 import QtCore
from PyQt5.uic import loadUi
import pyqtgraph as pg
from datetime import datetime
import test

# inside ui folder is the ui_main_window.py file, import the Ui_MainWindow class from that generated file.
from ui.ui_main_window import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        # The graph widget
        self.graph = pg.PlotWidget()
        # The plotted line on the graph.
        self.line = ""
        # Create the graph.
        self.addGraph()

    def connectSignalsSlots(self):
        self.actionQuit.triggered.connect(self.close)
        self.actionAbout_2.triggered.connect(self.dialog)
        # Connect the button to function. submitButton is a QtWidgets.QPushButton.
        self.submitButton.clicked.connect(self.submitClicked)

    def addGraph(self):
        self.graph.setMinimumSize(QtCore.QSize(400, 400))
        self.verticalLayoutGraphContainer.addWidget(self.graph)
        # Now draw the initial contents of the graph.
        self.plotGraph(True)

    def plotGraph(self, initialize = False):
        data = test.read_data_csv(test.getDataFilePath())
        print(list(data))
        # TODO: how to make it show the dates labels.
        time = range(len(data))
        amount = list(data.values())
        print(time)
        print(amount)
        # TODO: figure out how to refresh graph fully, so it doesn't act weird when inserting between exisitng or older dates 
        if initialize:
            self.line = self.graph.plot(time, amount)
        elif self.line:
            self.line.setData(time, amount)

    def about(self):
        QMessageBox.about(
            self,
            "About BUDGIE",
            """
            <p>A budget tracking app build with:</p>
            <p>- PyQt</p>
            <p>- Qt Designer</p>
            <p>- Python 3.12</p>
            <center><p>:)</p></center>
            """
        )

    def dialog(self):
        dialog = Dialog(self)
        # TODO: organize it so you can use these later, call and set them as needed.
        dialog.headerText.setText("Title :)")
        dialog.contentText.setText("Hi there!")
        dialog.exec()

    def getCurrencyAmount(self):
        # currencyInput is a QDoubleSpinBox
        amount = self.currencyInput.value()
        return amount

    def getDateString(self):
        # calendarWidget is a QCalendarWidget, get selected date from widget.
        qDate = self.calendarWidget.selectedDate()
        # Change the date ints into 0 padded strings.
        dayString = str(qDate.day()).zfill(2)
        monthString = str(qDate.month()).zfill(2)
        yearString = str(qDate.year()).zfill(4)
        # Format string so it matches expected date format of dd-mm-yyyy
        dateString = "{0}-{1}-{2}".format(dayString, monthString, yearString)

        return dateString

    def submitClicked(self):
        try:
            amount = self.getCurrencyAmount()
            # Validate amount and also shouldn't submit the default 0 amount.
            if not test.validate_amount(amount) or amount == 0:
                raise ValueError(amount)
        except ValueError as e:
            errorMessage = "Error: Cannot submit invalid amount: {}".format(e)
            print(errorMessage)
            dialog = Dialog(self)
            dialog.setBody(errorMessage)
            dialog.exec()
            return

        try:
            date = self.getDateString()
            if not test.validate_date(date):
                raise ValueError(date)
        except ValueError as e:
            errorMessage = "Error: Cannot submit invalid date: {}".format(e)
            print(errorMessage)
            dialog = Dialog(self)
            dialog.setBody(errorMessage)
            dialog.exec()
            return

        test.add_data_csv(test.getDataFilePath(), amount, date)

        # Update the the graph.
        self.plotGraph()

        # Reset the input fields.
        self.reset()

    def reset(self):
        self.currencyInput.setValue(0)

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/dialog.ui", self)
        
        # set a default header
        self.setHeader("Error")

    def setHeader(self, headerText):
        self.headerText.setText(headerText)

    def setBody(self, bodyText):
        self.contentText.setText(bodyText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    exitCode = app.exec()
    sys.exit(exitCode)