'''
This file does not need to be modified.
'''

from PySide6 import QtSerialPort
from PySide6.QtCore import Qt, QSize, Slot, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget, QToolButton, QStatusBar, QStackedWidget
from PySide6.QtGui import QIcon

from importlib import import_module
import yaml

with open('forms.yml', 'r') as f:
    toolbar_items = yaml.load(f, Loader=yaml.SafeLoader)

class Window(QMainWindow):

    serial = QtSerialPort.QSerialPort()

    def __init__(self):
        super().__init__()

        self.openMenu = False
        self.setFixedSize(QSize(900, 540))

        self.stackedWidget = QStackedWidget()

        self.toolbar = QToolBar()
        self.toolbar.setIconSize(QSize(36,36))
        self.toolbar.setStyleSheet("QToolBar {background: rgb(51, 51, 51); spacing: 10px;}")
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolbar)
        self.toolbar.setMovable(False)
        
        self.toolbuttons = []
        self.widgetlist = []
        for i, each_item in enumerate(toolbar_items):
            self.toolbuttons.append(QToolButton())
            self.toolbuttons[-1].setText(each_item.get('name'))
            self.toolbuttons[-1].setIcon(QIcon(each_item.get('icon')))
            self.toolbuttons[-1].Name = i
            self.toolbuttons[-1].setStyleSheet("QToolButton {color: white; font: 16px; font-weight: bold}")
            self.toolbuttons[-1].clicked.connect(self.pushToolButton)
            self.toolbar.addWidget(self.toolbuttons[-1])
            match i:
                case 0:
                    self.widgetlist.append(QWidget())
                case _:
                    script_path = each_item.get('widget')
                    self.widgetlist.append(getattr(import_module(script_path), 'Widget')())

        for i, eachwidget in enumerate(self.widgetlist):
            self.stackedWidget.addWidget(eachwidget)
            if i == 1:
                eachwidget.select_port.connect(self.openPort)
            if i > 1:
                eachwidget.push_button_signal.connect(self.send_serial)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        
        self.setCentralWidget(self.stackedWidget)

        self.stackedWidget.setCurrentIndex(1)
        
    def pushToolButton(self):

        match int(self.sender().Name):
            case 0:
                self.openMenu = not self.openMenu
                if self.openMenu == True:    
                    for each_toolbutton in self.toolbuttons:
                        each_toolbutton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
                else:
                    for each_toolbutton in self.toolbuttons:
                        each_toolbutton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
            case _:
                self.statusbar.showMessage(self.sender().text())
                self.stackedWidget.setCurrentIndex(self.sender().Name)
    
    def closeEvent(self, e):
       self.serial.close()
       e.accept()
    
    @Slot(int)
    def send_serial(self, x):
        self.serial.write(x.to_bytes(1, 'big'))
    
    @Slot(QtSerialPort.QSerialPortInfo)
    def openPort(self, x):
        self.serial.setPort(x)
        self.serial.setBaudRate(QtSerialPort.QSerialPort.Baud9600)
        self.serial.open(QIODevice.WriteOnly)
        
if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()
