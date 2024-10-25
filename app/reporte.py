import tkinter as tk
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import mysql.connector

# Función para conectar a la base de datos
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
root.mainloop()
