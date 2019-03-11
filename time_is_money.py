"""
    This is a joke program that I made when I was bored. I thought that if me and
    the other interns had a program that counts up the money we are making in real
    time, we would be more motivated to work. It also helps since we were hourly.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui
from threading import Thread
from time import sleep
from datetime import datetime, timedelta

class CountMoney(QMainWindow):
    """
        The CountMoney Class inherits from QMainWindow and builds the GUI
    """

    def __init__(self):
        """
            function:
                __init__ - This is the constructor that builds the GUI

            args:
                None

            returns:
                None

            raises:
                None
        """

        # Call the parent constructor
        QMainWindow.__init__(self)

        # Create the GUI and set the class variables
        self.initUI()
        self.done = False
        self.globalCounter = 0
		
    def initUI(self):
        """
            function:
                initUI - This function Builds the GUI

            args:
                None

            returns:
                None

            raises:
                None
        """

        # Set the size of the window and keep the user from resizing
        self.setGeometry(150,150,275,225)
        self.setFixedSize(275,225)

        # Set the title and icon
        self.setWindowTitle('Money Counter')
        self.setWindowIcon(QtGui.QIcon(r'C:\money.jpg'))

        # Create the clock in button and bind it to self.clockIn()
        self.clockinBtn = QPushButton('Clock In', self)
        self.clockinBtn.resize(self.clockinBtn.sizeHint())
        self.clockinBtn.move(10,10)
        self.clockinBtn.clicked.connect(self.clockIn)

        # Create the clock out button and bind it to self.clockOut()
        self.clockoutBtn = QPushButton('Clock Out', self)
        self.clockoutBtn.resize(self.clockoutBtn.sizeHint())
        self.clockoutBtn.move(100,10)
        self.clockoutBtn.clicked.connect(self.clockOut)

        # Create the reset button and bind it to self.reset()
        self.resetBtn = QPushButton('Reset', self)
        self.resetBtn.resize(self.resetBtn.sizeHint())
        self.resetBtn.move(190,10)
        self.resetBtn.clicked.connect(self.reset)

        # Create the label that indicates accumulated money
        self.moneyLog = QLabel(self)
        self.moneyLog.setGeometry(0,50,200,150)
        self.moneyLog.setFont(QtGui.QFont('Times', 32, QtGui.QFont.Bold))
        self.moneyLog.setText(' $000.00')

        # Create the rate input QLineEdit so the user can input their hourly rate
        self.rate = QLineEdit(self)
        self.rate.setGeometry(90,60,150,25)
        self.rate.setFont(QtGui.QFont('Times', 14))
        self.rate.setText('0')

        # Create the label to indicate to the user where to enter their
        # hourly rate
        self.rateLbl = QLabel(self)
        self.rateLbl.setGeometry(25,60,50,25)
        self.rateLbl.setFont(QtGui.QFont('Times', 14))
        self.rateLbl.setText('Rate -')

        # Create the clock in label
        self.inLbl = QLabel(self)
        self.inLbl.setGeometry(5,175,300,25)
        self.inLbl.setFont(QtGui.QFont('Times', 12))
        self.inLbl.setText('Clocked in at: ')

        # Create the clock out label
        self.outLbl = QLabel(self)
        self.outLbl.setGeometry(5,200,300,25)
        self.outLbl.setFont(QtGui.QFont('Times', 12))
        self.outLbl.setText('Clocked out at: ')

        # Show the GUI
        self.show()

    def clockIn(self):
        """
            function:
                clockIn - Starts the money accumulation

            args:
                None

            returns:
                None

            raises:
                None
        """

        # Set the done variable to false and start the count thread
        self.done = False
        Thread(target=self.count).start()
        return

    def count(self):
        """
            function:
                count - Function that does the accumulation of money

            args:
                None

            returns:
                None

            raises:
                None
        """

        # Set a local copy of the counter
        counter = self.globalCounter

        # Get the current time
        time = datetime.now()

        # Set the clock in time
        self.inLbl.setText('Clocked in at: ' + str(time.month) + '/' + str(time.day) + '/' + str(time.year) + ' ' + str(time.hour) + ':' + str(time.minute) + ':' + str(time.second))
        
        # Reset the size of the money label so that it can handle the range of numbers
        self.moneyLog.setGeometry(30,50,200,150)

        # Do until the clock out button is clicked...
        while True:

            # Set the current accumulated money based on how much time is passed
            self.moneyLog.setText('  $' + str(round(float(self.rate.text())*counter/3600,2)))

            # Sleep for a second and increment the counter
            sleep(1)
            counter+=1

            # If self.done is true, that means the clock out button was pressed
            if self.done == True:

                # Get the current time and set the label to indicate when the user clocked out
                new = datetime.now()
                self.outLbl.setText('Clocked out at: ' + str(new.month) + '/' + str(new.day) + '/' + str(new.year) + ' ' + str(new.hour) + ':' + str(new.minute) + ':' + str(new.second))
                self.globalCounter = 0
                return		

    def clockOut(self):
        """
            function:
                clockOut - this function stops the accumulation

            args:
                None

            returns:
                None

            raises:
                None
        """

        # Set the class variable that stops accumulation
        self.done = True


    def reset(self):
        """
            function:
                reset - this function resets everything to default
        """

        # Stop accumulating if currently doing so...
        self.done = True

        # Reset all of the labels and counter
        self.moneyLog.setText(' $000.00')
        self.inLbl.setText('Clocked in at: ')
        sleep(0.5)
        self.outLbl.setText('Clocked out at: ')
        self.globalCounter = 0

# Do this if the program is running on its own
if __name__ == "__main__":

    # Create a QApplication object and pass in the arg vector
    app = QApplication(sys.argv)

    # Create the GUI and start the main loop
    window = CountMoney()
    sys.exit(app.exec_())


