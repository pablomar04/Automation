import pyautogui

def reclamar_manodeobra (reclamo):
    pyautogui.moveTo(150, 200, duration=1) 
    pyautogui.click()
    pyautogui.moveTo(150, 230, duration=1) 
    pyautogui.click()
    pyautogui.press('Tab')
    pyautogui.write(reclamo[0])
    pyautogui.press('Tab')
    pyautogui.write('11M')
    pyautogui.moveTo(50, 275, duration=1)
    pyautogui.click()
    pyautogui.write(reclamo[1])
    pyautogui.press('Tab', presses=3)
    pyautogui.write(reclamo[2])
    pyautogui.press('Tab', presses=2)
    pyautogui.write(reclamo[3])
    pyautogui.press('Tab', presses=4)
    pyautogui.write(reclamo[5][0])
    pyautogui.press('Tab')
    pyautogui.write('0010')
    pyautogui.press('Tab')
    pyautogui.write(reclamo[4])
    pyautogui.press('Tab', presses=3)
    pyautogui.write('9AR')
    pyautogui.press('Tab', presses=6)
    pyautogui.write(reclamo[5][2])
    #CARGAR MANO DE OBRA
    pyautogui.moveTo(400, 95, duration=1)
    pyautogui.click()
    pyautogui.moveTo(1220, 120, duration=1)
    pyautogui.click()
    pyautogui.write(reclamo[5][1])
    pyautogui.press('enter')
    pyautogui.write(reclamo[5][3])
    pyautogui.press('enter')
    pyautogui.moveTo(30, 170, duration=1)
    pyautogui.click()
    pyautogui.moveTo(45, 60, duration=1)
    #pyautogui.click()

