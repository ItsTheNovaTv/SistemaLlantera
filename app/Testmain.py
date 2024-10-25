import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from Testconexion import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
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
    def solo_numeros(char):
        return char.isdigit()
    
    vcmd = (window.register(solo_numeros), '%S')
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
    color1 = tk.Label(frame_widgetscontenido1, bg=colorbanner, height=2, text='Insertar', foreground='white', font=('Arial', 16, 'bold'))
    color1.grid(row=0, column=0, columnspan=2, sticky="we")
    lblID1= tk.Label(frame_widgetscontenido1, text='ID: ')
    lblID1.grid(padx=separacionx, pady=separacion,row=1,column=0)
    lblMarca1= tk.Label(frame_widgetscontenido1, text='Marca: ')
    lblMarca1.grid(padx=separacionx, pady=separacion,row=2,column=0)
    lblMedida1 = tk.Label(frame_widgetscontenido1, text='Medida: ')
    lblMedida1.grid(padx=separacionx, pady=separacion,row=3,column=0)
    lblDisponible1= tk.Label(frame_widgetscontenido1,text='Disponible: ')
    lblDisponible1.grid(padx=separacionx,pady=separacion, row=4,column=0)

    entID1= tk.Entry(frame_widgetscontenido1)
    entID1.grid(padx=separacionx, pady=separacion,row=1,column=1)
    entMarca1 = tk.Entry(frame_widgetscontenido1)
    entMarca1.grid(padx=separacionx,pady=separacion, row=2,column=1)
    entMedida1= tk.Entry(frame_widgetscontenido1)
    entMedida1.grid(padx=separacionx,pady=separacion, row=3,column=1)
    entDisponible1 = tk.Entry(frame_widgetscontenido1,validate='key', validatecommand=vcmd)
    entDisponible1.grid(padx=separacionx,pady=separacion, row=4,column=1)

    def obtener_datos():
        id_value1 = entID1.get()
        Marca_value1=entMarca1.get()
        Medida_value1=entMedida1.get()
        Disponible_value1=entDisponible1.get()

        insertar_datos(id_value1, Marca_value1, Medida_value1, Disponible_value1)
    
    btnguardarinventario=tk.Button(frame_widgetscontenido1, text='Guardar', command=obtener_datos).grid(padx=separacionx,pady=separacion, row=5,column=1,)
    #seccion2
    def dropdown_opened():
            try:
                combo_values = cargar_combo()
                cbcombo['values'] = combo_values
                if not combo_values:
                    print("No se encontraron datos para el combobox.")
            except Exception as e:
                print(f"Error en dropdown_opened: {e}")


    def selection_changed(event):
        seleccion = cbcombo.get()  # Obtener el valor seleccionado
        if seleccion:
         datos_llanta = obtener_datos_llanta(seleccion)
        if datos_llanta:
            marca, medida, disponible = datos_llanta
            entMarca2.delete(0, tk.END)  # Limpiar la entrada
            entMarca2.insert(0, marca)   # Asignar el valor de 'marca'
            entMedida2.delete(0, tk.END)  # Limpiar la entrada
            entMedida2.insert(0, medida)  # Asignar el valor de 'medida'
            entDisponible2.delete(0, tk.END)  # Limpiar la entrada
            entDisponible2.insert(0, disponible)  # Asignar el valor de 'disponible'
        else:
            messagebox.showerror("Error", "No se encontraron datos para la llanta seleccionada.")

    
    
    color1 = tk.Label(frame_widgetscontenido2, bg=colorbanner, height=2,text='Editar', foreground='white', font=('Arial', 16, 'bold'))
    color1.grid(row=0, column=0, columnspan=2, sticky="we")
    lblID2= tk.Label(frame_widgetscontenido2, text='ID: ')
    lblID2.grid(padx=separacionx, pady=separacion,row=1,column=0)
    lblMarca2= tk.Label(frame_widgetscontenido2, text='Marca: ')
    lblMarca2.grid(padx=separacionx, pady=separacion,row=2,column=0)
    lblMedida2 = tk.Label(frame_widgetscontenido2, text='Medida: ')
    lblMedida2.grid(padx=separacionx, pady=separacion,row=3,column=0)
    lblDisponible2= tk.Label(frame_widgetscontenido2,text='Disponible: ')
    lblDisponible2.grid(padx=separacionx,pady=separacion, row=4,column=0)
    
    cbcombo= ttk.Combobox(frame_widgetscontenido2, postcommand=dropdown_opened, width=5)
    cbcombo.grid(padx=separacionx, pady=separacion,row=1,column=1)
    cbcombo.bind("<<ComboboxSelected>>", selection_changed)
    entMarca2 = tk.Entry(frame_widgetscontenido2)
    entMarca2.grid(padx=separacionx,pady=separacion, row=2,column=1)
    entMedida2= tk.Entry(frame_widgetscontenido2)
    entMedida2.grid(padx=separacionx, pady=separacion,row=3,column=1)
    entDisponible2 = tk.Entry(frame_widgetscontenido2,validate='key', validatecommand=vcmd)
    entDisponible2.grid(padx=separacionx, pady=separacion,row=4,column=1)

    def guardar_cambios():
        id_value2=cbcombo.get()
        marca_value2= entMarca2.get()
        medida_value2= entMedida2.get()
        cantidad_disponible2=entDisponible2.get()

        actualizar(marca_value2,medida_value2,cantidad_disponible2,id_value2)
        
    btnguardarinventario=tk.Button(frame_widgetscontenido2, text='Guardar', command=guardar_cambios).grid(padx=separacionx,pady=separacion, row=5,column=1,)

    
    #seccion3 
    def dropdown_opened2():
        try:
            combo_values = cargar_combo()
            cbcombo2['values'] = combo_values
            if not combo_values:
                print("No se encontraron datos para el combobox.")
        except Exception as e:
            print(f"Error en dropdown_opened: {e}")

    def selection_changed2(event):
        seleccion = cbcombo2.get()  # Obtener el valor seleccionado
        if seleccion:
            datos_llanta = obtener_datos_llanta2(seleccion)
            if datos_llanta:
                # Verificar si se obtuvieron 3 valores
                if len(datos_llanta) == 3:
                    marca, medida, cantidad_disponible = datos_llanta
                    entMarca3.delete(0, tk.END)  # Limpiar la entrada
                    entMarca3.insert(0, marca)   # Asignar el valor de 'marca'
                    entMedida3.delete(0, tk.END)  # Limpiar la entrada
                    entMedida3.insert(0, medida)  # Asignar el valor de 'medida'
                    lblSalidaDisp.config(text=cantidad_disponible)  # Asignar el valor de 'cantidad_disponible'
                else:
                    messagebox.showerror("Error", "Se esperaban 3 valores, pero se obtuvieron menos.")
            else:
                messagebox.showerror("Error", "No se encontraron datos para la llanta seleccionada.")

   
    color1 = tk.Label(frame_widgetscontenido3, bg=colorbanner, height=2, text='Salidas', foreground='white', font=('Arial', 16, 'bold'))
    color1.grid(row=0, column=0, columnspan=2, sticky="we")
    lblID= tk.Label(frame_widgetscontenido3, text='ID: ')
    lblID.grid(padx=separacionx, pady=separacion,row=1,column=0)
    lblMarca= tk.Label(frame_widgetscontenido3, text='Marca: ')
    lblMarca.grid(padx=separacionx, pady=separacion,row=2,column=0)
    lblMedida = tk.Label(frame_widgetscontenido3, text='Medida: ')
    lblMedida.grid(padx=separacionx, pady=separacion,row=3,column=0)
    lblSalida= tk.Label(frame_widgetscontenido3,text='Salida: ')
    lblSalida.grid(padx=separacionx,pady=separacion, row=4,column=0)
    lblDis= tk.Label(frame_widgetscontenido3,text='Disponible: ')
    lblDis.grid(padx=separacionx,pady=separacion, row=5,column=0)

    cbcombo2= ttk.Combobox(frame_widgetscontenido3, postcommand=dropdown_opened2, width=5)
    cbcombo2.grid(padx=separacionx, pady=separacion,row=1,column=1)
    cbcombo2.bind("<<ComboboxSelected>>", selection_changed2)
    entMarca3 = tk.Entry(frame_widgetscontenido3)
    entMarca3.grid(padx=separacionx,pady=separacion, row=2,column=1)
    entMedida3= tk.Entry(frame_widgetscontenido3)
    entMedida3.grid(padx=separacionx,pady=separacion, row=3,column=1)
    lblSalidaDisp = tk.Label(frame_widgetscontenido3, text='0')
    lblSalidaDisp.grid(column=1,row=5)
    
    def confirmar_eliminacion(id_value):
        
        respuesta = messagebox.askyesno(
            title="Confirmar eliminación",
            message="¿Está seguro de que desea eliminar este elemento?"
        )

        if respuesta:
            eliminar(id_value)
        else:
            print("Eliminación cancelada por el usuario.")




    btnProcesar=tk.Button(frame_widgetscontenido3, text='Eliminar', command=lambda: confirmar_eliminacion(id_value=cbcombo2.get()), fg="white", background="red").grid(padx=separacionx,pady=separacion, row=6,column=1)

def reportes():
    limpiar_frame(framecontenido)
    """Función para abrir la ventana de agregar inventario."""

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',        # Cambia si es necesario
            user='root',             # Tu usuario de MySQL
            password='root',         # Tu contraseña de MySQL
            database='llantera'      # Nombre de tu base de datos
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    

# Funciones para obtener datos de la base de datos
def obtener_proveedor():
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("""SELECT ID, NombreProveedor, ContactoPrincipal, Telefono, 
                          Email, Direccion, Pais, CodigoPostal, TipoProducto, 
                          MetodoPago, CuentaBancaria, EstadoProveedor, Observaciones 
                          FROM proveedores""")
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return filas
    return []

def obtener_datos_inventario():
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, marca, medida, cantidad_disponible FROM llantas")
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return filas
    return []

# Función para llenar el Treeview de Inventario
def llenar_inventario():
    filas = obtener_datos_inventario()
    for fila in filas:
        TablaInventario.insert('', 'end', values=fila)

# Función para llenar el Treeview de Proveedores
def llenar_proveedores():
    filas = obtener_proveedor()
    for fila in filas:
        TablaProveedores.insert('', 'end', values=fila)

# Función para generar PDF de la tabla de Inventario
def generar_pdf_inventario():
    def conectar_bd():

        try:
            conexion = mysql.connector.connect(
                host='localhost',        # Cambia si es necesario
                user='root',             # Tu usuario de MySQL
                password='root',         # Tu contraseña de MySQL
                database='llantera'      # Nombre de tu base de datos
            )
            return conexion
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
    

# Funciones para obtener datos de la base de datos
def obtener_proveedor():
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("""SELECT ID, NombreProveedor, ContactoPrincipal, Telefono, 
                          Email, Direccion, Pais, CodigoPostal, TipoProducto, 
                          MetodoPago, CuentaBancaria, EstadoProveedor, Observaciones 
                          FROM proveedores""")
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return filas
    return []

def obtener_datos_inventario():
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, marca, medida, cantidad_disponible FROM llantas")
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return filas
    return []

# Función para llenar el Treeview de Inventario
def llenar_inventario():
    filas = obtener_datos_inventario()
    for fila in filas:
        TablaInventario.insert('', 'end', values=fila)

# Función para llenar el Treeview de Proveedores
def llenar_proveedores():
    filas = obtener_proveedor()
    for fila in filas:
        TablaProveedores.insert('', 'end', values=fila)

# Función para generar PDF de la tabla de Inventario
def generar_pdf_inventario():
    filas = obtener_datos_inventario()
    c = canvas.Canvas("inventario.pdf", pagesize=letter)
    c.drawString(100, 750, "Reporte de Inventario")
    c.drawString(100, 730, "ID       Marca        Medida       Disponible")
    
    y = 710
    for fila in filas:
        c.drawString(100, y, f"{fila[0]}      {fila[1]}      {fila[2]}      {fila[3]}")
        y -= 20
    
    c.save()
    print("PDF de inventario generado.")

# Función para generar PDF de la tabla de Proveedores
def generar_pdf_proveedores():
    filas = obtener_proveedor()
    c = canvas.Canvas("proveedores.pdf", pagesize=letter)
    c.drawString(100, 750, "Reporte de Proveedores")
    c.drawString(100, 730, "ID       NombreProveedor       ContactoPrincipal       Telefono       Email")
    
    y = 710
    for fila in filas:
        c.drawString(100, y, f"{fila[0]}      {fila[1]}      {fila[2]}      {fila[3]}      {fila[4]}")
        y -= 20
    
    c.save()
    print("PDF de proveedores generado.")

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Gestión")

# Crear un Frame para el Treeview de Inventario
frame_treeview_inventario = ttk.Frame(root)
frame_treeview_inventario.pack(fill=tk.BOTH, expand=True)

# Crear el Treeview para Inventario
TablaInventario = ttk.Treeview(frame_treeview_inventario, columns=('ID', 'Marca', 'Medida', 'Disponible'), show='headings')
TablaInventario.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configuración de columnas del Treeview de Inventario
TablaInventario.heading("ID", text="ID")
TablaInventario.heading("Marca", text="Marca")
TablaInventario.heading("Medida", text="Medida")
TablaInventario.heading("Disponible", text="Disponible")

# Definir tamaño
TablaInventario.column("ID", width=50)
TablaInventario.column("Marca", width=100)
TablaInventario.column("Medida", width=100)
TablaInventario.column("Disponible", width=100)

# Crear un Frame para el Treeview de Proveedores
frame_treeview_proveedores = ttk.Frame(root)
frame_treeview_proveedores.pack(fill=tk.BOTH, expand=True)

# Crear el Treeview para Proveedores
TablaProveedores = ttk.Treeview(frame_treeview_proveedores, columns=('ID', 'NombreProveedor', 'ContactoPrincipal', 'Telefono', 'Email',
    'Direccion', 'Pais', 'CodigoPostal', 'TipoProducto', 'MetodoPago', 'CuentaBancaria', 'EstadoProveedor', 'Observaciones'), show='headings')
TablaProveedores.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configuración de columnas del Treeview de Proveedores
for col in TablaProveedores['columns']:
    TablaProveedores.heading(col, text=col)
    TablaProveedores.column(col, width=100, anchor='center')

# Ajustar el ancho de las columnas
TablaProveedores.column('ID', width=10)
TablaProveedores.column('NombreProveedor', anchor='w', width=200)
TablaProveedores.column('ContactoPrincipal', width=130, anchor='w')
TablaProveedores.column('Observaciones', width=500, anchor='w')
TablaProveedores.column('Email', width=200, anchor='w')
TablaProveedores.column('Direccion', width=200, anchor='w')

# Botones para cargar datos
btn_cargar_inventario = tk.Button(root, text="Cargar Inventario", command=llenar_inventario)
btn_cargar_inventario.pack(pady=10)

btn_cargar_proveedores = tk.Button(root, text="Cargar Proveedores", command=llenar_proveedores)
btn_cargar_proveedores.pack(pady=10)

# Botones para generar PDFs
btn_pdf_inventario = tk.Button(root, text="Generar PDF Inventario", command=generar_pdf_inventario)
btn_pdf_inventario.pack(pady=10)

btn_pdf_proveedores = tk.Button(root, text="Generar PDF Proveedores", command=generar_pdf_proveedores)
btn_pdf_proveedores.pack(pady=10)

# Ejecutar la aplicación





















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
def cargar_imagen_sesion(ruta):
    try:
        imagen = Image.open(ruta)
        imagen = imagen.resize((40,40), Image.LANCZOS)
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
ruta_imagen_Sesion = os.path.join(os.path.dirname(__file__), 'Assets/images/sesion.png')

imagenrueda = cargar_imagen(ruta_imagen_btnrueda)
imagenproveedor = cargar_imagen(ruta_imagen_btnproveedor)
imagenreporte = cargar_imagen(ruta_imagen_btnreporte)

imagensesion = cargar_imagen_sesion(ruta_imagen_Sesion)

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

btnCerrarSesion = tk.Button(framesuperior, image=imagensesion, command=reportes, borderwidth=0, background=colorbanner)
btnCerrarSesion.pack(side='right',anchor='w', fill='both')


# Configuración y ejecución de la ventana principal
window.mainloop()
