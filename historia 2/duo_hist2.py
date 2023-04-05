import pyautogui
from time import sleep

def clica(img):
    if img!=None:
        pyautogui.click(img)

procurar = "sim"
while procurar == "sim":

    #um encontro
    img = pyautogui.locateCenterOnScreen('encontro.png', confidence=0.9)
    clica(img)
    sleep(0.5)

    #leitura +5 xp
    img = pyautogui.locateCenterOnScreen('leitura.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('continuar.png', confidence=0.7)
    clica(img)
 
    #a big game
    img = pyautogui.locateCenterOnScreen('biggame.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('continuar.png', confidence=0.7)
    clica(img)

    #ela vai jogar futebol hoje
    img = pyautogui.locateCenterOnScreen('ela.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('continuar.png', confidence=0.7)
    clica(img)

    #but
    img = pyautogui.locateCenterOnScreen('but.png', confidence=0.9)
    clica(img)

    #my parents
    img = pyautogui.locateCenterOnScreen('myparents.png', confidence=0.9)
    clica(img)

    #are
    img = pyautogui.locateCenterOnScreen('are.png', confidence=0.9)
    clica(img)

    #from
    img = pyautogui.locateCenterOnScreen('from.png', confidence=0.7)
    clica(img)

    #brazil
    img = pyautogui.locateCenterOnScreen('brazil.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('continuar.png', confidence=0.7)
    clica(img)

    #deveriam ter encontrado outras pessoas
    img = pyautogui.locateCenterOnScreen('deveriam.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('continuar.png', confidence=0.7)
    clica(img)

    #daniel mentiu
    img = pyautogui.locateCenterOnScreen('danielmentiu.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('continuar.png', confidence=0.7)
    clica(img)

    # Combine os pares:
    img = pyautogui.locateCenterOnScreen('combine.png', confidence=0.9)

    if img != None:
        # Combine os pares:
        clica(img)
        for i in range(1,6):
            #penultimo continuar
            img = pyautogui.locateCenterOnScreen('continuar.png', confidence=0.7)
            clica(img)

            # Continuar azul
            img = pyautogui.locateCenterOnScreen('continuarazul.png', confidence=0.7)
            clica(img)
            for j in range(6,11):
                img = pyautogui.locateCenterOnScreen(f'{i}.png', confidence=0.9)
                clica(img)
                sleep(0.2)

                img = pyautogui.locateCenterOnScreen(f'{j}.png', confidence=0.9)
                clica(img)
                sleep(0.2)

    #penultimo continuar
    img = pyautogui.locateCenterOnScreen('continuar.png', confidence=0.7)
    clica(img)
    
    # Continuar azul
    img = pyautogui.locateCenterOnScreen('continuarazul.png', confidence=0.7)
    clica(img)



    

           

