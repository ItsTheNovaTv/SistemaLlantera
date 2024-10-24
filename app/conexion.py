import mysql.connector
admin = False


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
    print("Accedso a proveedores")
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

def insertar_datos(id_value, marca_value, medida_value, disponible_value):
    """Se guardaran datos en tabla llantas"""
    conexion = conectar_bd()
    if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO llantas (id, marca, medida, cantidad_disponible) VALUES (%s, %s, %s, %s)"
            valores = (id_value, marca_value, medida_value, disponible_value)
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Datos insertados correctamente.")
    else:
        print("No se pudo establecer la conexión.")


    
    print('Se guardaron los datos')

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
