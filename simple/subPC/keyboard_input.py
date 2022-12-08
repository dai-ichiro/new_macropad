from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout, QSizePolicy, QPushButton, QWidget
from functools import partial

buttons = [
    { 'text': '<h2></h2>', 'serialNum': 20},
    { 'text': '<h3></h3>', 'serialNum': 21},
    { 'text': '<h4></h4>', 'serialNum': 22},
    { 'text': '</br>', 'serialNum': 23},
    { 'text': '</br></br>', 'serialNum': 24},
    { 'text': 'python -m pip install --upgrade pip', 'serialNum': 25},
    { 'text': '--cache-dir python_cache', 'serialNum': 26},
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
            layout.addWidget(self.button_list[i], i % 6, i / 6)
        self.setLayout(layout)
    
    def button_push(self, x: int) -> None:
        self.push_button_signal.emit(x)
