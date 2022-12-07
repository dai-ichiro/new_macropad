from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout, QSizePolicy, QPushButton, QWidget
from PySide6.QtGui import QIcon
from functools import partial

buttons = [
    { 'text': '10秒もどる', 'icon': './icon_black/chevrons-left', 'serialNum': 20},
    { 'text': '10秒すすむ', 'icon': './icon_black/chevrons-right', 'serialNum': 21},
    { 'text': '再生/停止', 'icon': './icon_black/play.svg', 'serialNum': 22},
    { 'text': 'フルスクリーン', 'icon': './icon_black/monitor.svg', 'serialNum': 23}
]

class Widget(QWidget):

    push_button_signal = Signal(int)

    def __init__(self) -> None:
        super().__init__()

        self.button_list = []
        for each_button in buttons:
            self.button_list.append(QPushButton())
            self.button_list[-1].setStyleSheet('font: 20px; font-weight: bold; qproperty-iconSize: 32px;')
            self.button_list[-1].setText(each_button.get('text'))
            self.button_list[-1].setIcon(QIcon(each_button.get('icon')))
            self.button_list[-1].setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            self.button_list[-1].clicked.connect(partial(self.button_push, each_button.get('serialNum')))    

        layout = QGridLayout()
        layout.addWidget(self.button_list[0], 0, 0)
        layout.addWidget(self.button_list[1], 0, 2)
        layout.addWidget(self.button_list[2], 0, 1)
        layout.addWidget(self.button_list[3], 1, 1)
        self.setLayout(layout)
    
    def button_push(self, x: int) -> None:
        self.push_button_signal.emit(x)