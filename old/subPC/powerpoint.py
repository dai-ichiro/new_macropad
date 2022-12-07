from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QSizePolicy
from PySide6.QtGui import QIcon
from functools import partial

buttons = [
    { 'text': 'テキスト挿入', 'icon': './icon_black/edit.svg', 'serialNum': 0},
    { 'text': '画像挿入', 'icon': './icon_black/image.svg', 'serialNum': 1},
    { 'text': '図形挿入', 'icon': './icon_black/insertfig.svg', 'serialNum': 2},
    { 'text': '上揃え', 'serialNum': 3},
    { 'text': '左揃え', 'serialNum': 4},
    { 'text': '右揃え', 'serialNum': 5},
    { 'text': '下揃え', 'serialNum': 6},
    { 'text': '左右中央揃え', 'icon': './icon_black/centeralignment_v.svg', 'serialNum': 7},
    { 'text': '上下中央揃え', 'icon': './icon_black/centeralignment_h.svg', 'serialNum': 8},
    { 'text': '左右等間隔', 'icon': './icon_black/equal_h.svg', 'serialNum': 9},
    { 'text': '上下等間隔', 'icon': './icon_black/equal_v.svg', 'serialNum': 10}
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
        
        mainlayout = QVBoxLayout()

        upperlayout = QHBoxLayout()

        upperleftlayout = QGridLayout()
        upperleftlayout.addWidget(self.button_list[3], 0, 1)
        upperleftlayout.addWidget(self.button_list[4], 1, 0)
        upperleftlayout.addWidget(self.button_list[5], 1, 2)
        upperleftlayout.addWidget(self.button_list[6], 2, 1)

        upperrightlayout = QVBoxLayout()
        upperrightlayout.addWidget(self.button_list[7])
        upperrightlayout.addWidget(self.button_list[8])
        upperrightlayout.addWidget(self.button_list[9])
        upperrightlayout.addWidget(self.button_list[10])
        
        upperlayout.addLayout(upperleftlayout)
        upperlayout.addLayout(upperrightlayout)

        lowerlayout = QHBoxLayout()
        lowerlayout.addWidget(self.button_list[0])
        lowerlayout.addWidget(self.button_list[1])
        lowerlayout.addWidget(self.button_list[2])

        mainlayout.addLayout(upperlayout, 7)
        mainlayout.addLayout(lowerlayout, 3)

        self.setLayout(mainlayout)
    
    def button_push(self, x: int) -> None:
        self.push_button_signal.emit(x)