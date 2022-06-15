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

        #YouTube Settings
        case 20:
            kb.send('j')
        case 21:
            kb.send('l')
        case 22:
            kb.send('k')
        case 23:
            kb.send('f')

        #Keyboard settings
        case 40:
            kb.write('<h2></h2>')
            kb.send('left, left, left, left, left')
        case 41:
            kb.write('<h3></h3>')
            kb.send('left, left, left, left, left')
        case 42:
            kb.write('<h4></h4>')
            kb.send('left, left, left, left, left')
        case 43:
            kb.write('</br>')
        case 44:
            kb.write('</br></br>')
        case 45:
            kb.write('<a href=""></a>')
            kb.send('left, left, left, left, left, left')
        case 46:
            kb.write('python -m pip install --upgrade pip')
        case 47:
            kb.write('--cache-dir python_cache')
        case 48:
            kb.write('pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu113')
        case 49:
            kb.write('ghp_m8h0rdy6gfu8hfwge06C8EV9iy')
        
        #video player
        case 60:
            kb.send('left')
        case 61:
            kb.send('right')
        case 62:
            kb.send('num lock, shift+left, num lock')
        case 63:
            kb.send('num lock, shift+right, num lock')
        case 64:
            kb.send('ctrl+p')
        case 65:
            kb.send('ctrl+n')
        case 66:
            kb.send(',')
        case 67:
            kb.send('.')
        case 68:
            kb.send('shift+l')
        case 70:
            kb.send('k')
        case 71:
            kb.send('f')
        case 72:
            kb.send('down')
        case 73:
            kb.send('up')
        
        #OBS
        case 80:
            kb.send('ctrl+1')
        case 81:
            kb.send('ctrl+f')
        case 82:
            kb.send('ctrl+2')
        
        #PythonScript
        case 100:
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
        
        case 101:
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
