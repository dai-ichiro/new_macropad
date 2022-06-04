from PySide6 import QtSerialPort
from PySide6.QtCore import Qt, QSize, Slot, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget, QToolButton, QStatusBar, QStackedWidget
from PySide6.QtGui import QIcon

from youtube import YoutubeWidge
from powerpoint import PowerpointWidget
from keyboard import KeyboardWidge

toolbar_items = [
    { 'name': 'Menu', 'icon': './icon/menu.svg', 'widget': QWidget},
    { 'name': 'PowerPoint', 'icon': './icon/powerpoint.svg', 'widget': PowerpointWidget},
    { 'name': 'YouTube', 'icon': './icon/youtube.svg', 'widget': YoutubeWidge},
    { 'name': 'Keyboard', 'icon': './icon/pen-tool.svg', 'widget': KeyboardWidge}
]

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.serial = QtSerialPort.QSerialPort(
            'COM5', baudRate=QtSerialPort.QSerialPort.BaudRate.Baud9600)
        self.serial.open(QIODevice.OpenModeFlag.WriteOnly)
                
        self.openMenu = False
        self.setFixedSize(QSize(900, 600))

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
            self.widgetlist.append(each_item.get('widget')())

        for i, eachwidget in enumerate(self.widgetlist):
            self.stackedWidget.addWidget(eachwidget)
            if i > 0:
                eachwidget.push_button_signal.connect(self.send_serial)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        
        self.setCentralWidget(self.stackedWidget)
        
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
        
if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()