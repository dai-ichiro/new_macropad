from PySide6 import QtSerialPort
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout

class Widget(QMainWindow):

    select_port = Signal(QtSerialPort.QSerialPortInfo)

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.connectLabel = QLabel()
        self.connectLabel.setStyleSheet('font: 24px; font-weight: bold')
        self.connectLabel.setAlignment(Qt.AlignCenter)

        self.connectBtn = QPushButton('connect')
        self.connectBtn.setStyleSheet('font: 24px; font-weight: bold')
        self.connectBtn.clicked.connect(self.selectBtn)

        self.port_selector = QComboBox()
        self.port_selector.setStyleSheet('font: 24px; font-weight: bold')
        self.port_list = QtSerialPort.QSerialPortInfo.availablePorts()
        for each_port in self.port_list:
            self.port_selector.addItem(f'{each_port.portName()}: {each_port.description()}')

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.port_selector)
        layout.addWidget(self.connectBtn)
        layout.addWidget(self.connectLabel)

        main = QWidget()
        main.setLayout(layout)

        self.setCentralWidget(main)
            
    def selectBtn(self):
        self.connectLabel.setText('sending serial')
        self.connectBtn.setEnabled(False)
        list_index = self.port_selector.currentIndex()
        self.port_list[list_index]
        self.select_port.emit(self.port_list[list_index])