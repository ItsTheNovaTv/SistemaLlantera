import mysql.connector
from tkinter import messagebox
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
            messagebox.showwarning(message=f"Error: Ya existe un registro con el ID {id}.",title= "Error")
            print(f"Error: Ya existe un registro con el ID {id}.")
        else:
            print(f"Error de integridad de datos: {error}")
            messagebox.showwarning(message=f"Error: Error de integridad de datos: {error}.",title= "Error")
    except mysql.connector.Error as error:
        print(f"Error al insertar datos: {error}")
        messagebox.showwarning(message=f"Error al insertar datos: {error}.",title= "Error")
        

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            
def llenar_datos_inventario():
    """llenar tabla"""

def cargar_combo():
    try:
     
        conexion = conectar_bd()
        cursor = conexion.cursor()
        
        # Consulta para obtener todos los IDs de la tabla llantas
        cursor = conexion.cursor()
        cursor.execute("SELECT id FROM llantas")
        ids = [str(row[0]) for row in cursor.fetchall()]
        return ids

    except mysql.connector.Error as error:
        print(f"Error al cargar IDs: {error}")
        return []

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
   


def actualizar(conexion, id_value, marca_value, medida_value, cantidad_disponible):
    
    messagebox.YESNO(message='Esta a punto de realizar un cambio en un dato existente. ¿Desea continuar?.')
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

def obtener_datos_llanta(id_llanta):
    try:
        conexion=conectar_bd()
        cursor = conexion.cursor()
        consulta = "SELECT marca, medida, cantidad_disponible FROM llantas WHERE id = %s"
        cursor.execute(consulta, (id_llanta,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado  # (marca, medida, cantidad_disponible)
        else:
            return None

    except mysql.connector.Error as error:
        print(f"Error al obtener datos de llanta: {error}")
        return None

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()