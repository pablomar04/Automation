import datos
import contratos
import manodeobrabonificada
import tkinter as tk
from datetime import datetime

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoSAGA")
        self.root.geometry("250x440")
        self.time_label = tk.Label(root, text="Tiempo restante: ")
        self.target_date = datetime(2023, 8, 31, 23, 59, 59)  # Target date and time (adjust as needed)
        
        self.ordenlabel = tk.Label(root, text='Orden')
        self.ordenlabel.pack()
        self.ordentexto = tk.Entry(root, justify = 'center')
        self.ordentexto.pack()

        self.chasislabel = tk.Label(root, text='Chasis')
        self.chasislabel.pack()
        self.chasistexto = tk.Entry(root, justify = 'center')
        self.chasistexto.pack()

        self.recepcionlabel = tk.Label(root, text='Fecha recepción')
        self.recepcionlabel.pack()
        self.recepciontexto = tk.Entry(root, justify = 'center')
        self.recepciontexto.pack()

        self.kilometrajelabel = tk.Label(root, text='Kilometraje')
        self.kilometrajelabel.pack()
        self.kilometrajetexto = tk.Entry(root, justify = 'center')
        self.kilometrajetexto.pack()

        self.reparacionlabel = tk.Label(root, text='Fecha reparación')
        self.reparacionlabel.pack()
        self.reparaciontexto = tk.Entry(root, justify = 'center')
        self.reparaciontexto.pack()

        self.codigolabel = tk.Label(root, text='Código')
        self.codigolabel.pack()
        self.codigotexto = tk.Entry(root, justify = 'center')
        self.codigotexto.pack()
        self.errorlabel = tk.Label(root)
        self.errorlabel.pack()

        self.botonreclamar = tk.Button(root, text='Reclamar', command= self.reclamar)
        self.botonreclamar.pack(pady=5)
        self.botonborrar = tk.Button(root, text='Borrar', command= self.borrar)
        self.botonborrar.pack(pady=5)

        self.time_label.pack(pady=10)#linea agregada
        

        copyright = u"\u00A9"
        self.copyrightlabel = tk.Label(root, text=copyright + " JPSOFT")
        self.copyrightlabel.pack(pady=10)

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
            self.time_label.config(text="Tiempo restante: {}".format(time_string))
            self.root.after(1000, self.update_timer)

    def show_expired_message(self):
        self.time_label.config(text="Tiempo expirado! Cerrando la app...")
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
        #controlar que ninguno es vacio
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
        
        if reclamo["codigo"] in datos.codigos_contratos:
            contratos.reclamar_contrato(reclamo)
        elif reclamo["codigo"] in datos.codigos_mo:
            manodeobrabonificada.reclamar_manodeobra(reclamo)
        else:
            self.error(self)


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    #app.time_label = tk.Label(root, text="Time remaining: --")
    #app.time_label.pack(pady=10)
    root.mainloop()

