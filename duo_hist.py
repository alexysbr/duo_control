#É necessario instalar via terminal as bibliotecas: pip install pyautogui pillow mouseinfo
import pyautogui
from time import sleep

def clica(img):
    if img!=None:
        pyautogui.click(img)

procurar = "sim"
while procurar == "sim":

    #bom dia
    img = pyautogui.locateCenterOnScreen('BomDia.png', confidence=0.9)
    clica(img)
    

    #leitura +5 xp
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 160300.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132345.png', confidence=0.7)
    clica(img)
 
    #sim isso mesmo
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-02 002615.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132345.png', confidence=0.7)
    clica(img)

    # I
    img = pyautogui.locateCenterOnScreen('1Captura de tela 2023-04-01 131634.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132345.png', confidence=0.7)
    clica(img)

    # need the
    img = pyautogui.locateCenterOnScreen('2Captura de tela 2023-04-01 131706.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132345.png', confidence=0.7)
    clica(img)

    # key
    img = pyautogui.locateCenterOnScreen('3Captura de tela 2023-04-01 131749.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132345.png', confidence=0.7)
    clica(img)

    # to my car
    img = pyautogui.locateCenterOnScreen('4Captura de tela 2023-04-01 131822.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132345.png', confidence=0.7)
    clica(img)

    # tired
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 184404.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132345.png', confidence=0.7)
    clica(img)

    # Procurando um pouco de acucar para o cafe dela
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 131929.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132345.png', confidence=0.7)
    clica(img)

    # ...ela colocou sal no cafe dela
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132008.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132345.png', confidence=0.7)
    clica(img)

    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 192511.png', confidence=0.9)

    if img != None:
        # Combine os pares:
        clica(img)
        for i in range(1,6):
            #ultimo continuar
            img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 193900.png', confidence=0.7)
            clica(img)

            # Continuar azul
            img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132543.png', confidence=0.7)
            clica(img)
            for j in range(6,11):
                img = pyautogui.locateCenterOnScreen(f'{i}.png', confidence=0.9)
                clica(img)
                sleep(0.1)

                img = pyautogui.locateCenterOnScreen(f'{j}.png', confidence=0.9)
                clica(img)
                sleep(0.1)

    #ultimo continuar
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 193900.png', confidence=0.7)
    clica(img)
    
    # Continuar azul
    img = pyautogui.locateCenterOnScreen('Captura de tela 2023-04-01 132543.png', confidence=0.7)
    clica(img)



    

           

