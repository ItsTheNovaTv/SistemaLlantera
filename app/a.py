import tkinter as tk
colorbanner = '#2b2d42'
window = tk.Tk()
window.title('Llantera Urias')
window.geometry('1280x720')  
separacionx = 6
separacion=8



color1 = tk.Label(window, bg=colorbanner, height=2)
color1.grid(row=0, column=0, columnspan=2, sticky="we")
lblID= tk.Label(window, text='ID: ')
lblID.grid(padx=separacionx, pady=separacion,row=1,column=0)
lblMarca= tk.Label(window, text='Marca: ')
lblMarca.grid(padx=separacionx, pady=separacion,row=2,column=0)
lblMedida = tk.Label(window, text='Medida: ')
lblMedida.grid(padx=separacionx, pady=separacion,row=3,column=0)
lblDisponible= tk.Label(window,text='Disponible: ')
lblDisponible.grid(padx=separacionx,pady=separacion, row=4,column=0)

color2 = tk.Label(window, bg=colorbanner, height=2)
color2.grid(row=0, column=1, columnspan=2, sticky="we")    
entID= tk.Entry(window)
entID.grid(padx=separacionx, pady=separacion,row=1,column=1)
entMarca = tk.Entry(window)
entMarca.grid(padx=separacionx,pady=separacion, row=2,column=1)
entMedida= tk.Entry(window)
entMedida.grid(padx=separacionx,pady=separacion, row=3,column=1)
entDisponible = tk.Entry(window)
entDisponible.grid(padx=separacionx,pady=separacion, row=4,column=1)
def obtener_datos():
    print(entID.get())
btn = tk.Button(window, command=obtener_datos, text='boton').grid(row=5, column=1)

window.mainloop()