import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from coneccion import obtener_datos_inventario, obtener_proveedor, guardar_proveedor  # Importa las funciones desde tu archivo de conexión

# Colores de fondo y banner
colorfondo = '#1f1f1f'
colorbanner = '#2b2d42'

def limpiar_frame(frame):
    """Función para limpiar todos los widgets de un frame."""
    for widget in frame.winfo_children():
        widget.destroy()

def mostrar_proveedor():
    """Función para mostrar los proveedores en el Treeview."""
    # Limpiar el frame actual
    limpiar_frame(framecontenido)

    frame_treeview_Proveedores = tk.Frame(framecontenido)
    frame_treeview_Proveedores.pack(fill='both', expand=True)

    # Crear el Treeview
    TablaProveedores = ttk.Treeview(
        frame_treeview_Proveedores,
        columns=('ID', 'NombreProveedor', 'ContactoPrincipal', 'Telefono', 'Email',
                 'Direccion', 'Pais', 'CodigoPostal', 'TipoProducto', 
                 'MetodoPago', 'CuentaBancaria', 'EstadoProveedor', 'Observaciones'),
        show='headings'
    )

    # Crear headings
    for col in TablaProveedores['columns']:
        TablaProveedores.heading(col, text=col)
        TablaProveedores.column(col, width=100,anchor='center')
    
        TablaProveedores.column('ID', width=10)
        TablaProveedores.column('NombreProveedor',anchor='w', width=200)
        TablaProveedores.column('ContactoPrincipal',width=130, anchor='w')
        TablaProveedores.column('Observaciones', width=500, anchor='w')
        TablaProveedores.column('Email', width=200, anchor='w')
        TablaProveedores.column('Direccion',width=200, anchor='w')

    # Añadir un scrollbar
    scrollbar = ttk.Scrollbar(frame_treeview_Proveedores, orient="horizontal", command=TablaProveedores.xview)
    TablaProveedores.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='bottom', fill='x')

    TablaProveedores.pack(side='left', anchor='n', fill='both', expand=True)

    # Obtener datos y llenar el Treeview
    proveedores = obtener_proveedor()
    for proveedor in proveedores:
        TablaProveedores.insert('', 'end', values=proveedor)

def mostrar_inventario():
    """Función para mostrar el menú de inventario."""
    
    # Limpiar frame actual
    limpiar_frame(framecontenido)  

    # Frame para el Treeview
    frame_treeview_inventario = tk.Frame(framecontenido, width=100)  
    frame_treeview_inventario.pack(side='left', fill='y')

    # Treeview para mostrar proveedores
    TablaInventario = ttk.Treeview(frame_treeview_inventario, columns=("ID", "Marca", "Medida", "Disponible"), show='headings')
    TablaInventario.pack(side='left', anchor='n', fill='y')

    # Crear headings 
    TablaInventario.heading("ID", text="ID")  
    TablaInventario.heading("Marca", text="Marca")                
    TablaInventario.heading("Medida", text="Medida")              
    TablaInventario.heading("Disponible", text="Disponible")      

    # Definir tamaño
    TablaInventario.column("ID", width=50)
    TablaInventario.column("Marca", width=100)
    TablaInventario.column("Medida", width=100)
    TablaInventario.column("Disponible", width=100)
     

    # Scrollbar para el Treeview
    scrollbar = ttk.Scrollbar(frame_treeview_inventario, orient="vertical", command=TablaInventario.yview)
    TablaInventario.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

    # Obtener datos y llenar el Treeview
    datos = obtener_datos_inventario()
    for fila in datos:
        TablaInventario.insert('', 'end', values=fila)
    

def reportes():
    """Función para abrir la ventana de agregar inventario."""
    addinventario = tk.Tk()
    addinventario.title('Agregar nuevo objeto')
    addinventario.geometry('820x520')

# Crear ventana principal
window = tk.Tk()
window.title('Llantera Urias')
window.geometry('1280x720')  
# Cargar imágenes
def cargar_imagen(ruta):
    try:
        imagen = Image.open(ruta)
        imagen = imagen.resize((110, 110), Image.LANCZOS)
        return ImageTk.PhotoImage(imagen)
    except FileNotFoundError:
        print(f"Error: no se puede encontrar el archivo en la ruta {ruta}")
        return None

# Rutas de imágenes
ruta_imagen_btnrueda = os.path.join(os.path.dirname(__file__), 'Assets/images/rueda.png')
ruta_imagen_btnproveedor = os.path.join(os.path.dirname(__file__), 'Assets/images/proveedor.png')
ruta_imagen_btnreporte = os.path.join(os.path.dirname(__file__), 'Assets/images/reporte.png')

imagenrueda = cargar_imagen(ruta_imagen_btnrueda)
imagenproveedor = cargar_imagen(ruta_imagen_btnproveedor)
imagenreporte = cargar_imagen(ruta_imagen_btnreporte)

# Configuración de frames
window.configure(bg=colorfondo)
framesuperior = tk.Frame(window, height=220, bg='#005a9d')
framelateral = tk.Frame(window, bg=colorbanner)
framesuperior.pack(side='top', fill='both', ipady=40)
framelateral.pack(side='left', fill='y')
framecontenido = tk.Frame(window, bg='gray')
framecontenido.pack(side='right', fill='both', expand=True, pady=25, padx=25, anchor='e')

# Widgets framsuperior
label1 = ttk.Label(framesuperior, text='  Llantera Urias', font=('Arial', 25, 'bold'), background=colorbanner, foreground='white')
label1.pack(side='left', fill='both', expand=True)

# Botones laterales
btnInventario = tk.Button(framelateral, image=imagenrueda, command=mostrar_inventario, borderwidth=0, background='lightgray')
btnInventario.pack(side='top', pady=22, padx=20)

btnProveedor = tk.Button(framelateral, image=imagenproveedor, command=mostrar_proveedor, borderwidth=0, background='lightgray')
btnProveedor.pack(side='top', pady=22, padx=20)

btnReporte = tk.Button(framelateral, image=imagenreporte, command=reportes, borderwidth=0, background='lightgray')
btnReporte.pack(side='top', pady=22, padx=20)

# Configuración y ejecución de la ventana principal
window.mainloop()
