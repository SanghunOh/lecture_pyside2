import sys
from PySide2 import QtCore, QtGui, QtWidgets
import serial
ser = serial.Serial('/dev/ttyUSB1', 9600)

class SlotWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.roiLabel = QtWidgets.QLabel('Rate of Interest')
    
        self.roiSpin = QtWidgets.QSpinBox()
        self.roiSpin.setMinimum(0)
        self.roiSpin.setMaximum(180)
        
        self.roiDial = QtWidgets.QDial()
        self.roiDial.setNotchesVisible(True)
        self.roiDial.setMinimum(0)
        self.roiDial.setMaximum(180)
    
        self.myGridLayout = QtWidgets.QGridLayout()
    
        self.myGridLayout.addWidget(self.roiLabel, 0, 0)
        self.myGridLayout.addWidget(self.roiSpin, 0, 1)
        self.myGridLayout.addWidget(self.roiDial, 0, 2)
    
        self.setLayout(self.myGridLayout)
        self.setWindowTitle("A simple EMI calculator")
    
        self.roiDial.valueChanged.connect(self.roiSpin.setValue)
        self.roiDial.valueChanged.connect(self.arduino_connect)
        self.roiSpin.valueChanged.connect(self.roiDial.setValue)
        
    def arduino_connect(self):
        cmd = chr(self.roiDial.value()).encode()
        print ('Dail value : ',cmd)
        ser.write(cmd)
        print('arduino_connect ',ser.readline())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = SlotWidget()
    win.show()
    sys.exit(app.exec_())
      