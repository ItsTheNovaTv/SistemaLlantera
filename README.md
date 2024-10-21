# SistemaLlantera

# Bustamnate
Para poder ejecutar el programa, debe de instalar las dependencias necesarias en caso de no tenerlas.
Es recomendable utilizar un entorno virtual para que no haya incompatibilidad con las demas deppendencias.
ejecutar para crear entorno virtual, primero nos dirigimos a la direccion de nuestro proyecto 


cd /ruta/a/tu/proyecto

Una vez ubicados en el folder del proyecto ejecutamos


python -m venv venv

Esto creara una carpeta venv, ahora debemos activar el entorno virtual
En terminal de windows, ubicados en el folder usamos 


venv\Scripts\activate

Si usamos Bash de github, vamos al directorio del proyecto 


cd ~/ruta/a/tu/proyecto

Y activamos venv


source venv/Scripts/activate

instalamos las dependencias en la terminal con el venv activo


pip install -r requirements.txt


# Estructura sugerida del proyecto
mi_proyecto/
│
├── venv/                          # Entorno virtual
│   ├── Scripts/                   # (Windows)
│   ├── bin/                       # (Linux/macOS)
│   ├── Lib/                       # (Windows)
│   └── site-packages/             # Librerías instaladas
│
├── app/                           # Código fuente de la aplicación
│   ├── __init__.py                # Inicializa el paquete
│   ├── routes.py                  # Definiciones de rutas
│   ├── models.py                  # Modelos de datos (si usas una base de datos)
│   ├── forms.py                   # Definiciones de formularios (si es necesario)
│   └── static/                    # Archivos estáticos (CSS, JavaScript, imágenes)
│       ├── css/
│       ├── js/
│       └── images/
│
├── templates/                     # Plantillas HTML
│   ├── base.html                  # Plantilla base
│   └── index.html                 # Página de inicio
│
├── tests/                         # Pruebas unitarias
│   ├── test_app.py                # Pruebas para la aplicación
│   └── test_models.py             # Pruebas para los modelos
│
├── requirements.txt               # Lista de dependencias
├── .gitignore                     # Archivos y carpetas a ignorar en Git
├── README.md                      # Descripción del proyecto
└── main.py                        # Archivo principal para ejecutar la aplicación

#