import time
from PyQt5.QtCore import QTimer, QTime, pyqtSignal, QObject


class StopWatch(QObject):
    timer_tic = pyqtSignal(str)
    _FORMAT = 'hh:mm:ss'

    def __init__(self):
        super(StopWatch, self).__init__()
        self.timer = QTimer()
        self.passed_time = QTime(0, 0, 0)
        self.timer.timeout.connect(self.showTimer)

    def startTimer(self):
        self.timer.start(1000)

    def stopTimer(self):
        self.timer.stop()

    def showTimer(self):
        self.passed_time = self.passed_time.addSecs(1)
        formated_time = self.passed_time.toString(self._FORMAT)
        self.timer_tic.emit(formated_time)

    def resetTimer(self):
        self.timer.stop()
        self.passed_time = QTime(0, 0, 0)
        return self.passed_time.toString(self._FORMAT)
