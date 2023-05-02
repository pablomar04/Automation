import pyautogui
#print(pyautogui.size())
##########################
#X030 GOL TREND
reclamo = ["209496","S10","9BWAB45U1NT087484","20.04.23","16556","X030", "0010", "20.04.23","9AR","1ER SERVICIO CON CONTRATO", "X030101N", "21810","MAT-OTROS","23446"]

#X030 VIRTUS/POLO/T-CROSS
#reclamo = ["609577","S10","9BWAL5BZ2NP004950","18.04.23","12322","X030", "0010", "19.04.23","9AR","1ER SERVICIO CON CONTRATO", "X030101N", "21810","MAT-OTROS","29016"]

#X030 TAOS
#reclamo = ["414400","S10","8AWBJ6B29NA827545","20.04.23","17298","X030", "0010", "20.04.23","9AR","1ER SERVICIO CON CONTRATO", "X030101N", "25050","MAT-OTROS","37124"]

#X017 VIRTUS/POLO/T-CROSS
#reclamo = ["609584","S10","9BWDL5BZ5MP043821","19.04.23","13592","X017", "0010", "20.04.23","9AR","2DO SERVICIO CON CONTRATO", "X017101N", "27068","MAT-OTROS","31686"]

#X018 VIRTUS/POLO/T-CROSS
#reclamo = ["609586","S10","9BWDL5BZ0LP081536","19.04.23","38444","X018", "0010", "19.04.23","9AR","3ER SERVICIO CON CONTRATO", "X018101N", "20301","MAT-OTROS","24653"]

#X030 TAOS
#reclamo = ["514313","S10","8AWBJ6B2XNA819289","19.04.23","10722","X030", "0010", "19.04.23","9AR","1ER SERVICIO CON CONTRATO", "X030101N", "25050","MAT-OTROS","37124"]


##########################
#X030 V6
#reclamo = ["209500","S10","8AWDW22H9PA004074","20.04.23","10932","X030", "0010", "20.04.23","9AR","1ER SERVICIO CON CONTRATO", "X0300000", "15030","MAT-OTROS","45301"]

#X20K V6
#reclamo = ["609592","S10","8AWDW22H4NA005243","20.04.23","20378","X20K", "0010", "20.04.23","9AR","2DO SERVICIO CON CONTRATO", "X20K0000", "16700","MAT-OTROS","59374"]

#X30K V6
#reclamo = ["209478","S10","8AWDW22H1PA000360","18.04.23","30439","X30K", "0010", "18.04.23","9AR","3ER SERVICIO CON CONTRATO", "X30K0000", "27068","MAT-OTROS","70702"]

#X30K V6
#reclamo = ["514335","S10","8AWDW22H9MA002319","20.04.23","51281","X50K", "0010", "20.04.23","9AR","5to SERVICIO CON CONTRATO", "X50K0000", "15030","MAT-OTROS","45301"]

#X20K 2.0L
#reclamo = ["209492","S10","8AWDD22H0NA016391","20.04.23","23324","X20K", "0010", "20.04.23","9AR","2DO SERVICIO CON CONTRATO", "X20K0000", "16700","MAT-OTROS","48440"]

#X30K 2.0L
#reclamo = ["209485","S10","8AWDB22H5LA014042","19.04.23","29958","X30K", "0010", "19.04.23","9AR","4TO SERVICIO CON CONTRATO", "X30K0000", "27068","MAT-OTROS","75612"]

#X40K 2.0L
#reclamo = ["609599","S10","8AWDB22H2NA018147","21.04.23","44248","X40K", "0010", "21.04.23","9AR","4TO SERVICIO CON CONTRATO", "X40K0000", "13534","MAT-OTROS","45091"]

#X50K 2.0L
#reclamo = ["209474","S10","8AWDB22H5LA016809","18.04.23","51378","X50K", "0010", "18.04.23","9AR","5TO SERVICIO CON CONTRATO", "X50K0000", "15030","MAT-OTROS","39871"]


pyautogui.moveTo(150, 200, duration=1) 
pyautogui.click()
pyautogui.moveTo(150, 230) 
pyautogui.click()
pyautogui.press('Tab')
pyautogui.write(reclamo[0])
pyautogui.press('Tab')
pyautogui.write(reclamo[1])
pyautogui.moveTo(50, 275, duration=1)
pyautogui.click()
pyautogui.write(reclamo[2])
pyautogui.press('Tab', presses=3)
pyautogui.write(reclamo[3])
pyautogui.press('Tab', presses=2)

pyautogui.write(reclamo[4])
pyautogui.press('Tab', presses=4)

pyautogui.write(reclamo[5])
pyautogui.press('Tab')
pyautogui.write(reclamo[6])
pyautogui.press('Tab')
pyautogui.write(reclamo[7])
pyautogui.press('Tab', presses=3)

pyautogui.write(reclamo[8])
pyautogui.press('Tab', presses=6)

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
#CARGAR MATERIAL
pyautogui.moveTo(1220, 525, duration=1)
pyautogui.click()
pyautogui.write(reclamo[12])
pyautogui.press('enter')
pyautogui.write('MATERIALES')
pyautogui.press('enter')
pyautogui.write('1')
pyautogui.press('enter', presses=2)
pyautogui.press('down', presses=3)
pyautogui.press('enter', presses=2)
pyautogui.write(reclamo[13])
pyautogui.press('enter')
#MARCAR CAUSAL
pyautogui.moveTo(30, 565, duration=1)
pyautogui.click()
#COMPLETAR
pyautogui.moveTo(45, 60, duration=1)
#pyautogui.click()           


