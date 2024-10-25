import mysql.connector
from tkinter import Tk, ttk, messagebox

# Función para cargar los IDs de la base de datos
def cargar_combo():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="llantera"
        )
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

# Función que se llama cuando se abre el Combobox
def dropdown_opened():
    try:
        combo_values = cargar_combo()
        cbcombo['values'] = combo_values
        if not combo_values:
            print("No se encontraron datos para el combobox.")
    except Exception as e:
        print(f"Error en dropdown_opened: {e}")

# Configuración de la interfaz de usuario de Tkinter
root = Tk()
frame_widgetscontenido2 = ttk.Frame(root)
frame_widgetscontenido2.pack()

separacionx = 10
separacion = 10

cbcombo = ttk.Combobox(frame_widgetscontenido2, postcommand=dropdown_opened)
cbcombo.grid(padx=separacionx, pady=separacion, row=1, column=1)

entMarca2 = ttk.Entry(frame_widgetscontenido2)
entMarca2.grid(padx=separacionx, pady=separacion, row=2, column=1)

entMedida2 = ttk.Entry(frame_widgetscontenido2)
entMedida2.grid(padx=separacionx, pady=separacion, row=3, column=1)

entDisponible2 = ttk.Entry(frame_widgetscontenido2)
entDisponible2.grid(padx=separacionx, pady=separacion, row=4, column=1)

root.mainloop()