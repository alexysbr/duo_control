#É necessario instalar via terminal as bibliotecas: pip install pyautogui pillow mouseinfo
import pyautogui
from time import sleep

def clica(img):
    if img!=None:
        pyautogui.click(img)

procurar = "sim"
while procurar == "sim":

    #banda de menina
    img = pyautogui.locateCenterOnScreen('duo_control2/banda de menina.png', confidence=0.9)
    clica(img)
    sleep(0.5)

    """#continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)
 
    #but
    img = pyautogui.locateCenterOnScreen('duo_control2/1 but.png', confidence=0.9)
    clica(img)

    #they re
    img = pyautogui.locateCenterOnScreen('duo_control2/2 they re.png', confidence=0.9)
    clica(img)

    #all
    img = pyautogui.locateCenterOnScreen('duo_control2/3 all.png', confidence=0.9)
    clica(img)

    #such
    img = pyautogui.locateCenterOnScreen('duo_control2/4 such.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)

    # with junior
    img = pyautogui.locateCenterOnScreen('duo_control2/5 with junior.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)

    #my daughter
    img = pyautogui.locateCenterOnScreen('duo_control2/6 my daughter.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)

    #i think
    img = pyautogui.locateCenterOnScreen('duo_control2/7 i think.png', confidence=0.9)
    clica(img)

    # this
    img = pyautogui.locateCenterOnScreen('duo_control2/8 this.png', confidence=0.9)
    clica(img)

    # music
    img = pyautogui.locateCenterOnScreen('duo_control2/9 music.png', confidence=0.9)
    clica(img)

    # is
    img = pyautogui.locateCenterOnScreen('duo_control2/10 is.png', confidence=0.9)
    clica(img)

    # for everyone
    img = pyautogui.locateCenterOnScreen('duo_control2/11 for everyone.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)

    # mine too
    img = pyautogui.locateCenterOnScreen('duo_control2/12 mine too.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)

    # tapping
    img = pyautogui.locateCenterOnScreen('duo_control2/13 tapping.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)

    # tapped
    img = pyautogui.locateCenterOnScreen('duo_control2/14 tapped.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)

"""