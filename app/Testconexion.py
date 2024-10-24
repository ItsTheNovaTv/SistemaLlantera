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

def llenar_datos_inventario():
    """Se guardaran datos en tabla llantas dependiendo del id"""
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

def insertar_datos(id, marca, medida, cantidad_disponible):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()

        # Consulta SQL para insertar datos
        consulta = "INSERT INTO llantas (id, marca, medida, cantidad_disponible) VALUES (%s, %s, %s, %s)"
        valores = (id, marca, medida, cantidad_disponible)

        # Ejecutar la consulta
        cursor.execute(consulta, valores)

        # Guardar cambios en la base de datos
        conexion.commit()
        print(f"Datos insertados correctamente, ID: {id}")

    except mysql.connector.IntegrityError as error:
        if error.errno == 1062:  # Código de error de MySQL para entrada duplicada
            print(f"Error: Ya existe un registro con el ID {id}.")
        else:
            print(f"Error de integridad de datos: {error}")

    except mysql.connector.Error as error:
        print(f"Error al insertar datos: {error}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()



def actualizar(conexion, id_value, marca_value, medida_value, cantidad_disponible):
    cursor = conexion.cursor()
    sql = "UPDATE llantas SET marca = %s, medida = %s, cantidad_disponible = %s WHERE id = %s"
    valores = (marca_value, medida_value, cantidad_disponible, id_value)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    print("Datos actualizados correctamente")


def eliminar(conexion, id_value):
    cursor = conexion.cursor()
    sql = "DELETE FROM llantas WHERE id = %s"
    value = (id_value,)
    cursor.execute(sql, value)
    conexion.commit()
    cursor.close()
    print("Datos eliminados correctamente")