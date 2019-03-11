import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui
from threading import Thread
from time import sleep
from datetime import datetime, timedelta

class CountMoney(QMainWindow):

    def __init__(self):
		
        QMainWindow.__init__(self)
        self.initUI()
        self.done = False
        self.globalCounter = 0
		
    def initUI(self):

        self.setGeometry(150,150,275,225)
        self.setFixedSize(275,225)
        self.setWindowTitle('Money Counter')
        self.setWindowIcon(QtGui.QIcon(r'C:\money.jpg'))

        self.clockinBtn = QPushButton('Clock In', self)
        self.clockinBtn.resize(self.clockinBtn.sizeHint())
        self.clockinBtn.move(10,10)
        self.clockinBtn.clicked.connect(self.clockIn)

        self.clockoutBtn = QPushButton('Clock Out', self)
        self.clockoutBtn.resize(self.clockoutBtn.sizeHint())
        self.clockoutBtn.move(100,10)
        self.clockoutBtn.clicked.connect(self.clockOut)

        self.resetBtn = QPushButton('Reset', self)
        self.resetBtn.resize(self.resetBtn.sizeHint())
        self.resetBtn.move(190,10)
        self.resetBtn.clicked.connect(self.reset)

        self.moneyLog = QLabel(self)
        self.moneyLog.setGeometry(0,50,200,150)
        self.moneyLog.setFont(QtGui.QFont('Times', 32, QtGui.QFont.Bold))
        self.moneyLog.setText(' $000.00')

        self.rate = QLineEdit(self)
        self.rate.setGeometry(90,60,150,25)
        self.rate.setFont(QtGui.QFont('Times', 14))
        self.rate.setText('0')

        self.rateLbl = QLabel(self)
        self.rateLbl.setGeometry(25,60,50,25)
        self.rateLbl.setFont(QtGui.QFont('Times', 14))
        self.rateLbl.setText('Rate -')

        self.inLbl = QLabel(self)
        self.inLbl.setGeometry(5,175,300,25)
        self.inLbl.setFont(QtGui.QFont('Times', 12))
        self.inLbl.setText('Clocked in at: ')

        self.outLbl = QLabel(self)
        self.outLbl.setGeometry(5,200,300,25)
        self.outLbl.setFont(QtGui.QFont('Times', 12))
        self.outLbl.setText('Clocked out at: ')

        self.show()

    def clockIn(self):

        self.done = False
        Thread(target=self.count).start()
        return

    def count(self):

        counter = self.globalCounter
        time = datetime.now()
        self.inLbl.setText('Clocked in at: ' + str(time.month) + '/' + str(time.day) + '/' + str(time.year) + ' ' + str(time.hour) + ':' + str(time.minute) + ':' + str(time.second))
        self.moneyLog.setGeometry(30,50,200,150)
        while True:

            self.moneyLog.setText('  $' + str(round(float(self.rate.text())*counter/3600,2)))
            sleep(1)
            counter+=1
            if self.done == True:

                new = datetime.now()
                self.outLbl.setText('Clocked out at: ' + str(new.month) + '/' + str(new.day) + '/' + str(new.year) + ' ' + str(new.hour) + ':' + str(new.minute) + ':' + str(new.second))
                self.globalCounter = 0
                return		

    def clockOut(self):

        self.done = True


    def reset(self):

        if self.done == False:
            self.done = True

        self.moneyLog.setText(' $000.00')
        self.inLbl.setText('Clocked in at: ')
        sleep(1.5)
        self.outLbl.setText('Clocked out at: ')
        self.globalCounter = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CountMoney()
    sys.exit(app.exec_())

    fw.close()

