from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget, QSizePolicy
from functools import partial

buttons = [
    { 'text': '50', 'serialNum': 50},
    { 'text': '51', 'serialNum': 51},
    { 'text': '52', 'serialNum': 52},
    { 'text': '53', 'serialNum': 53},
    { 'text': '54', 'serialNum': 54},
    { 'text': '55', 'serialNum': 55},
    { 'text': '56', 'serialNum': 56},
    { 'text': '57', 'serialNum': 57}
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