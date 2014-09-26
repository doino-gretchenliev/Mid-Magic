#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

from ui_mainform import Ui_MainWindow
from utils import Utils
from cache import ScaleCache


class MainForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        
        self.utils = Utils();
        self.cache = ScaleCache();

        self.ui = Ui_MainWindow();
        self.ui.setupUi(self);
        
        self.loadAvailableScales();
        
    def loadAvailableScales(self):
        for scale in self.utils.getAvailableScales():
            self.ui.listWidgetScales.addItem(scale)
                    
    @QtCore.pyqtSlot(str)
    def on_listWidgetScales_currentTextChanged(self, value):
        print str(value)


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec_())
