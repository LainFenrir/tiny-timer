# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SmallTimer_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(210, 60)
        MainWindow.setMaximumSize(QtCore.QSize(250, 60))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 250, 60))
        self.frame.setMaximumSize(QtCore.QSize(251, 60))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: deepskyblue;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.startBtn = QtWidgets.QPushButton(self.frame)
        self.startBtn.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.startBtn.setObjectName("startBtn")
        self.timerLabel = QtWidgets.QLabel(self.frame)
        self.timerLabel.setGeometry(QtCore.QRect(80, 0, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.timerLabel.setFont(font)
        self.timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerLabel.setObjectName("timerLabel")
        self.resetBtn = QtWidgets.QPushButton(self.frame)
        self.resetBtn.setGeometry(QtCore.QRect(40, 0, 41, 41))
        self.resetBtn.setObjectName("resetBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 210, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionProgram_List = QtWidgets.QAction(MainWindow)
        self.actionProgram_List.setObjectName("actionProgram_List")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuProgram.addAction(self.actionProgram_List)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProgram.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.startBtn.clicked.connect(MainWindow.startTimer)
        self.resetBtn.clicked.connect(MainWindow.resetTimer)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Small Timer"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.timerLabel.setText(_translate("MainWindow", "00:00:00"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuProgram.setTitle(_translate("MainWindow", "Program"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionProgram_List.setText(_translate("MainWindow", "Program List"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

