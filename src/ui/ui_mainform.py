# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_calculatorform.ui'
#
# Created: Wed Sep 24 23:52:50 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(320, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        MainWindow.setWindowTitle("Mid!Magic")
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(25, 25))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.tabWidget.setSizeIncrement(QtCore.QSize(499, 566))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.AllScales = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AllScales.sizePolicy().hasHeightForWidth())
        self.AllScales.setSizePolicy(sizePolicy)
        self.AllScales.setObjectName("AllScales")
        self.listWidget = QtWidgets.QListWidget(self.AllScales)
        self.listWidget.setGeometry(QtCore.QRect(10, 0, 281, 31))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setSpacing(3)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(self.AllScales)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 40, 281, 101))
        self.listWidget_2.setMovement(QtWidgets.QListView.Static)
        self.listWidget_2.setProperty("isWrapping", True)
        self.listWidget_2.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget_2.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget_2.setModelColumn(0)
        self.listWidget_2.setUniformItemSizes(True)
        self.listWidget_2.setWordWrap(False)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.tabWidget.addTab(self.AllScales, "")
        self.CustomScale = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CustomScale.sizePolicy().hasHeightForWidth())
        self.CustomScale.setSizePolicy(sizePolicy)
        self.CustomScale.setSizeIncrement(QtCore.QSize(432, 43))
        self.CustomScale.setBaseSize(QtCore.QSize(400, 400))
        self.CustomScale.setObjectName("CustomScale")
        self.pushButtonCS = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonCS.setGeometry(QtCore.QRect(30, 10, 41, 61))
        self.pushButtonCS.setAutoFillBackground(True)
        self.pushButtonCS.setCheckable(True)
        self.pushButtonCS.setAutoDefault(False)
        self.pushButtonCS.setFlat(False)
        self.pushButtonCS.setObjectName("pushButtonCS")
        self.pushButtonFS = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonFS.setGeometry(QtCore.QRect(150, 10, 41, 61))
        self.pushButtonFS.setCheckable(True)
        self.pushButtonFS.setObjectName("pushButtonFS")
        self.pushButtonC = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonC.setGeometry(QtCore.QRect(10, 70, 41, 71))
        self.pushButtonC.setCheckable(True)
        self.pushButtonC.setObjectName("pushButtonC")
        self.pushButtonE = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonE.setGeometry(QtCore.QRect(90, 70, 41, 71))
        self.pushButtonE.setCheckable(True)
        self.pushButtonE.setObjectName("pushButtonE")
        self.pushButtonF = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonF.setGeometry(QtCore.QRect(130, 70, 41, 71))
        self.pushButtonF.setCheckable(True)
        self.pushButtonF.setObjectName("pushButtonF")
        self.pushButtonD = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonD.setGeometry(QtCore.QRect(50, 70, 41, 71))
        self.pushButtonD.setCheckable(True)
        self.pushButtonD.setObjectName("pushButtonD")
        self.pushButtonB = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonB.setGeometry(QtCore.QRect(250, 70, 41, 71))
        self.pushButtonB.setCheckable(True)
        self.pushButtonB.setObjectName("pushButtonB")
        self.pushButtonA = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonA.setGeometry(QtCore.QRect(210, 70, 41, 71))
        self.pushButtonA.setCheckable(True)
        self.pushButtonA.setObjectName("pushButtonA")
        self.pushButtonAS = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonAS.setGeometry(QtCore.QRect(230, 10, 41, 61))
        self.pushButtonAS.setCheckable(True)
        self.pushButtonAS.setObjectName("pushButtonAS")
        self.pushButtonDS = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonDS.setGeometry(QtCore.QRect(70, 10, 41, 61))
        self.pushButtonDS.setCheckable(True)
        self.pushButtonDS.setObjectName("pushButtonDS")
        self.pushButtonG = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonG.setGeometry(QtCore.QRect(170, 70, 41, 71))
        self.pushButtonG.setCheckable(True)
        self.pushButtonG.setObjectName("pushButtonG")
        self.pushButtonGS = QtWidgets.QPushButton(self.CustomScale)
        self.pushButtonGS.setGeometry(QtCore.QRect(190, 10, 41, 61))
        self.pushButtonGS.setCheckable(True)
        self.pushButtonGS.setObjectName("pushButtonGS")
        self.tabWidget.addTab(self.CustomScale, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.dialTranspose = QtWidgets.QDial(self.tab)
        self.dialTranspose.setGeometry(QtCore.QRect(80, 10, 141, 101))
        self.dialTranspose.setMinimum(-12)
        self.dialTranspose.setMaximum(12)
        self.dialTranspose.setOrientation(QtCore.Qt.Horizontal)
        self.dialTranspose.setInvertedAppearance(False)
        self.dialTranspose.setInvertedControls(False)
        self.dialTranspose.setObjectName("dialTranspose")
        self.spinBoxTranspose = QtWidgets.QSpinBox(self.tab)
        self.spinBoxTranspose.setGeometry(QtCore.QRect(110, 110, 81, 26))
        self.spinBoxTranspose.setMinimum(-12)
        self.spinBoxTranspose.setMaximum(12)
        self.spinBoxTranspose.setObjectName("spinBoxTranspose")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 24))
        self.menubar.setAcceptDrops(True)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menuAbout.setAcceptDrops(True)
        self.menuAbout.setTearOffEnabled(False)
        self.menuAbout.setSeparatorsCollapsible(False)
        self.menuAbout.setToolTipsVisible(False)
        self.menuAbout.setObjectName("menuAbout")
        self.menuMagic_mode = QtWidgets.QMenu(self.menubar)
        self.menuMagic_mode.setTearOffEnabled(False)
        self.menuMagic_mode.setSeparatorsCollapsible(False)
        self.menuMagic_mode.setObjectName("menuMagic_mode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMidi_input = QtWidgets.QAction(MainWindow)
        self.actionMidi_input.setCheckable(False)
        self.actionMidi_input.setObjectName("actionMidi_input")
        self.actionMidi_output = QtWidgets.QAction(MainWindow)
        self.actionMidi_output.setObjectName("actionMidi_output")
        self.actionScan_for_devices = QtWidgets.QAction(MainWindow)
        self.actionScan_for_devices.setObjectName("actionScan_for_devices")
        self.menuNew.addAction(self.actionMidi_input)
        self.menuNew.addAction(self.actionMidi_output)
        self.menuNew.addAction(self.actionScan_for_devices)
        self.menubar.addAction(self.menuMagic_mode.menuAction())
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.dialTranspose.valueChanged['int'].connect(self.spinBoxTranspose.setValue)
        self.spinBoxTranspose.valueChanged['int'].connect(self.dialTranspose.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "C"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "C#"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "D"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "D#"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "E"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "F"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "F#"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "G"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "G#"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "A"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "A#"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "B"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "first"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "second"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "thrid"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "fourth"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "fifth"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "sexth"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("MainWindow", "seveth"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AllScales), _translate("MainWindow", "All scales"))
        self.pushButtonCS.setText(_translate("MainWindow", "C#"))
        self.pushButtonFS.setText(_translate("MainWindow", "F#"))
        self.pushButtonC.setText(_translate("MainWindow", "C"))
        self.pushButtonE.setText(_translate("MainWindow", "E"))
        self.pushButtonF.setText(_translate("MainWindow", "F"))
        self.pushButtonD.setText(_translate("MainWindow", "D"))
        self.pushButtonB.setText(_translate("MainWindow", "B"))
        self.pushButtonA.setText(_translate("MainWindow", "A"))
        self.pushButtonAS.setText(_translate("MainWindow", "A#"))
        self.pushButtonDS.setText(_translate("MainWindow", "D#"))
        self.pushButtonG.setText(_translate("MainWindow", "G"))
        self.pushButtonGS.setText(_translate("MainWindow", "G#"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CustomScale), _translate("MainWindow", "Custom scale"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Transpose"))
        self.menuNew.setTitle(_translate("MainWindow", "Configuration"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuMagic_mode.setTitle(_translate("MainWindow", "Magic mode"))
        self.actionMidi_input.setText(_translate("MainWindow", "Midi input"))
        self.actionMidi_output.setText(_translate("MainWindow", "Midi output"))
        self.actionScan_for_devices.setText(_translate("MainWindow", "Scan for devices"))
