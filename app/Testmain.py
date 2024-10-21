import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from Testconexion import obtener_datos_inventario, obtener_proveedor,llenar_datos_inventario

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

    frame_widgetscontenido = tk.Frame(framecontenido)
    frame_widgetscontenido.pack(side='right', expand=True, fill='both')

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
    
    TablaInventario.bind('<<TreeviewSelect>>', on_treeview_select)

    # Scrollbar para el Treeview
    scrollbar = ttk.Scrollbar(frame_treeview_inventario, orient="vertical", command=TablaInventario.yview)
    TablaInventario.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

    # Obtener datos y llenar el Treeview
    datos = obtener_datos_inventario()
    for fila in datos:
        TablaInventario.insert('', 'end', values=fila)

    separacionx = 5
    separacion=5

    lblID= tk.Label(frame_widgetscontenido, text='ID: ').grid(padx=separacionx, pady=separacion,row=0,column=0)
    lblMarca= tk.Label(frame_widgetscontenido, text='Marca: ').grid(padx=separacionx, pady=separacion,row=1,column=0)
    lblMedida = tk.Label(frame_widgetscontenido, text='Medida: ').grid(padx=separacionx, pady=separacion,row=2,column=0)
    lblDisponible= tk.Label(frame_widgetscontenido,text='Disponible: ').grid(padx=separacionx, row=3,column=0)
    global entID, entMarca, entMedida, entDisponible
    entID= tk.Entry(frame_widgetscontenido).grid(padx=separacionx, pady=separacion,row=0,column=1)
    entMarca = tk.Entry(frame_widgetscontenido).grid(padx=separacionx, row=1,column=1)
    entMedida= tk.Entry(frame_widgetscontenido).grid(padx=separacionx, row=2,column=1)
    entDisponible = tk.Entry(frame_widgetscontenido).grid(padx=separacionx, row=3,column=1)

    def on_treeview_select(event):
        """Función que maneja la selección de una fila en el Treeview."""
        selected_item = TablaInventario.selection()  # Obtiene la fila seleccionada
        if selected_item:
            item = TablaInventario.item(selected_item)  # Obtiene los datos de la fila
            record = item['values']  # Extrae los valores de la fila seleccionada

            # Llenar los campos de Entry con los valores seleccionados
            entID.delete(0, tk.END)
            entID.insert(0, record[0])

            entMarca.delete(0, tk.END)
            entMarca.insert(0, record[1])

            entMedida.delete(0, tk.END)
            entMedida.insert(0, record[2])

            entDisponible.delete(0, tk.END)
            entDisponible.insert(0, record[3])



    btnguardarinventario=tk.Button(frame_widgetscontenido, text='Guardar', command=llenar_datos_inventario).grid(padx=separacionx,pady=separacion, row=4,column=3)
    


def reportes():
    """Función para abrir la ventana de agregar inventario."""
    addinventario = tk.Tk()
    addinventario.title('Agregar nuevo objeto')
    addinventario.geometry('820x520')
    Texto = tk.Label(addinventario, text='SELECCION DE REPORTE A PDF', font=('Arial', 40, 'bold')).pack(expand=True, fill='both')

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
def cargar_imagenlogo(ruta):
    try:
        imagen = Image.open(ruta)
        imagen = imagen.resize((100,70), Image.LANCZOS)
        return ImageTk.PhotoImage(imagen)
    except FileNotFoundError:
        print(f"Error: no se puede encontrar el archivo en la ruta {ruta}")
        return None

# Rutas de imágenes
ruta_imagen_logo=os.path.join(os.path.dirname(__file__), 'Assets/images/llantera_6.png')
ruta_imagen_btnrueda = os.path.join(os.path.dirname(__file__), 'Assets/images/rueda.png')
ruta_imagen_btnproveedor = os.path.join(os.path.dirname(__file__), 'Assets/images/proveedor.png')
ruta_imagen_btnreporte = os.path.join(os.path.dirname(__file__), 'Assets/images/reporte.png')

imagenrueda = cargar_imagen(ruta_imagen_btnrueda)
imagenproveedor = cargar_imagen(ruta_imagen_btnproveedor)
imagenreporte = cargar_imagen(ruta_imagen_btnreporte)

imagenlogo = cargar_imagenlogo(ruta_imagen_logo)
# Configuración de frames
window.configure(bg=colorfondo)
framesuperior = tk.Frame(window, height=220, bg='#005a9d')

framelateral = tk.Frame(window, bg=colorbanner)
framesuperior.pack(side='top', fill='both', ipady=40)
framelateral.pack(side='left', fill='y')
framecontenido = tk.Frame(window, bg='gray')
framecontenido.pack(side='right', fill='both', expand=True, pady=25, padx=25, anchor='e')

# Widgets framsuperior
lbllogo = tk.Label(framesuperior, image=imagenlogo,background=colorbanner).pack(side='left', fill='y')
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
