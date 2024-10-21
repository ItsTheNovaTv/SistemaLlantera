import mysql.connector
admin = True


if admin == True:
    credencial = 'root'
    credencialpass='root'
else:
        credencial = 'newuser'
        credencialpass='user'


def conectar_bd():
    """Establecer conexión con la base de datos."""
    try:
        conexion = mysql.connector.connect(
            host='localhost',        # Cambia si es necesario
            user=credencial,             # Tu usuario de MySQL
            password=credencialpass,         # Tu contraseña de MySQL
            database='llantera'      # Nombre de tu base de datos
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    
def validacion_login():
    """Validar usuario y contraseña"""

def obtener_datos_inventario():
    """Obtener datos de la tabla llantas."""
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, marca, medida, cantidad_disponible FROM llantas")
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return filas
    return []

def llenar_datos_inventario():
    """Se guardaran datos en tabla llantas dependiendo del id"""

def Salida_datos_inventario():
    """Funcion para mover datos de tabla llantas a salida, quizas con trigger"""




def obtener_proveedor():
    """Obtener datos de la tabla proveedor."""
    conexion = conectar_bd()
    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute("""SELECT ID, NombreProveedor, ContactoPrincipal, Telefono, 
                          Email, Direccion, Pais, CodigoPostal, TipoProducto, 
                          MetodoPago, CuentaBancaria, EstadoProveedor, Observaciones 
                          FROM proveedores""")  # Asegúrate de incluir el FROM
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return filas
    return []
