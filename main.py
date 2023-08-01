import datos
import contratos
import manodeobrabonificada
import tkinter

def borrar ():   
    ordentexto.delete(0,'end')
    chasistexto.delete(0,'end')
    recepciontexto.delete(0,'end')
    kilometrajetexto.delete(0,'end')
    reparaciontexto.delete(0,'end')
    codigotexto.delete(0,'end')
    errorlabel.config(text = "")

def error():
    errorlabel.config(text = "No existe código")

def reclamar():
    #controlar que ninguno es vacio
    orden_texto = ordentexto.get()
    chasis_texto = chasistexto.get()
    recepcion_texto = recepciontexto.get()
    kilometraje_texto = kilometrajetexto.get()
    reparacion_texto =reparaciontexto.get()
    codigo_texto = codigotexto.get()

    reclamo = {
        "orden":orden_texto,
        "chasis":chasis_texto,
        "recepcion":recepcion_texto,
        "kilometraje":kilometraje_texto,
        "reparacion":reparacion_texto,
        "codigo":codigo_texto
        }
    
    if reclamo["codigo"] in datos.codigos_contratos:
        contratos.reclamar_contrato(reclamo)
    elif reclamo["codigo"] in datos.codigos_mo:
        manodeobrabonificada.reclamar_manodeobra(reclamo)
    else:
        error()



ventana = tkinter.Tk()
ventana.geometry("230x370")
ventana.title('Auto-SAGA')

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
errorlabel = tkinter.Label(ventana)
errorlabel.pack()

botonreclamar = tkinter.Button(ventana, text='Reclamar', command= reclamar)
botonreclamar.pack()
botonborrar = tkinter.Button(ventana, text='Borrar', command= borrar)
botonborrar.pack()

copyright = u"\u00A9"
copyrightlabel = tkinter.Label(ventana, text=copyright + " Juan Pablo Marcovecchio")
copyrightlabel.pack()

ventana.mainloop()







