from datos import *
from contratos import *
from manodeobrabonificada import *
import tkinter

ventana = tkinter.Tk()
ventana.geometry("250x300")
ventana.title('Auto-SAGA')

#etiqueta = tkinter.Label(ventana, text="Auto-SAGA")
#etiqueta.pack()
def imprimir (cadena):
    print(cadena)
def borrar ():   
    ordentexto.delete(0,'end')
    chasistexto.delete(0,'end')
    recepciontexto.delete(0,'end')
    kilometrajetexto.delete(0,'end')
    reparaciontexto.delete(0,'end')
    codigotexto.delete(0,'end')

ordenlabel = tkinter.Label(ventana, text='Orden')
ordenlabel.pack()
ordentexto = tkinter.Entry(ventana, justify = 'center')
ordentexto.pack()

chasislabel = tkinter.Label(ventana, text='Chasis')
chasislabel.pack()
chasistexto = tkinter.Entry(ventana, justify = 'center')
chasistexto.pack()

recepcionlabel = tkinter.Label(ventana, text='Fecha recepción')
recepcionlabel.pack()
recepciontexto = tkinter.Entry(ventana, justify = 'center')
recepciontexto.pack()

kilometrajelabel = tkinter.Label(ventana, text='Kilometraje')
kilometrajelabel.pack()
kilometrajetexto = tkinter.Entry(ventana, justify = 'center')
kilometrajetexto.pack()

reparacionlabel = tkinter.Label(ventana, text='Fecha reparación')
reparacionlabel.pack()
reparaciontexto = tkinter.Entry(ventana, justify = 'center')
reparaciontexto.pack()

codigolabel = tkinter.Label(ventana, text='Código')
codigolabel.pack()
codigotexto = tkinter.Entry(ventana, justify = 'center')
codigotexto.pack()

botonreclamar = tkinter.Button(ventana, text='Reclamar', command= lambda: imprimir(codigotexto.get()))
botonreclamar.pack()
botonborrar = tkinter.Button(ventana, text='Borrar', command= borrar)
botonborrar.pack()


reclamo = {"orden":ordentexto,
           "chasis":chasistexto,
           "recepcion":recepciontexto,
           "kilometraje":kilometrajetexto,
           "reparacion":reparaciontexto,
           "codigo":codigotexto}


ventana.mainloop()

#reclamo = ["209568","8AWDW22H5PA014889","02.05.23","10003","02.05.23",a11]


#reclamar_contrato(reclamo)
#reclamar_manodeobra(reclamo)







