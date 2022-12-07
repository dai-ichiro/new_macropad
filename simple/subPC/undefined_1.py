from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget, QSizePolicy
from functools import partial

buttons = [
    { 'text': '40', 'serialNum': 40},
    { 'text': '41', 'serialNum': 41},
    { 'text': '42', 'serialNum': 42},
    { 'text': '43', 'serialNum': 43},
    { 'text': '44', 'serialNum': 44},
    { 'text': '45', 'serialNum': 45},
    { 'text': '46', 'serialNum': 46},
    { 'text': '47', 'serialNum': 47}
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