import sys,time,serial
from PySide6 import QtSerialPort
from PySide6.QtCore import QSize, QIODevice
from PySide6.QtWidgets import QMainWindow, QWidget, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QSizePolicy

ZENHAN=0x35; ENTER=0x28; SPACE=0x2C; BACKSPACE=0x2A; SHIFT=0xE1
CTRL=0xE0; ALT=0xE2; TAB=0x2B; ESC=0x58; WINDOWS=0xE3

SPK={ZENHAN, ENTER, SPACE, BACKSPACE, SHIFT, CTRL, ALT, TAB, ESC, WINDOWS}

TBL={'!':[2,0x1E], '"':[2,0x1F], '#':[2,0x20], '$':[2,0x21], '%':[2,0x22],
        '&':[2,0x23], "'":[2,0x24], '=':[2,0x2D],
        '-':[0,0x2D], '~':[2,0x2E], '^':[0,0x2E], '|':[2,0x89], '\\':[0,0x89],
        '`':[2,0x2F], '@':[0,0x2F], '{':[2,0x30], '[':[0,0x30], '}':[2,0x31],
        ']':[0,0x31], '*':[2,0x34], ':':[0,0x34], '+':[2,0x33], ';':[0,0x33],
        '<':[2,0x36], ',':[0,0x36], '>':[2,0x37], '.':[0,0x37], '?':[2,0x38],
        '/':[0,0x38], '_':[2,0x87], '\\':[0,0x87] }

TBL[' ']=[0,0x2C]
TBL['0']=[0,0x27] #数字(0)
for i in range(9):
    TBL[chr(i+1+48)]=[0,0x1E+i] #数字(1-9)
for i in range(26):
    TBL[chr(i+65)]=[2,0x04+i] #大文字(A-Z)
    TBL[chr(i+97)]=[0,0x04+i] #小文字(a-z)

class Windows(QMainWindow):

    serial = QtSerialPort.QSerialPort()

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(540, 300))

        #portの選択
        self.port_selector = QComboBox()
        self.port_selector.setStyleSheet('font: 20px; font-weight: bold')
        self.port_list = QtSerialPort.QSerialPortInfo.availablePorts()
        for each_port in self.port_list:
            self.port_selector.addItem(f'{each_port.portName()}: {each_port.description()}')
        self.connect_button = QPushButton('connect')
        self.connect_button.setStyleSheet('font: 20px; font-weight: bold')
        self.connect_button.clicked.connect(self.connect_push)
        
        menu_layout = QHBoxLayout()
        menu_layout.addWidget(self.port_selector, 3)
        menu_layout.addWidget(self.connect_button)
        #portの選択
        
        #ボタンの配置
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")

        self.button1.clicked.connect(self.button1_push)
        self.button1.setEnabled(False)
        self.button1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.button1.setStyleSheet('font: 28px; font-weight: bold')
        self.button2.clicked.connect(self.button2_push)
        self.button2.setEnabled(False)
        self.button2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.button2.setStyleSheet('font: 28px; font-weight: bold')
        self.button3.clicked.connect(self.button3_push)
        self.button3.setEnabled(False)
        self.button3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.button3.setStyleSheet('font: 28px; font-weight: bold')

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)

        main_layout = QVBoxLayout()
        main_layout.addLayout(menu_layout)
        main_layout.addLayout(button_layout)

        menu_widget = QWidget()
        menu_widget.setLayout(main_layout)
        
        self.setCentralWidget(menu_widget)
    
    def connect_push(self):
        self.connect_button.setEnabled(False)
        list_index = self.port_selector.currentIndex()
        
        self.serial.setPort(self.port_list[list_index])
        self.serial.setBaudRate(QtSerialPort.QSerialPort.Baud9600)
        self.serial.open(QIODevice.WriteOnly)

        self.button1.setEnabled(True)
        self.button2.setEnabled(True)
        self.button3.setEnabled(True)

    def button1_push(self):
        self.print('python -m pip install --upgrade pip')
    
    def button2_push(self):
        self.print('--cache-dir python_cache')

    def button3_push(self):
        self.print('explorer.exe .')

    def sendpacket(self,data):
        self.serial.write(bytes(data))
        time.sleep(0.01)
        #return self.ser.read(7)

    def push(self,k0,k1,k2=0,k3=0,k4=0,k5=0,k6=0):
        #print(self.port,": ",hex(k0),hex(k1))
        b=[0x57,0xAB,0x00,0x02,0x08,k0,0x00,k1,k2,k3,k4,k5,k6]
        b.append(sum(b) & 0xff)
        self.sendpacket(b)
        b=[0x57,0xAB,0x00,0x02,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x0c]
        self.sendpacket(b)

    def print(self,st):
        if len(st)<1:
            return
        for x in st:
            if(x in TBL):
                dat=TBL[x]
                self.push(dat[0],dat[1])

    def write(self,k):
        if(k in TBL): #通常キーの場合
            dat=TBL[k]
            self.push(dat[0],dat[1])
        if(k in SPK): #特殊(装飾)キーの場合
            if(k==SHIFT):
                self.push(0x02,0)
                return
            if(k==CTRL):
                self.push(0x01,0)
                return
            self.push(0x00,k)

if __name__ == "__main__":
    app = QApplication([])
    ex = Windows()
    ex.show()
    app.exec()
