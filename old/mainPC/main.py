from PySide6 import QtSerialPort
from PySide6.QtCore import Qt, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout

from action_list import action_do

class Window(QMainWindow):

    serial = QtSerialPort.QSerialPort()

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.connectLabel = QLabel()
        self.connectLabel.setAlignment(Qt.AlignCenter)

        self.connectBtn = QPushButton('connect')
        self.connectBtn.clicked.connect(self.pushBtn)

        self.port_selector = QComboBox()
        self.port_list = QtSerialPort.QSerialPortInfo.availablePorts()
        for each_port in self.port_list:
            self.port_selector.addItem(f'{each_port.portName()}: {each_port.description()}')

        layout = QVBoxLayout()
        layout.addWidget(self.port_selector)
        layout.addWidget(self.connectBtn)
        layout.addWidget(self.connectLabel)

        main = QWidget()
        main.setLayout(layout)

        self.setCentralWidget(main)
            
    def pushBtn(self):
        list_index = self.port_selector.currentIndex()
        self.serial.setPort(self.port_list[list_index])
        self.serial.setBaudRate(QtSerialPort.QSerialPort.Baud9600)
        self.serial.readyRead.connect(self.receive)
        self.serial.open(QIODevice.ReadOnly)

        self.connectLabel.setText('receiving serial')
        self.connectBtn.setEnabled(False)

    def closeEvent(self, e):
       self.serial.close()
       e.accept()
    
    def receive(self):
        data_from_PC = self.serial.read(1)
        action_do(int.from_bytes(data_from_PC, 'big'))       
        
if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()