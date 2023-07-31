from datos import *
from contratos import *
from manodeobrabonificada import *
import tkinter as tk
from datetime import datetime

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto-SAGA")
        self.root.geometry("230x370")

        self.ordenlabel = tk.Label(root, text='Orden')
        self.ordenlabel.pack()
        self.ordentexto = tk.Entry(root, justify = 'center')
        self.ordentexto.pack()

        chasislabel = tk.Label(root, text='Chasis')
        chasislabel.pack()
        chasistexto = tk.Entry(root, justify = 'center')
        chasistexto.pack()

        recepcionlabel = tk.Label(root, text='Fecha recepción')
        recepcionlabel.pack()
        recepciontexto = tk.Entry(root, justify = 'center')
        recepciontexto.pack()

        kilometrajelabel = tk.Label(root, text='Kilometraje')
        kilometrajelabel.pack()
        kilometrajetexto = tk.Entry(root, justify = 'center')
        kilometrajetexto.pack()

        reparacionlabel = tk.Label(root, text='Fecha reparación')
        reparacionlabel.pack()
        reparaciontexto = tk.Entry(root, justify = 'center')
        reparaciontexto.pack()



        codigolabel = tk.Label(root, text='Código')
        codigolabel.pack()
        codigotexto = tk.Entry(root, justify = 'center')
        codigotexto.pack()
        errorlabel = tk.Label(root)
        errorlabel.pack()

        

        botonreclamar = tk.Button(root, text='Reclamar', command= reclamar)
        botonreclamar.pack()
        botonborrar = tk.Button(root, text='Borrar', command= borrar)
        botonborrar.pack()

        copyright = u"\u00A9"
        copyrightlabel = tk.Label(root, text=copyright + " Juan Pablo Marcovecchio")
        copyrightlabel.pack()
        
        self.time_label = tk.Label(root, text="Time remaining: --") #Linea agregada
        
        self.target_date = datetime(2023, 12, 31, 23, 59, 59)  # Target date and time (adjust as needed)
        self.update_timer()

    def update_timer(self):
        current_date = datetime.now()
        remaining_time = self.target_date - current_date

        if remaining_time.total_seconds() <= 0:
            self.show_expired_message()
        else:
            days, seconds = remaining_time.days, remaining_time.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            time_string = "{:02d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds)
            self.time_label.config(text="Time remaining: {}".format(time_string))
            self.root.after(1000, self.update_timer)

    def show_expired_message(self):
        self.time_label.config(text="Date expired! Closing the app...")
        self.root.after(2000, self.root.destroy)  # Close the app after 2 seconds


    def borrar (self):   
        self.ordentexto.delete(0,'end')
        self.chasistexto.delete(0,'end')
        self.recepciontexto.delete(0,'end')
        self.kilometrajetexto.delete(0,'end')
        self.reparaciontexto.delete(0,'end')
        self.codigotexto.delete(0,'end')
        self.errorlabel.config(text = "")

    def error(self):
        self.errorlabel.config(text = "No existe código")
    
    def reclamar(self):
        
        orden_texto = self.ordentexto.get()
        chasis_texto = self.chasistexto.get()
        recepcion_texto = self.recepciontexto.get()
        kilometraje_texto = self.kilometrajetexto.get()
        reparacion_texto = self.reparaciontexto.get()
        codigo_texto = self.codigotexto.get()
    
        reclamo = {
            "orden":orden_texto,
            "chasis":chasis_texto,
            "recepcion":recepcion_texto,
            "kilometraje":kilometraje_texto,
            "reparacion":reparacion_texto,
            "codigo":codigo_texto
            }
        
        if reclamo["codigo"] in codigos_contratos:
            reclamar_contrato(reclamo)
        elif reclamo["codigo"] in codigos_mo:
            reclamar_manodeobra(reclamo)
        else:
            error(self)    
if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    # app.time_label = tk.Label(root, text="Time remaining: --")
    app.time_label.pack(pady=10)
    root.mainloop()
