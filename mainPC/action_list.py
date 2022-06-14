import keyboard as kb

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
            kb.write('ghp_m8h5rdj5dd98yMV9oVX4Iwge06C8EV9iy')
