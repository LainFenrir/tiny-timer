import sys
import os
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow
from timer_logic.core import StopWatch
from ui.SmallTimer_main import Ui_MainWindow
from utils.styles_window import STATE_DEFAULT, STATE_RUNNING, STATE_STOP


class MainWindow(QMainWindow):
    _STOP = "Stop"
    _START = "Start"

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # Timer related variables
        self.stop_watch = StopWatch()
        self.is_timer_running = False
        self.is_reseted = True
        self.stop_watch.timer_tic.connect(self.updateLabel)
        # style
        self.ui.frame.setStyleSheet(STATE_DEFAULT)
        self.ui.timerLabel.setStyleSheet(STATE_DEFAULT)

    # ----- functionality----
    @pyqtSlot()
    def startTimer(self):
        if self.is_timer_running is False:
            self.is_timer_running = True
            self.is_reseted = False
            self.stop_watch.startTimer()
            self.changeButtonName()
            self.changeState()
        else:
            self.is_timer_running = False
            self.stop_watch.stopTimer()
            self.changeButtonName()
            self.changeState()

    @pyqtSlot()
    def resetTimer(self):
        self.is_timer_running = False
        self.is_reseted = True
        passed_time = self.stop_watch.resetTimer()
        self.ui.timerLabel.setText(passed_time)
        self.changeState()

    @pyqtSlot(str)
    def updateLabel(self, formated_time):
        self.ui.timerLabel.setText(formated_time)

    # ----- graphic -----
    def changeButtonName(self):
        if self.is_timer_running is True:
            self.ui.startBtn.setText(self._STOP)
        else:
            self.ui.startBtn.setText(self._START)

    def changeState(self):
        if self.is_reseted is True:
            self.ui.frame.setStyleSheet(STATE_DEFAULT)
            self.ui.timerLabel.setStyleSheet(STATE_DEFAULT)
            self.setWindowTitle("Tiny Timer")
        else:
            if self.is_timer_running is True:
                self.ui.frame.setStyleSheet(STATE_RUNNING)
                self.ui.timerLabel.setStyleSheet(STATE_RUNNING)
                self.setWindowTitle("GO GO GO")
            else:
                self.ui.frame.setStyleSheet(STATE_STOP)
                self.ui.timerLabel.setStyleSheet(STATE_STOP)
                self.setWindowTitle("Y U NOT WORK")
