import pyautogui
from datos import *

def reclamar_contrato (reclamo):
    
    #pyautogui.moveTo(150, 200, duration=0.5)
    #pyautogui.click() 
    position = pyautogui.locateCenterOnScreen('cc.png', confidence=0.8)
    pyautogui.click(position)
    pyautogui.moveTo(150, 230) 
    pyautogui.click()
    pyautogui.press('Tab')
    pyautogui.write(reclamo["orden"])
    pyautogui.press('Tab')
    pyautogui.write('S10')
    pyautogui.moveTo(50, 275, duration=0.5)
    pyautogui.click()
    pyautogui.write(reclamo["chasis"], interval=0.05)
    pyautogui.press('Tab', presses=3)
    pyautogui.write(reclamo["recepcion"])
    pyautogui.press('Tab', presses=2)

    pyautogui.write(reclamo["kilometraje"])
    pyautogui.press('Tab', presses=4)
    codigo = reclamo["codigo"]
    pyautogui.write(codigos_contratos[codigo][0])
    pyautogui.press('Tab')
    pyautogui.write('0010')
    pyautogui.press('Tab')
    pyautogui.write(reclamo["reparacion"])
    pyautogui.press('Tab', presses=3)

    pyautogui.write('9AR')
    pyautogui.press('Tab', presses=7)
    
    pyautogui.write(codigos_contratos[codigo][2])
    #CARGAR MANO DE OBRA
    pyautogui.moveTo(400, 95, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(1220, 120, duration=0.5)
    pyautogui.click()
    pyautogui.write(codigos_contratos[codigo][1])
    pyautogui.press('enter')
    pyautogui.write(codigos_contratos[codigo][3])
    pyautogui.press('enter')
    #CARGAR MATERIAL
    pyautogui.moveTo(1220, 525, duration=0.5)
    pyautogui.click()
    pyautogui.write('MAT-OTROS')
    pyautogui.press('enter')
    pyautogui.write('MATERIALES')
    pyautogui.press('enter')
    pyautogui.write('1')
    pyautogui.press('enter', presses=2)
    pyautogui.press('down', presses=3)
    pyautogui.press('enter', presses=2)
    pyautogui.write(codigos_contratos[codigo][4])
    pyautogui.press('enter')
    #MARCAR CAUSAL
    pyautogui.moveTo(30, 565, duration=0.5)
    pyautogui.click()
    #COMPLETAR
    pyautogui.moveTo(45, 60, duration=0.5)
    #pyautogui.click()           


