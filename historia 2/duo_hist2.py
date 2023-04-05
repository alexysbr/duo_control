import pyautogui
from time import sleep

def clica(img):
    if img!=None:
        pyautogui.click(img)

procurar = "sim"
while procurar == "sim":

    #um encontro
    img = pyautogui.locateCenterOnScreen('historia 2/encontro.png', confidence=0.9)
    clica(img)
    sleep(0.5)

    #leitura +5 xp
    img = pyautogui.locateCenterOnScreen('historia 2/leitura.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 2/continuar.png', confidence=0.7)
    clica(img)
 
    #a big game
    img = pyautogui.locateCenterOnScreen('historia 2/biggame.png', confidence=1)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 2/continuar.png', confidence=0.7)
    clica(img)

    #ela vai jogar futebol hoje
    img = pyautogui.locateCenterOnScreen('historia 2/ela.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 2/continuar.png', confidence=0.7)
    clica(img)

    #but
    img = pyautogui.locateCenterOnScreen('historia 2/but.png', confidence=0.9)
    clica(img)

    #my parents
    img = pyautogui.locateCenterOnScreen('historia 2/myparents.png', confidence=0.9)
    clica(img)

    #are
    img = pyautogui.locateCenterOnScreen('historia 2/are.png', confidence=0.9)
    clica(img)

    #from
    img = pyautogui.locateCenterOnScreen('historia 2/from.png', confidence=0.9)
    clica(img)

    #brazil
    img = pyautogui.locateCenterOnScreen('historia 2/brazil.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 2/continuar.png', confidence=0.7)
    clica(img)

    #deveriam ter encontrado outras pessoas
    img = pyautogui.locateCenterOnScreen('historia 2/deveriam.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 2/continuar.png', confidence=0.7)
    clica(img)

    #daniel mentiu
    img = pyautogui.locateCenterOnScreen('historia 2/danielmentiu.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 2/continuar.png', confidence=0.7)
    clica(img)

    # Combine os pares:
    img = pyautogui.locateCenterOnScreen('historia 2/combine.png', confidence=0.9)

    if img != None:
        # Combine os pares:
        clica(img)
        for i in range(1,6):
            #penultimo continuar
            img = pyautogui.locateCenterOnScreen('historia 2/continuar.png', confidence=0.7)
            clica(img)

            # Continuar azul
            img = pyautogui.locateCenterOnScreen('historia 2/continuarazul.png', confidence=0.7)
            clica(img)
            for j in range(6,11):
                img = pyautogui.locateCenterOnScreen(f'historia 2/{i}.png', confidence=0.9)
                clica(img)
                sleep(0.2)

                img = pyautogui.locateCenterOnScreen(f'historia 2/{j}.png', confidence=0.9)
                clica(img)
                sleep(0.2)

    #penultimo continuar
    img = pyautogui.locateCenterOnScreen('historia 2/continuar.png', confidence=0.7)
    clica(img)
    
    # Continuar azul
    img = pyautogui.locateCenterOnScreen('historia 2/continuarazul.png', confidence=0.7)
    clica(img)



    

           

