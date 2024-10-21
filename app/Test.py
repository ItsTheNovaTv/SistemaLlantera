import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def inventario():
    limpiar_frame(framecontenido)
    Tabla = ttk.Treeview(framecontenido)
    Tabla.pack()
def limpiar_frame(frame):
    """Función para limpiar todos los widgets de un frame."""
    for widget in frame.winfo_children():
        widget.destroy()

def mostrar_menu():
    """Función para mostrar un mensaje en el frame de contenido."""
    limpiar_frame(framecontenido)  # Limpiar el frame antes de agregar un nuevo mensaje
    label_mensaje = tk.Label(framecontenido, text="Widgets Menu!", bg='lightgreen')
    label_mensaje.pack(pady=20)

# Configuración de la ventana principal
window = tk.Tk()
window.title('Llantera Urias')
window.geometry('800x500')
# Ruta de la imagen
ruta_imagen_btnrueda = os.path.join(os.path.dirname(__file__), 'Assets/images/rueda.png')

# Intentar cargar la imagen
try:
    imagen = Image.open(ruta_imagen_btnrueda)
    imagen = imagen.resize((90, 90), Image.LANCZOS)
    imagenrueda = ImageTk.PhotoImage(imagen)
except FileNotFoundError:
    print(f"Error: no se puede encontrar el archivo en la ruta {ruta_imagen_btnrueda}")
    imagenrueda = None


ruta_imagen_btnproveedor = os.path.join(os.path.dirname(__file__), 'Assets/images/proveedor.png')
try:
    imagen = Image.open(ruta_imagen_btnproveedor)
    imagen = imagen.resize((90, 90), Image.LANCZOS)
    imagenproveedor = ImageTk.PhotoImage(imagen)
except FileNotFoundError:
    print(f"Error: no se puede encontrar el archivo en la ruta {ruta_imagen_btnproveedor}")
    imagenproveedor = None

ruta_imagen_btnreporte = os.path.join(os.path.dirname(__file__), 'Assets/images/reporte.png')
try:
    imagen = Image.open(ruta_imagen_btnreporte)
    imagen = imagen.resize((90, 90), Image.LANCZOS)
    imagenreporte = ImageTk.PhotoImage(imagen)
except FileNotFoundError:
    print(f"Error: no se puede encontrar el archivo en la ruta {ruta_imagen_btnreporte}")
    imagenreporte = None



# Configuración de los frames
window.configure(bg="gray")
framesuperior = tk.Frame(window, height=200, bg='orange')
framelateral = tk.Frame(window, bg='lightblue')
framesuperior.pack(side='top', fill='both', padx=2, ipady=20)
framelateral.pack(side='left', padx=2, pady=5, fill='y')
framecontenido = tk.Frame(window, bg='lightgreen')
framecontenido.pack(side='right', fill='both', expand=True, padx=2, pady=5)

# Widgets
label1 = ttk.Label(framesuperior, text='Llantera Urias', font=('Arial', 16, 'bold'), background='orange')
label1.pack(side='left', fill='both', expand=True)

if imagenrueda:
    botonMenu = tk.Button(framelateral, image=imagenrueda, command=mostrar_menu)
    botonMenu.pack(side='bottom', pady=2)

if imagenproveedor:
    boton1 = tk.Button(framelateral, image=imagenproveedor, command=inventario)
    boton1.pack(side='bottom', pady=2)

if imagenreporte:
    boton2 = tk.Button(framelateral, image=imagenreporte, command=inventario)
    boton2.pack(side='bottom', pady=2)


# Llamar a la función Menu (puedes personalizarla como desees)
botonmenu1 = tk.Button(framecontenido, text='click').pack(side='right', anchor='se')

window.mainloop()