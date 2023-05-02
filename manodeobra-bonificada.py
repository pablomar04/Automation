import pyautogui
#print(pyautogui.size())
##########################
#NAFTA

#X017 MOB
reclamo = ["414459","11M","9BWAB45U4MT114076","26.04.23","20559","X017", "0010", "26.04.23","9AR","SERVICIO MANO DE OBRA BONIFICADA", "X017101N", "27068"]

#X018 MOB
#reclamo = ["414456","11M","9BWDL5BZ6LP120355","26.04.23","46305","X018", "0010", "26.04.23","9AR","SERVICIO MANO DE OBRA BONIFICADA", "X018101N", "20301"]

#X018 MOB-UP
#reclamo = ["209496","11M","9BWAB45U1NT087484","20.04.23","30003","X018", "0010", "21.04.23","9AR","SERVICIO MANO DE OBRA BONIFICADA", "X018101N", "13534"]

##########################
#DIESEL
# X20K MOB
#reclamo = ["609598","11M","8AWDD22H0NA020912","21.04.23","30003","X20K", "0010", "21.04.23","9AR","SERVICIO MANO DE OBRA BONIFICADA", "X20K101D", "16241"]

# X30K MOB 
#reclamo = ["609595","11M","8AWDB22H4MA013479","20.04.23","41987","X30K", "0010", "20.04.23","9AR","SERVICIO MANO DE OBRA BONIFICADA", "X30K101D", "27068"]

##########################
# AMAROK
# X30K MOB
#reclamo = ["414444","11M","8AWDB22H3MA024098","25.04.23","30295","X30K", "0010", "25.04.23","9AR","SERVICIO MANO DE OBRA BONIFICADA", "X30K111D", "27068"]

# X40K MOB 
#reclamo = ["609595","11M","8AWDB22H4MA013479","20.04.23","41987","X40K", "0010", "20.04.23","9AR","SERVICIO MANO DE OBRA BONIFICADA", "X40K111D", "13534"]




pyautogui.moveTo(150, 200, duration=1) 
pyautogui.click()
pyautogui.moveTo(150, 230, duration=1) 
pyautogui.click()
pyautogui.press('Tab')
pyautogui.write(reclamo[0])
pyautogui.press('Tab')
pyautogui.write(reclamo[1])
pyautogui.moveTo(50, 275, duration=1)
pyautogui.click()
pyautogui.write(reclamo[2])
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.write(reclamo[3])
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.write(reclamo[4])
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.write(reclamo[5])
pyautogui.press('Tab')
pyautogui.write(reclamo[6])
pyautogui.press('Tab')
pyautogui.write(reclamo[7])
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.write(reclamo[8])
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.write(reclamo[9])
#CARGAR MANO DE OBRA
pyautogui.moveTo(400, 95, duration=1)
pyautogui.click()
pyautogui.moveTo(1220, 120, duration=1)
pyautogui.click()
pyautogui.write(reclamo[10])
pyautogui.press('enter')
pyautogui.write(reclamo[11])
pyautogui.press('enter')
pyautogui.moveTo(30, 170, duration=1)
pyautogui.click()
pyautogui.moveTo(45, 60, duration=1)
#pyautogui.click()


