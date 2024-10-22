import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from Testconexion import obtener_datos_inventario, obtener_proveedor,llenar_datos_inventario
from tkinter import Scrollbar

# Colores de fondo y banner
colorfondo = '#575757'
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



    # Treeview para mostrar inventario
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

    frame_widgetscontenido = tk.Frame(framecontenido, background=colorfondo)
    frame_widgetscontenido.pack(side='right', expand=True, fill='y')
    separacionx = 6
    separacion=8


    #Frame inferior dentro de frame_widgetcontenidoinferior
    myscrollbar=ttk.Scrollbar(frame_widgetscontenido,orient="horizontal")
    myscrollbar.pack(side="bottom",fill="x")

    frame_widgetscontenidoinferior = tk.Frame(frame_widgetscontenido, highlightbackground="black", highlightthickness=4)
    frame_widgetscontenidoinferior.pack(pady=separacion, padx=separacionx, fill='both', expand=True, side='bottom', anchor='center')
    label1 = tk.Label(frame_widgetscontenidoinferior, height=3, background=colorbanner).pack(side='bottom', fill='x')



    frame_widgetscontenido1 = tk.Frame(frame_widgetscontenido, highlightbackground="black", highlightthickness=4)
    frame_widgetscontenido1.pack(pady=separacion,anchor='n',side='left', padx=separacionx)
    frame_widgetscontenido2 = tk.Frame(frame_widgetscontenido, highlightbackground="black", highlightthickness=4)
    frame_widgetscontenido2.pack(pady=separacion,anchor='n',side='left', padx=separacionx)    
    frame_widgetscontenido3 = tk.Frame(frame_widgetscontenido, highlightbackground="black", highlightthickness=4)
    frame_widgetscontenido3.pack(pady=separacion,anchor='n',side='left', padx=separacionx)


    #seccion1
    color1 = tk.Label(frame_widgetscontenido1, bg=colorbanner, height=2)
    color1.grid(row=0, column=0, columnspan=2, sticky="we")
    lblID= tk.Label(frame_widgetscontenido1, text='ID: ')
    lblID.grid(padx=separacionx, pady=separacion,row=1,column=0)
    lblMarca= tk.Label(frame_widgetscontenido1, text='Marca: ')
    lblMarca.grid(padx=separacionx, pady=separacion,row=2,column=0)
    lblMedida = tk.Label(frame_widgetscontenido1, text='Medida: ')
    lblMedida.grid(padx=separacionx, pady=separacion,row=3,column=0)
    lblDisponible= tk.Label(frame_widgetscontenido1,text='Disponible: ')
    lblDisponible.grid(padx=separacionx,pady=separacion, row=4,column=0)

    color2 = tk.Label(frame_widgetscontenido1, bg=colorbanner, height=2)
    color2.grid(row=0, column=1, columnspan=2, sticky="we")    
    entID= tk.Entry(frame_widgetscontenido1)
    entID.grid(padx=separacionx, pady=separacion,row=1,column=1)
    entMarca = tk.Entry(frame_widgetscontenido1)
    entMarca.grid(padx=separacionx,pady=separacion, row=2,column=1)
    entMedida= tk.Entry(frame_widgetscontenido1)
    entMedida.grid(padx=separacionx,pady=separacion, row=3,column=1)
    entDisponible = tk.Entry(frame_widgetscontenido1)
    entDisponible.grid(padx=separacionx,pady=separacion, row=4,column=1)

    btnguardarinventario=tk.Button(frame_widgetscontenido1, text='Guardar', command=llenar_datos_inventario).grid(padx=separacionx,pady=separacion, row=5,column=1,)


    #seccion2
    color1 = tk.Label(frame_widgetscontenido2, bg=colorbanner, height=2)
    color1.grid(row=0, column=0, columnspan=2, sticky="we")
    lblID= tk.Label(frame_widgetscontenido2, text='ID: ')
    lblID.grid(padx=separacionx, pady=separacion,row=1,column=0)
    lblMarca= tk.Label(frame_widgetscontenido2, text='Marca: ')
    lblMarca.grid(padx=separacionx, pady=separacion,row=2,column=0)
    lblMedida = tk.Label(frame_widgetscontenido2, text='Medida: ')
    lblMedida.grid(padx=separacionx, pady=separacion,row=3,column=0)
    lblDisponible= tk.Label(frame_widgetscontenido2,text='Disponible: ')
    lblDisponible.grid(padx=separacionx,pady=separacion, row=4,column=0)
    
    color2 = tk.Label(frame_widgetscontenido2, bg=colorbanner, height=2)
    color2.grid(row=0, column=1, columnspan=2, sticky="we")
    entID= tk.Entry(frame_widgetscontenido2)
    entID.grid(padx=separacionx, pady=separacion,row=1,column=1)
    entMarca = tk.Entry(frame_widgetscontenido2)
    entMarca.grid(padx=separacionx,pady=separacion, row=2,column=1)
    entMedida= tk.Entry(frame_widgetscontenido2)
    entMedida.grid(padx=separacionx, pady=separacion,row=3,column=1)
    entDisponible = tk.Entry(frame_widgetscontenido2)
    entDisponible.grid(padx=separacionx, pady=separacion,row=4,column=1)

    btnguardarinventario=tk.Button(frame_widgetscontenido2, text='Guardar', command=llenar_datos_inventario).grid(padx=separacionx,pady=separacion, row=5,column=0,)
    btneliminarinventario=tk.Button(frame_widgetscontenido2, text='Eliminar', command=llenar_datos_inventario).grid(padx=separacionx,pady=separacion, row=5,column=1)

    #seccion3
    color1 = tk.Label(frame_widgetscontenido3, bg=colorbanner, height=2)
    color1.grid(row=0, column=0, columnspan=2, sticky="we")
    lblID= tk.Label(frame_widgetscontenido3, text='ID: ')
    lblID.grid(padx=separacionx, pady=separacion,row=1,column=0)
    lblMarca= tk.Label(frame_widgetscontenido3, text='Marca: ')
    lblMarca.grid(padx=separacionx, pady=separacion,row=2,column=0)
    lblMedida = tk.Label(frame_widgetscontenido3, text='Medida: ')
    lblMedida.grid(padx=separacionx, pady=separacion,row=3,column=0)
    lblEntrada= tk.Label(frame_widgetscontenido3,text='Entrada: ')
    lblEntrada.grid(padx=separacionx, pady=separacion, row=4,column=0)
    lblSalida= tk.Label(frame_widgetscontenido3,text='Salida: ')
    lblSalida.grid(padx=separacionx,pady=separacion, row=5,column=0)
    
    color2 = tk.Label(frame_widgetscontenido3, bg=colorbanner, height=2)
    color2.grid(row=0, column=1, columnspan=2, sticky="we")
    entID= tk.Entry(frame_widgetscontenido3)
    entID.grid(padx=separacionx, pady=separacion,row=1,column=1)
    entMarca = tk.Entry(frame_widgetscontenido3)
    entMarca.grid(padx=separacionx,pady=separacion, row=2,column=1)
    entMedida= tk.Entry(frame_widgetscontenido3)
    entMedida.grid(padx=separacionx,pady=separacion, row=3,column=1)
    entEntrada = tk.Entry(frame_widgetscontenido3)
    entEntrada.grid(padx=separacionx,pady=separacion, row=4,column=1)
    entSalida = tk.Entry(frame_widgetscontenido3)
    entSalida.grid(padx=separacionx,pady=separacion, row=5,column=1)

    btnBuscar=tk.Button(frame_widgetscontenido3, text='Buscar', command=llenar_datos_inventario).grid(padx=separacionx,pady=separacion, row=6,column=0)
    btnProcesar=tk.Button(frame_widgetscontenido3, text='Procesar', command=llenar_datos_inventario).grid(padx=separacionx,pady=separacion, row=6,column=1)

    


def reportes():
    limpiar_frame(framecontenido)
    """Función para abrir la ventana de agregar inventario."""
    addinventario = tk.Tk()
    addinventario.title('Agregar nuevo objeto')
    addinventario.geometry('820x520')
    Texto = tk.Label(addinventario, text='SELECCION DE REPORTE A PDF', font=('Arial', 40, 'bold')).pack(expand=True, fill='both')
        # Frame para el Treeview
    frame_treeview_inventario = tk.Frame(framecontenido, width=100)  
    frame_treeview_inventario.pack(side='left', fill='y')

  
    # Treeview para mostrar proveedores
    TablaInventario = ttk.Treeview(addinventario, columns=("ID", "Marca", "Medida", "Disponible"), show='headings')
    TablaInventario.pack(anchor='n', fill='y')

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
    scrollbar = ttk.Scrollbar(addinventario, orient="vertical", command=TablaInventario.yview)
    TablaInventario.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

    # Obtener datos y llenar el Treeview
    datos = obtener_datos_inventario()
    for fila in datos:
        TablaInventario.insert('', 'end', values=fila)


# Crear ventana principal

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
        imagen = imagen.resize((110,110), Image.LANCZOS)
        return ImageTk.PhotoImage(imagen)
    except FileNotFoundError:
        print(f"Error: no se puede encontrar el archivo en la ruta {ruta}")
        return None
window = tk.Tk()
window.title('Llantera Urias')
window.geometry('1280x720')  
# Rutas de imágenes
ruta_imagen_logo=os.path.join(os.path.dirname(__file__), 'Assets/images/llantera_6.png')
ruta_imagen_btnrueda = os.path.join(os.path.dirname(__file__), 'Assets/images/rueda.png')
ruta_imagen_btnproveedor = os.path.join(os.path.dirname(__file__), 'Assets/images/proveedor.png')
ruta_imagen_btnreporte = os.path.join(os.path.dirname(__file__), 'Assets/images/reporte.png')

imagenrueda = cargar_imagen(ruta_imagen_btnrueda)
imagenproveedor = cargar_imagen(ruta_imagen_btnproveedor)
imagenreporte = cargar_imagen(ruta_imagen_btnreporte)

imagenlogo = cargar_imagenlogo(ruta_imagen_logo)
# Configuración de frames de UI
window.configure(bg=colorfondo)
framesuperior = tk.Frame(window, height=220, bg='#005a9d')

framelateral = tk.Frame(window, bg=colorbanner)
framesuperior.pack(side='top', fill='both', ipady=30)
framelateral.pack(side='left', fill='y')
framecontenido = tk.Frame(window, bg='gray')
framecontenido.pack(side='right', fill='both', expand=True, pady=25, padx=25, anchor='e')

# Widgets framsuperior
lbllogo = tk.Label(framesuperior, image=imagenlogo,background=colorbanner).pack(side='left', fill='both',ipadx=20,)
label1 = ttk.Label(framesuperior, text='  Llantera Urias', font=('Arial', 25, 'bold'), background=colorbanner, foreground='white')
label1.pack(side='left', fill='both', expand=True)

# Botones laterales
btnInventario = tk.Button(framelateral, image=imagenrueda, command=mostrar_inventario, borderwidth=0, background='white')
btnInventario.pack(side='top', pady=22, padx=20)

btnProveedor = tk.Button(framelateral, image=imagenproveedor, command=mostrar_proveedor, borderwidth=0, background='white')
btnProveedor.pack(side='top', pady=22, padx=20)

btnReporte = tk.Button(framelateral, image=imagenreporte, command=reportes, borderwidth=0, background='white')
btnReporte.pack(side='top', pady=22, padx=20)

# Configuración y ejecución de la ventana principal
window.mainloop()
