# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainform.ui'
#
# Created: Mon Sep 29 21:34:33 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(320, 240)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        MainWindow.setWindowTitle(_fromUtf8("Mid!Magic"))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(25, 25))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.tabWidget.setSizeIncrement(QtCore.QSize(499, 566))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.AllScales = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AllScales.sizePolicy().hasHeightForWidth())
        self.AllScales.setSizePolicy(sizePolicy)
        self.AllScales.setObjectName(_fromUtf8("AllScales"))
        self.listWidgetNotes = QtGui.QListWidget(self.AllScales)
        self.listWidgetNotes.setGeometry(QtCore.QRect(10, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listWidgetNotes.setFont(font)
        self.listWidgetNotes.setAutoFillBackground(False)
        self.listWidgetNotes.setFrameShape(QtGui.QFrame.StyledPanel)
        self.listWidgetNotes.setFrameShadow(QtGui.QFrame.Sunken)
        self.listWidgetNotes.setAutoScroll(True)
        self.listWidgetNotes.setMovement(QtGui.QListView.Static)
        self.listWidgetNotes.setFlow(QtGui.QListView.LeftToRight)
        self.listWidgetNotes.setProperty("isWrapping", False)
        self.listWidgetNotes.setResizeMode(QtGui.QListView.Fixed)
        self.listWidgetNotes.setLayoutMode(QtGui.QListView.SinglePass)
        self.listWidgetNotes.setSpacing(2)
        self.listWidgetNotes.setUniformItemSizes(False)
        self.listWidgetNotes.setWordWrap(True)
        self.listWidgetNotes.setSelectionRectVisible(True)
        self.listWidgetNotes.setObjectName(_fromUtf8("listWidgetNotes"))
        item = QtGui.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetNotes.addItem(item)
        self.listWidgetScales = QtGui.QListWidget(self.AllScales)
        self.listWidgetScales.setGeometry(QtCore.QRect(10, 50, 281, 81))
        self.listWidgetScales.setTextElideMode(QtCore.Qt.ElideRight)
        self.listWidgetScales.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.listWidgetScales.setFlow(QtGui.QListView.TopToBottom)
        self.listWidgetScales.setProperty("isWrapping", False)
        self.listWidgetScales.setResizeMode(QtGui.QListView.Adjust)
        self.listWidgetScales.setViewMode(QtGui.QListView.ListMode)
        self.listWidgetScales.setUniformItemSizes(True)
        self.listWidgetScales.setWordWrap(True)
        self.listWidgetScales.setObjectName(_fromUtf8("listWidgetScales"))
        self.pushButtonMagic = QtGui.QPushButton(self.AllScales)
        self.pushButtonMagic.setGeometry(QtCore.QRect(10, 136, 93, 26))
        self.pushButtonMagic.setCheckable(True)
        self.pushButtonMagic.setObjectName(_fromUtf8("pushButtonMagic"))
        self.pushButtonExit = QtGui.QPushButton(self.AllScales)
        self.pushButtonExit.setGeometry(QtCore.QRect(190, 136, 93, 26))
        self.pushButtonExit.setCheckable(True)
        self.pushButtonExit.setObjectName(_fromUtf8("pushButtonExit"))
        self.pushButtonPanic = QtGui.QPushButton(self.AllScales)
        self.pushButtonPanic.setGeometry(QtCore.QRect(120, 136, 50, 26))
        self.pushButtonPanic.setCheckable(True)
        self.pushButtonPanic.setObjectName(_fromUtf8("pushButtonPanic"))
        self.tabWidget.addTab(self.AllScales, _fromUtf8(""))
        self.CustomScale = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CustomScale.sizePolicy().hasHeightForWidth())
        self.CustomScale.setSizePolicy(sizePolicy)
        self.CustomScale.setSizeIncrement(QtCore.QSize(432, 43))
        self.CustomScale.setBaseSize(QtCore.QSize(400, 400))
        self.CustomScale.setObjectName(_fromUtf8("CustomScale"))
        self.pushButtonCS = QtGui.QPushButton(self.CustomScale)
        self.pushButtonCS.setGeometry(QtCore.QRect(30, 10, 41, 71))
        self.pushButtonCS.setAutoFillBackground(True)
        self.pushButtonCS.setCheckable(True)
        self.pushButtonCS.setAutoDefault(False)
        self.pushButtonCS.setFlat(False)
        self.pushButtonCS.setObjectName(_fromUtf8("pushButtonCS"))
        self.pushButtonFS = QtGui.QPushButton(self.CustomScale)
        self.pushButtonFS.setGeometry(QtCore.QRect(150, 10, 41, 71))
        self.pushButtonFS.setCheckable(True)
        self.pushButtonFS.setObjectName(_fromUtf8("pushButtonFS"))
        self.pushButtonC = QtGui.QPushButton(self.CustomScale)
        self.pushButtonC.setGeometry(QtCore.QRect(10, 80, 41, 81))
        self.pushButtonC.setCheckable(True)
        self.pushButtonC.setObjectName(_fromUtf8("pushButtonC"))
        self.pushButtonE = QtGui.QPushButton(self.CustomScale)
        self.pushButtonE.setGeometry(QtCore.QRect(90, 80, 41, 81))
        self.pushButtonE.setCheckable(True)
        self.pushButtonE.setObjectName(_fromUtf8("pushButtonE"))
        self.pushButtonF = QtGui.QPushButton(self.CustomScale)
        self.pushButtonF.setGeometry(QtCore.QRect(130, 80, 41, 81))
        self.pushButtonF.setCheckable(True)
        self.pushButtonF.setObjectName(_fromUtf8("pushButtonF"))
        self.pushButtonD = QtGui.QPushButton(self.CustomScale)
        self.pushButtonD.setGeometry(QtCore.QRect(50, 80, 41, 81))
        self.pushButtonD.setCheckable(True)
        self.pushButtonD.setObjectName(_fromUtf8("pushButtonD"))
        self.pushButtonB = QtGui.QPushButton(self.CustomScale)
        self.pushButtonB.setGeometry(QtCore.QRect(250, 80, 41, 81))
        self.pushButtonB.setCheckable(True)
        self.pushButtonB.setObjectName(_fromUtf8("pushButtonB"))
        self.pushButtonA = QtGui.QPushButton(self.CustomScale)
        self.pushButtonA.setGeometry(QtCore.QRect(210, 80, 41, 81))
        self.pushButtonA.setCheckable(True)
        self.pushButtonA.setObjectName(_fromUtf8("pushButtonA"))
        self.pushButtonAS = QtGui.QPushButton(self.CustomScale)
        self.pushButtonAS.setGeometry(QtCore.QRect(230, 10, 41, 71))
        self.pushButtonAS.setCheckable(True)
        self.pushButtonAS.setObjectName(_fromUtf8("pushButtonAS"))
        self.pushButtonDS = QtGui.QPushButton(self.CustomScale)
        self.pushButtonDS.setGeometry(QtCore.QRect(70, 10, 41, 71))
        self.pushButtonDS.setCheckable(True)
        self.pushButtonDS.setObjectName(_fromUtf8("pushButtonDS"))
        self.pushButtonG = QtGui.QPushButton(self.CustomScale)
        self.pushButtonG.setGeometry(QtCore.QRect(170, 80, 41, 81))
        self.pushButtonG.setCheckable(True)
        self.pushButtonG.setObjectName(_fromUtf8("pushButtonG"))
        self.pushButtonGS = QtGui.QPushButton(self.CustomScale)
        self.pushButtonGS.setGeometry(QtCore.QRect(190, 10, 41, 71))
        self.pushButtonGS.setCheckable(True)
        self.pushButtonGS.setObjectName(_fromUtf8("pushButtonGS"))
        self.tabWidget.addTab(self.CustomScale, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.spinBoxTranspose = QtGui.QSpinBox(self.tab)
        self.spinBoxTranspose.setGeometry(QtCore.QRect(90, 10, 81, 26))
        self.spinBoxTranspose.setMinimum(-12)
        self.spinBoxTranspose.setMaximum(12)
        self.spinBoxTranspose.setObjectName(_fromUtf8("spinBoxTranspose"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidgetInput = QtGui.QListWidget(self.tab)
        self.listWidgetInput.setGeometry(QtCore.QRect(10, 50, 281, 51))
        self.listWidgetInput.setObjectName(_fromUtf8("listWidgetInput"))
        self.listWidgetOutput = QtGui.QListWidget(self.tab)
        self.listWidgetOutput.setGeometry(QtCore.QRect(10, 110, 281, 51))
        self.listWidgetOutput.setObjectName(_fromUtf8("listWidgetOutput"))
        self.pushButtonScan = QtGui.QPushButton(self.tab)
        self.pushButtonScan.setGeometry(QtCore.QRect(190, 10, 93, 27))
        self.pushButtonScan.setObjectName(_fromUtf8("pushButtonScan"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionMidiInput = QtGui.QAction(MainWindow)
        self.actionMidiInput.setCheckable(False)
        self.actionMidiInput.setObjectName(_fromUtf8("actionMidiInput"))
        self.actionMidiOutput = QtGui.QAction(MainWindow)
        self.actionMidiOutput.setObjectName(_fromUtf8("actionMidiOutput"))
        self.actionScanForDevices = QtGui.QAction(MainWindow)
        self.actionScanForDevices.setObjectName(_fromUtf8("actionScanForDevices"))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        __sortingEnabled = self.listWidgetNotes.isSortingEnabled()
        self.listWidgetNotes.setSortingEnabled(False)
        item = self.listWidgetNotes.item(0)
        item.setText(_translate("MainWindow", "C", None))
        item = self.listWidgetNotes.item(1)
        item.setText(_translate("MainWindow", "C#", None))
        item = self.listWidgetNotes.item(2)
        item.setText(_translate("MainWindow", "D", None))
        item = self.listWidgetNotes.item(3)
        item.setText(_translate("MainWindow", "D#", None))
        item = self.listWidgetNotes.item(4)
        item.setText(_translate("MainWindow", "E", None))
        item = self.listWidgetNotes.item(5)
        item.setText(_translate("MainWindow", "F", None))
        item = self.listWidgetNotes.item(6)
        item.setText(_translate("MainWindow", "F#", None))
        item = self.listWidgetNotes.item(7)
        item.setText(_translate("MainWindow", "G", None))
        item = self.listWidgetNotes.item(8)
        item.setText(_translate("MainWindow", "G#", None))
        item = self.listWidgetNotes.item(9)
        item.setText(_translate("MainWindow", "A", None))
        item = self.listWidgetNotes.item(10)
        item.setText(_translate("MainWindow", "A#", None))
        item = self.listWidgetNotes.item(11)
        item.setText(_translate("MainWindow", "B", None))
        self.listWidgetNotes.setSortingEnabled(__sortingEnabled)
        self.pushButtonMagic.setText(_translate("MainWindow", "Magic mode", None))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit", None))
        self.pushButtonPanic.setText(_translate("MainWindow", "Panic", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AllScales), _translate("MainWindow", "All scales", None))
        self.pushButtonCS.setText(_translate("MainWindow", "C#", None))
        self.pushButtonFS.setText(_translate("MainWindow", "F#", None))
        self.pushButtonC.setText(_translate("MainWindow", "C", None))
        self.pushButtonE.setText(_translate("MainWindow", "E", None))
        self.pushButtonF.setText(_translate("MainWindow", "F", None))
        self.pushButtonD.setText(_translate("MainWindow", "D", None))
        self.pushButtonB.setText(_translate("MainWindow", "B", None))
        self.pushButtonA.setText(_translate("MainWindow", "A", None))
        self.pushButtonAS.setText(_translate("MainWindow", "A#", None))
        self.pushButtonDS.setText(_translate("MainWindow", "D#", None))
        self.pushButtonG.setText(_translate("MainWindow", "G", None))
        self.pushButtonGS.setText(_translate("MainWindow", "G#", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CustomScale), _translate("MainWindow", "Custom scale", None))
        self.label.setText(_translate("MainWindow", "Transpose:", None))
        self.pushButtonScan.setText(_translate("MainWindow", "Scan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Configurate", None))
        self.actionMidiInput.setText(_translate("MainWindow", "Midi input", None))
        self.actionMidiOutput.setText(_translate("MainWindow", "Midi output", None))
        self.actionScanForDevices.setText(_translate("MainWindow", "Scan for devices", None))

