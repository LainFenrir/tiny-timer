import sys
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from timer_logic.core import StopWatch
from ui.SmallTimer_main import Ui_MainWindow

UI_FOLDER = "ui"
TIMER_UI = "SmallTimer_main.ui"
UI_PATH = os.path.join(sys.path[0], UI_FOLDER)
TIMER_UI_PATH = os.path.join(UI_PATH, TIMER_UI)
# main_window_ui, MainWindowBase = uic.loadUiType(TIMER_UI_PATH)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stop_watch = StopWatch()
        self.is_timer_running = False
        self.stop_watch.timer_tic.connect(self.updateLabel)

    @pyqtSlot()
    def startTimer(self):
        if self.is_timer_running is False:
            self.is_timer_running = True
            self.stop_watch.startTimer()
        else:
            self.is_timer_running = False
            self.stop_watch.stopTimer()

    @pyqtSlot()
    def resetTimer(self):
        passed_time = self.stop_watch.resetTimer()
        self.ui.timerLabel.setText(passed_time)

    @pyqtSlot(str)
    def updateLabel(self, formated_time):
        self.ui.timerLabel.setText(formated_time)
