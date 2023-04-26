#É necessario instalar via terminal as bibliotecas: pip install pyautogui pillow mouseinfo

#para exexutar o mouseInfo no cmd
"""python
from mouseinfo import mouseInfo
mouseInfo()"""

import pyautogui
from time import sleep

def clica(img):
    sleep(0.1)
    if img!=None:
        pyautogui.click(img)

procurar = "sim"
while procurar == "sim":

    #banda de menina
    img = pyautogui.locateCenterOnScreen('duo_control2/banda de menina.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)
 
    #this band
    img = pyautogui.locateCenterOnScreen('duo_control2/this band.png', confidence=0.9)
    clica(img)

    #but
    img = pyautogui.locateCenterOnScreen('duo_control2/1 but.png', confidence=0.9)
    if img != None:
        clica(img)

        #they re
        img = pyautogui.locateCenterOnScreen('duo_control2/2 they re.png', confidence=0.8)
        clica(img)

        #all
        img = pyautogui.locateCenterOnScreen('duo_control2/3 all.png', confidence=0.8)
        clica(img)

        #such
        img = pyautogui.locateCenterOnScreen('duo_control2/4 such.png', confidence=0.8)
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
    img = pyautogui.locateCenterOnScreen('duo_control2/6 my daughter.png', confidence=0.8)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)

    #i think
    img = pyautogui.locateCenterOnScreen('duo_control2/7 i think.png', confidence=0.8)
    if img != None:
        clica(img)

        # this
        img = pyautogui.locateCenterOnScreen('duo_control2/8 this.png', confidence=0.8)
        clica(img)

        # music
        img = pyautogui.locateCenterOnScreen('duo_control2/9 music.png', confidence=0.8)
        clica(img)

        # is
        img = pyautogui.locateCenterOnScreen('duo_control2/10 is.png', confidence=0.8)
        clica(img)

        # for everyone
        img = pyautogui.locateCenterOnScreen('duo_control2/11 for everyone.png', confidence=0.7)
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
    img = pyautogui.locateCenterOnScreen('duo_control2/13 tapping.png', confidence=0.8)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)

    # tapped
    img = pyautogui.locateCenterOnScreen('duo_control2/14 tapped.png', confidence=0.8)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar.png', confidence=0.7)
    clica(img)

    #pares
    img = pyautogui.locateCenterOnScreen('duo_control2/Toque nos pares.png', confidence=0.7)
    if img != None:
        #sound
        img = pyautogui.locateCenterOnScreen('duo_control2/par 1.png', confidence=0.8)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 1 b.png', confidence=0.8)
        clica(img)

        #son
        img = pyautogui.locateCenterOnScreen('duo_control2/par 2.png', confidence=0.8)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 2 b.png', confidence=0.8)
        clica(img)

        #daughter
        img = pyautogui.locateCenterOnScreen('duo_control2/par 3.png', confidence=0.8)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 3 b.png', confidence=0.8)
        clica(img)

        #show
        img = pyautogui.locateCenterOnScreen('duo_control2/par 4.png', confidence=0.8) #igual show
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 4 b.png', confidence=0.8)
        clica(img)
        #img = pyautogui.locateCenterOnScreen('duo_control2/par 11.png', confidence=0.8) #igual show
        #clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 11 b.png', confidence=0.8)
        clica(img)

        #start
        img = pyautogui.locateCenterOnScreen('duo_control2/par 5.png', confidence=0.8)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 5 b.png', confidence=0.7)
        clica(img)

        #music
        img = pyautogui.locateCenterOnScreen('duo_control2/par 6.png', confidence=0.8)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 6 b.png', confidence=0.8)
        clica(img)

        #is watching
        img = pyautogui.locateCenterOnScreen('duo_control2/par 7.png', confidence=0.7)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 7 b.png', confidence=0.8)
        clica(img)

        #practice
        img = pyautogui.locateCenterOnScreen('duo_control2/par 8.png', confidence=0.7)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 8 b.png', confidence=0.8)
        clica(img)

        #songs
        img = pyautogui.locateCenterOnScreen('duo_control2/par 9.png', confidence=0.8)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 9 b.png', confidence=0.8)
        clica(img)

        #signed
        img = pyautogui.locateCenterOnScreen('duo_control2/par 10.png', confidence=0.8)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 10 b.png', confidence=0.8)
        clica(img)

        #arms
        img = pyautogui.locateCenterOnScreen('duo_control2/par 12.png', confidence=0.8)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 12 b.png', confidence=0.8)
        clica(img)

        #foot
        img = pyautogui.locateCenterOnScreen('duo_control2/par 13.png', confidence=0.8)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 13 b.png', confidence=0.7)
        clica(img)

        #dancers
        img = pyautogui.locateCenterOnScreen('duo_control2/par 14.png', confidence=0.8)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 14 b.png', confidence=0.8)
        clica(img)

        #band
        img = pyautogui.locateCenterOnScreen('duo_control2/par 15.png', confidence=0.7)
        clica(img)
        img = pyautogui.locateCenterOnScreen('duo_control2/par 15 b.png', confidence=0.8)
        clica(img)

    #fecha propaganda
    img = pyautogui.locateCenterOnScreen('duo_control2/fecha propaganda.png', confidence=0.7)
    clica(img)

    #fecha propaganda 2
    img = pyautogui.locateCenterOnScreen('duo_control2/fecha propaganda 2.png', confidence=0.9)
    clica(img)

    #continuar azul
    img = pyautogui.locateCenterOnScreen('duo_control2/continuar azul.png', confidence=0.7)
    clica(img)

   