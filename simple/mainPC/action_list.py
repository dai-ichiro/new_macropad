import keyboard as kb
import pyperclip

def action_do(x: int) -> None:
    match x:
        #PowerPoint settings 1
        case 0:
            kb.send('alt, n, x, h') # テキスト挿入
        case 1:
            kb.send('alt, n, p, d') # 画像挿入
        case 2:
            kb.send('alt, n, s, h') # 図形挿入

        #PowerPoint settings 2
        case 10:
            kb.send('alt, h, g, a, t')  # 上揃え
        case 11:
            kb.send('alt, h, g, a, b')  # 下揃え
        case 12:
            kb.send('alt, h, g, a, l')  # 左揃え
        case 13:
            kb.send('alt, h, g, a, r')  # 右揃え
        case 14:
            kb.send('alt, h, g, a, c')  # 左右中央揃え
        case 15:
            kb.send('alt, h, g, a, h')  # 左右等間隔
        case 16:
            kb.send('alt, h, g, a, m')  # 上下中央揃え
        case 17:
            kb.send('alt, h, g, a, v')  # 上下等間隔

        #Keyboard settings
        case 20:
            kb.write('<h2></h2>')
            kb.send('left, left, left, left, left')
        case 21:
            kb.write('<h3></h3>')
            kb.send('left, left, left, left, left')
        case 22:
            kb.write('<h4></h4>')
            kb.send('left, left, left, left, left')
        case 23:
            kb.write('</br>')
        case 24:
            kb.write('</br></br>')
        case 25:
            kb.write('python -m pip install --upgrade pip')
        case 26:
            kb.write('--cache-dir python_cache')
        case 27:
            kb.write('explorer.exe .')
        
        #PythonScript
        case 30:
            script = '''from PySide6.QtCore import Qt, Signal, Slot, QThread, QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QSlider, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout 
from PySide6.QtGui import QImage, QPixmap

class Window(QMainWindow):
    def __init__(self):
        super().__init__()    
        self.initUI()

    def initUI(self):
        None

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()
'''
            pyperclip.copy(script)
            kb.send('ctrl+v')
        
        case 31:
            script = '''import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    cv2.imshow('window', frame)   
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
'''
            pyperclip.copy(script)
            kb.send('ctrl+v')
