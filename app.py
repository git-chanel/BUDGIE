import sys
from PyQt5.QtWidgets import ( QApplication, QDialog, QMainWindow, QMessageBox)
from PyQt5.uic import loadUi
import test

# inside ui folder is the ui_main_window.py file, import the Ui_MainWindow class from that generated file.
from ui.ui_main_window import Ui_MainWindow

# tutorial: https://realpython.com/qt-designer-python/#putting-everything-together-in-an-application
# docs: https://doc.qt.io/qtforpython-5/modules.html

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.actionQuit.triggered.connect(self.close)
        # There was actionAbout 1, but I deleted it, but it is still in the generated code.
        #self.actionAbout_2.triggered.connect(self.about)
        #testing dialog
        self.actionAbout_2.triggered.connect(self.dialog)
        # Connect the button to function. submitButton is a QtWidgets.QPushButton.
        self.submitButton.clicked.connect(self.submitClicked)

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
            #TODO: raise an amount error dialog
            print("Error: Cannot submit invalid amount:", e)
            return

        try:
            date = self.getDateString()
            if not test.validate_date(date):
                raise ValueError(date)
        except ValueError as e:
            #TODO: raise a date error dialog
            print("Error: Cannot submit invalid date:", e)
            return

        test.add_data_csv(test.getDataFilePath(), amount, date)
        self.reset()

    def reset(self):
        self.currencyInput.setValue(0)
        #TODO: perhaps reset date to today, also have a "date today" button to reset it to current date.

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/dialog.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    exitCode = app.exec()
    sys.exit(exitCode)