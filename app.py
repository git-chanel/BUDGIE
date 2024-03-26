import sys
from PyQt5.QtWidgets import ( QApplication, QDialog, QMainWindow, QMessageBox)
from PyQt5.uic import loadUi

# inside ui folder is the ui_main_window.py file, import the Ui_MainWindow class from that generated file.
from ui.ui_main_window import Ui_MainWindow

# TODO: https://realpython.com/qt-designer-python/#putting-everything-together-in-an-application

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