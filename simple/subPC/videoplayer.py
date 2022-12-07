from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout, QSizePolicy, QPushButton, QWidget
from functools import partial

buttons = [
    { 'text': '再生', 'serialNum': 70},
    { 'text': 'フルスクリーン', 'serialNum': 71},
    { 'text': '10秒もどる', 'serialNum': 60},
    { 'text': '10秒すすむ', 'serialNum': 61},
    { 'text': '60秒もどる', 'serialNum': 62},
    { 'text': '60秒すすむ', 'serialNum': 63},
    { 'text': '前のチャプタ', 'serialNum': 64},
    { 'text': '次のチャプタ', 'serialNum': 65},
    { 'text': '遅く', 'serialNum': 66},
    { 'text': '速く', 'serialNum': 67},
    { 'text': '標準速度', 'serialNum': 68},
    { 'text': '', 'serialNum': 256},
    { 'text': '音量さげる', 'serialNum': 72},
    { 'text': '音量あげる', 'serialNum': 73},
]

class Widget(QWidget):

    push_button_signal = Signal(int)

    def __init__(self):
        super().__init__()

        self.button_list = []
        for i in range(14):
            self.button_list.append(QPushButton())
            self.button_list[-1].setStyleSheet('font: 20px; font-weight: bold;')
            self.button_list[-1].setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            
        for i, each_button in enumerate(buttons):
            self.button_list[i].setText(each_button.get('text'))
            self.button_list[i].clicked.connect(partial(self.button_push, each_button.get('serialNum')))    

        layout = QGridLayout()
        for i in range(14):
            layout.addWidget(self.button_list[i], i / 2, i % 2)
        self.setLayout(layout)
    
    def button_push(self, x: int) -> None:
        if x < 256:
            self.push_button_signal.emit(x)
