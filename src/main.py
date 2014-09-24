#!/usr/bin/env python

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from ui_mainform import Ui_MainWindow


class MainForm(QMainWindow):

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    @pyqtSlot(bool)
    def on_pushButtonD_toggled(self, value):
        print str(value)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec_())
