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


# BDD 
create schema llanteras
# Llantas BDD
CREATE TABLE Llantas (
    Id INT PRIMARY KEY IDENTITY(1,1), -- Clave primaria y autoincrementable
    marca VARCHAR(50) NOT NULL,        -- Marca de la llanta
    medida VARCHAR(20) NOT NULL,       -- Medida de la llanta
    cantidad_disponible INT NOT NULL,  -- Cantidad disponible
    precio DECIMAL(10, 2) NOT NULL,    -- Precio de la llanta
);



# Proveedores BDD
CREATE TABLE Proveedores (
  ID INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único y autoincremental
    NombreProveedor VARCHAR(100) NOT NULL,
    ContactoPrincipal VARCHAR(100) NOT NULL,
    Telefono VARCHAR(15),
    Email VARCHAR(100),
    Direccion VARCHAR(255),
    Pais VARCHAR(50),
    CodigoPostal VARCHAR(10),
    TipoProducto VARCHAR(100),
    MetodoPago VARCHAR(50),
    CuentaBancaria VARCHAR(50),
    EstadoProveedor BOOLEAN NOT NULL, -- Estado del proveedor como booleano
    Observaciones VARCHAR(255)
    );

    INSERT INTO Proveedores (NombreProveedor, ContactoPrincipal, Telefono, Email, Direccion, Pais, CodigoPostal, TipoProducto, MetodoPago, CuentaBancaria, EstadoProveedor, Observaciones)
VALUES 
    ('Neumáticos del Norte S.A.', 'Juan Pérez', '555-1234', 'contacto@neumaticosnorte.com', 'Av. Principal 123, Ciudad A', 'México', '12345', 'Neumáticos para vehículos ligeros', 'Transferencia', '123456789', 1, 'Suministramos neumáticos de alta calidad para automóviles y SUVs.'),
    
    ('Equipos Balanceo y Montaje S.A. de C.V.', 'María Gómez', '555-5678', 'info@equiposbalanceo.com', 'Calle Secundaria 456, Ciudad B', 'México', '54321', 'Equipos de taller', 'Cheque', '987654321', 1, 'Proveedores de equipos de montaje y balanceo para talleres automotrices.'),
    
    ('Herramientas Rápidas S.R.L.', 'Pedro López', '555-8765', 'ventas@herramientasrapidas.com', 'Calle Tercera 789, Ciudad C', 'México', '67890', 'Herramientas de reparación', 'Transferencia', '123123123', 1, 'Distribuimos herramientas y kits de reparación para neumáticos y llantas.'),
    
    ('Lubricantes y Limpieza S.A.', 'Laura Torres', '555-4321', 'soporte@lubricanteslimpieza.com', 'Calle Cuarta 321, Ciudad D', 'México', '09876', 'Lubricantes y productos de limpieza', 'Transferencia', '321321321', 1, 'Ofrecemos lubricantes y limpiadores para el mantenimiento de llantas y equipos.'),
    
    ('Ruedas & Repuestos S.A.', 'Carlos Ruiz', '555-5670', 'contacto@ruedasrepuestos.com', 'Av. Internacional 654, Ciudad E', 'México', '23456', 'Ruedas de repuesto', 'Cheque', '456456456', 1, 'Suministramos ruedas de repuesto para todos los tipos de vehículos.'),
    
    ('Ecollantas Verde S.A. de C.V.', 'Sofía Martínez', '555-6789', 'info@ecollantasverde.com', 'Calle Nueva 234, Ciudad F', 'México', '34567', 'Llantas ecológicas', 'Transferencia', '654654654', 1, 'Proveedores de llantas ecológicas y sostenibles.'),
    
    ('Neumáticos Off-Road S.A.', 'Fernando Díaz', '555-7890', 'ventas@neumaticosoffroad.com', 'Calle Séptima 111, Ciudad G', 'México', '45678', 'Llantas 4x4', 'Cheque', '789789789', 1, 'Especialistas en llantas para vehículos off-road y 4x4.'),
    
    ('Tecnología TPMS S.R.L.', 'María López', '555-3456', 'info@tecnologiatpms.com', 'Calle Octava 222, Ciudad H', 'México', '56789', 'Sistemas de monitoreo de presión', 'Transferencia', '321654987', 1, 'Proveedores de sistemas TPMS para monitoreo de presión de neumáticos.'),
    
    ('Logística Neumática S.A.', 'Antonio Morales', '555-4567', 'contacto@logisticaneumatica.com', 'Calle Novena 333, Ciudad I', 'México', '67890', 'Servicios de transporte', 'Cheque', '654321789', 1, 'Ofrecemos servicios de transporte para llantas y equipos.'),
    
    ('Marketing Automotriz S.A. de C.V.', 'Lucía García', '555-5678', 'ventas@marketingautomotriz.com', 'Calle Décima 444, Ciudad J', 'México', '78901', 'Publicidad y marketing', 'Transferencia', '987321654', 1, 'Proveedores de servicios de marketing para la industria automotriz.');

