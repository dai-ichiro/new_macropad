import pyautogui as pg
import pyperclip as clip

def action_do(x: int) -> None:
    match x:
        #PowerPoint settings
        case 0:
            pg.press(['alt', 'n', 'x', 'h'])
        case 1:
            pg.press(['alt', 'n', 'p', 'd'])
        case 2:
            pg.press(['alt', 'n', 's', 'h']) 
        case 3:
            pg.press(['alt', 'h', 'g', 'a', 't'])
        case 4:
            pg.press(['alt', 'h', 'g', 'a', 'l'])
        case 5:
            pg.press(['alt', 'h', 'g', 'a', 'r'])
        case 6:
            pg.press(['alt', 'h', 'g', 'a', 'b'])
        case 7:
            pg.press(['alt', 'h', 'g', 'a', 'c'])
        case 8:
            pg.press(['alt', 'h', 'g', 'a', 'm'])
        case 9:
            pg.press(['alt', 'h', 'g', 'a', 'h'])
        case 10:
            pg.press(['alt', 'h', 'g', 'a', 'v'])

        #YouTube Settings
        case 20:
            pg.press('j')
        case 21:
            pg.press('l')
        case 22:
            pg.press('k')
        case 23:
            pg.press('f')

        #Keyboard settings
        case 40:
            pg.write('<h2></h2>')
            pg.press(['left', 'left', 'left', 'left', 'left'])
        case 41:
            pg.write('<h3></h3>')
            pg.press(['left', 'left', 'left', 'left', 'left'])
        case 42:
            pg.write('<h4></h4>')
            pg.press(['left', 'left', 'left', 'left', 'left'])
        case 43:
            pg.write('</br>')
        case 44:
            pg.write('</br></br>')
        case 45:
            pg.write('<a href=""></a>')
            pg.press(['left', 'left', 'left', 'left', 'left', 'left'])
        case 46:
            pg.write('python -m pip install --upgrade pip')
        case 47:
            pg.write('--cache-dir python_cache')
        case 48:
            clip.copy('pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu113')
            pg.hotkey('ctrl', 'v')
        case 49:
            pg.write('abc_abc_abc')
            