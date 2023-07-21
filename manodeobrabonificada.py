import pyautogui
from datos import *

def reclamar_manodeobra (reclamo):
    position = pyautogui.locateCenterOnScreen('cc.png', confidence=0.8)
    pyautogui.click(position)
    position = pyautogui.locateCenterOnScreen('numero.png', confidence=0.8)
    pyautogui.click(position)
    pyautogui.press('Tab')
    pyautogui.write(reclamo["orden"])
    pyautogui.press('Tab')
    pyautogui.write('11M')

    position = pyautogui.locateCenterOnScreen('bastidor.png', confidence=0.8)
    pyautogui.click(position)

    pyautogui.write(reclamo["chasis"],interval=0.05)

    position = pyautogui.locateCenterOnScreen('recepcion.png', confidence=0.8)
    pyautogui.click(position)

    pyautogui.write(reclamo["recepcion"])
    pyautogui.press('Tab', presses=2)
    pyautogui.write(reclamo["kilometraje"])


    position = pyautogui.locateCenterOnScreen('at.png', confidence=0.8)
    pyautogui.click(position)

    codigo = reclamo["codigo"]

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

    pyautogui.write(codigos_mo[codigo][2])

    #CARGAR MANO DE OBRA
    position = pyautogui.locateCenterOnScreen('tercero.png', confidence=0.8)
    pyautogui.click(position)

    position = pyautogui.locateCenterOnScreen('e1.png', confidence=0.8)
    pyautogui.click(position)

    pyautogui.write(codigos_mo[codigo][1])
    pyautogui.press('enter')
    pyautogui.write(codigos_mo[codigo][3])
    pyautogui.press('enter')

    #MARCAR CAUSAL
    position = pyautogui.locateCenterOnScreen('causal2.png', confidence=0.9)
    pyautogui.click(position)
    #COMPLETAR
    position = pyautogui.locateCenterOnScreen('completar.png', confidence=0.8)
    pyautogui.moveTo(position)


