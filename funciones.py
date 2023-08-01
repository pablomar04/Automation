import pyautogui
from datos import *


def completar_hoja1(tipo, reclamo):
    position = pyautogui.locateCenterOnScreen('cc.png', confidence=0.8)
    pyautogui.click(position)
    position = pyautogui.locateCenterOnScreen('numero.png', confidence=0.8)
    pyautogui.click(position)
    pyautogui.press('Tab')
    pyautogui.write(reclamo["orden"])
    pyautogui.press('Tab')
    pyautogui.write(tipo)

    position = pyautogui.locateCenterOnScreen('bastidor.png', confidence=0.8)
    pyautogui.click(position)

    pyautogui.write(reclamo["chasis"], interval=0.05)

    position = pyautogui.locateCenterOnScreen('recepcion.png', confidence=0.8)
    pyautogui.click(position)

    pyautogui.write(reclamo["recepcion"])
    pyautogui.press('Tab', presses=2)
    pyautogui.write(reclamo["kilometraje"])

    position = pyautogui.locateCenterOnScreen('at.png', confidence=0.8)
    pyautogui.click(position)

    codigo = reclamo["codigo"]

    if tipo == 'S10':
        pyautogui.write(codigos_contratos[codigo][0])
    elif tipo == '11M':
        pyautogui.write(codigos_mo[codigo][0])
    pyautogui.press('Tab')
    pyautogui.write('0010')
    pyautogui.press('Tab')
    pyautogui.write(reclamo["reparacion"])

    position = pyautogui.locateCenterOnScreen('proveedor.png', confidence=0.8)
    pyautogui.click(position)

    pyautogui.write('9AR')
    
    position = pyautogui.locateCenterOnScreen('comentarios.png', confidence=0.8)
    pyautogui.click(position)
    
    if tipo == 'S10':
        pyautogui.write(codigos_contratos[codigo][2])
    elif tipo == '11M':
        pyautogui.write(codigos_mo[codigo][2])
