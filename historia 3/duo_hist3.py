#É necessario instalar via terminal as bibliotecas: pip install pyautogui pillow mouseinfo
import pyautogui
from time import sleep

def clica(img):
    if img!=None:
        pyautogui.click(img)

procurar = "sim"
while procurar == "sim":

    #Uma Coisa
    img = pyautogui.locateCenterOnScreen('historia 3/UmaCoisa.png', confidence=0.9)
    clica(img)    

    #leitura +5 xp
    img = pyautogui.locateCenterOnScreen('historia 3/Leitura5XP.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)
 
    #Nao eh isso
    img = pyautogui.locateCenterOnScreen('historia 3/Nao eh isso.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)

    #My salad
    img = pyautogui.locateCenterOnScreen('historia 3/My salad.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)

    #For my coffee
    img = pyautogui.locateCenterOnScreen('historia 3/For my coffee.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)

    #Here
    img = pyautogui.locateCenterOnScreen('historia 3/Here.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)

    #Is
    img = pyautogui.locateCenterOnScreen('historia 3/Is.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)

    #Some
    img = pyautogui.locateCenterOnScreen('historia 3/Some.png', confidence=0.9)
    clica(img)

     #continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)

    #Money
    img = pyautogui.locateCenterOnScreen('historia 3/Money.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)

    #Lin
    img = pyautogui.locateCenterOnScreen('historia 3/Lin.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)

    #Ela quer que a Lin va ao supermercado
    img = pyautogui.locateCenterOnScreen('historia 3/Lin va ao supermercado.png', confidence=0.9)
    clica(img)

    #continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)

    #Combine os pares:
    img = pyautogui.locateCenterOnScreen('historia 3/combine.png', confidence=0.9)

    if img != None:
        # Combine os pares:
        clica(img)
        for i in range(1,6):
            #ultimo continuar
            img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
            clica(img)

            # Continuar azul
            img = pyautogui.locateCenterOnScreen('historia 3/ContinuarAzul.png', confidence=0.7)
            clica(img)
            for j in range(6,11):
                img = pyautogui.locateCenterOnScreen(f'historia 3/{i}.png', confidence=0.9)
                clica(img)
                sleep(0.1)

                img = pyautogui.locateCenterOnScreen(f'historia 3/{j}.png', confidence=0.9)
                clica(img)
                sleep(0.1)

    #ultimo continuar
    img = pyautogui.locateCenterOnScreen('historia 3/Continuar.png', confidence=0.7)
    clica(img)
    
    # Continuar azul
    img = pyautogui.locateCenterOnScreen('historia 3/ContinuarAzul.png', confidence=0.7)
    clica(img)



    

           

