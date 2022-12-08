import keyboard as kb
import pyperclip

def action_do(x: int) -> None:
    match x:
        #PowerPoint settings
        case 0:
            kb.send('alt, n, x, h')
        case 1:
            kb.send('alt, n, p, d')
        case 2:
            kb.send('alt, n, s, h')
        case 3:
            kb.send('alt, h, g, a, t')
        case 4:
            kb.send('alt, h, g, a, l')
        case 5:
            kb.send('alt, h, g, a, r')
        case 6:
            kb.send('alt, h, g, a, b')
        case 7:
            kb.send('alt, h, g, a, c')
        case 8:
            kb.send('alt, h, g, a, m')
        case 9:
            kb.send('alt, h, g, a, h')
        case 10:
            kb.send('alt, h, g, a, v')

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
