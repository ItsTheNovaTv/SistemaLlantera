import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Llantera Urias')
window.geometry('800x400')

framesuperior = tk.Frame(window, bg='orange')
framelateral = tk.Frame(window, bg='lightblue')
botonMenu= tk.Button(framelateral, text='Menu', width=10).pack(side='bottom', pady=2)



label1 = ttk.Label(framesuperior, text='Llantera Urias', font=('Arial',16,'bold'),background='orange')
label1.pack(side='left', fill='both', expand=True)
boton1 = tk.Button(framelateral, text='Aceptar')
boton1.pack(side='bottom', fill='x',pady=2)
boton2= tk.Button(framelateral, text='Aceptar')
boton2.pack(side='bottom', fill='x',pady=2)

framesuperior.pack(side='top', fill='both', pady=2, padx=2)
framelateral.pack(side='left', padx=2,pady=2, fill='y')

framecontenido = tk.Frame(window,bg='lightgreen')
framecontenido.pack(side='right', fill='both', expand=True,padx=2,pady=2)
def Menu():
    botonmenu1 = tk.Button(framecontenido, text='click').pack(side='right', anchor='se')

Menu()




window.mainloop()