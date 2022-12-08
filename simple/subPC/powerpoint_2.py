from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget, QSizePolicy
from functools import partial

buttons = [
    { 'text': '上揃え', 'serialNum': 10},
    { 'text': '下揃え', 'serialNum': 11},
    { 'text': '左揃え', 'serialNum': 12},
    { 'text': '右揃え', 'serialNum': 13},
    { 'text': '左右中央揃え', 'serialNum': 14},
    { 'text': '左右等間隔', 'serialNum': 15},
    { 'text': '上下中央揃え', 'serialNum': 16},
    { 'text': '上下等間隔', 'serialNum': 17}
]

class Widget(QWidget):

    push_button_signal = Signal(int)

    def __init__(self):
        super().__init__()

        self.button_list = []
        for i in range(8):
            self.button_list.append(QPushButton())
            self.button_list[-1].setStyleSheet('font: 20px; font-weight: bold;')
            self.button_list[-1].setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            
        for i, each_button in enumerate(buttons):
            self.button_list[i].setText(each_button.get('text'))
            self.button_list[i].clicked.connect(partial(self.button_push, each_button.get('serialNum')))    

        layout = QGridLayout()
        for i in range(8):
            layout.addWidget(self.button_list[i], i / 2, i % 2)
        self.setLayout(layout)
    
    def button_push(self, x: int) -> None:
        if x < 256:
            self.push_button_signal.emit(x)