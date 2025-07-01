# **Sistema de Gestión de Clínica Médica (Python + PostgreSQL)**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?style=for-the-badge&logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-2.1-purple?style=for-the-badge&logo=pandas)

## 📌 **Resumen del Proyecto**

Este proyecto es una aplicación de consola en Python que simula un completo sistema de gestión para una clínica médica. El objetivo principal es demostrar un manejo integral de una base de datos **PostgreSQL**, abarcando el ciclo de vida completo de los datos: desde la configuración inicial y carga masiva, hasta la implementación de lógica de negocio avanzada con procedimientos almacenados.

La aplicación permite gestionar pacientes, profesionales y turnos, y sirve como un caso de estudio práctico del uso de **SQLAlchemy** como ORM, la ejecución segura de **SQL nativo** y la interacción con la base de datos a través de una interfaz de usuario interactiva.

---

## ✨ **Características Principales**

* **Configuración e Inicialización:** Creación del esquema de la base de datos (DDL) a partir de modelos de Python definidos con SQLAlchemy.
* **Carga de Datos Masiva:** Población inicial de la base de datos desde archivos `.csv` utilizando la librería Pandas.
* **Gestión de Datos Dual:** Demostración de la inserción de datos mediante dos técnicas:
    1.  A través del **ORM de SQLAlchemy** para una sintaxis orientada a objetos, segura y legible.
    2.  Mediante **SQL nativo parametrizado** para un control más directo de la base de datos.
* **Manipulación de Datos en Lote:** Scripts para la actualización y borrado masivo de registros basados en reglas de negocio (ej. reprogramar o cancelar turnos por fecha).
* **Evolución del Esquema:** Modificación de la estructura de una tabla en producción (`ALTER TABLE`) para añadir nuevas columnas sin pérdida de datos.
* **Lógica de Negocio en la Base de Datos:**
    * Implementación de **Procedimientos Almacenados** y **Funciones** en `PL/pgSQL` para encapsular y automatizar operaciones complejas y críticas.
    * Validación de disponibilidad de turnos para prevenir conflictos de agendamiento.
* **Interfaz de Usuario (CLI):** Un menú interactivo en la consola que funciona como punto de entrada para que un usuario final opere el sistema de forma intuitiva.

---

## 🚀 **Tecnologías y Herramientas**

| Tecnología | Propósito |
| :--- | :--- |
| **Python** | Lenguaje principal de la aplicación. |
| **PostgreSQL** | Sistema de gestión de bases de datos relacional. |
| **SQLAlchemy** | ORM principal para la interacción entre Python y la base de datos. |
| **psycopg2** | Driver para la comunicación entre Python y PostgreSQL. |
| **Pandas** | Librería para la lectura y procesamiento inicial de los archivos CSV. |
| **DBeaver** | Cliente de base de datos para administración y ejecución de SQL. |
| **Git & GitHub**| Sistema de control de versiones y hosting del repositorio. |

---

## ⚙️ **Instalación y Uso**

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### **Prerrequisitos**
* Tener instalado Python 3.8 o superior.
* Tener instalado y corriendo un servidor de PostgreSQL.
* Tener Git instalado.

### **Pasos de Configuración**

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/AleHerreraSoria/sistema_de_gestion_de_clinica_medica.git](https://github.com/AleHerreraSoria/sistema_de_gestion_de_clinica_medica.git)
    cd sistema_de_gestion_de_clinica_medica
    ```

2.  **Crear y activar el entorno virtual:**
    ```bash
    # Crear el entorno
    python -m venv .venv

    # Activar en Windows
    .venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    El proyecto incluye un archivo `requirements.txt` con todas las librerías necesarias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar la Base de Datos:**
    a. Asegúrate de que tu servicio de PostgreSQL esté activo.
    b. Crea una base de datos. El nombre esperado por el proyecto es `gestion_turnos`.
       ```sql
       CREATE DATABASE gestion_turnos;
       ```
    c. Abre el archivo `database.py` y actualiza la línea `DATABASE_URL` con tu usuario y contraseña de PostgreSQL. **Nota:** Se recomienda usar una contraseña sin acentos ni caracteres especiales para evitar errores de codificación.

5.  **Inicializar el Sistema (Scripts de Única Ejecución):**
    Ejecuta los siguientes scripts en orden para preparar la base de datos.
    ```bash
    # 1. Crear las tablas (pacientes, profesionales, turnos)
    python create_tables.py

    # 2. Cargar los datos iniciales desde los archivos CSV
    python load_data.py

    # 3. Crear los procedimientos almacenados en la base de datos
    # (Ejecuta el contenido del archivo que contiene las funciones SQL en DBeaver)
    ```

6.  **Ejecutar la Aplicación Principal:**
    Para interactuar con el sistema, ejecuta el menú interactivo.
    ```bash
    python menu_interactivo.py
    ```
    ¡Sigue las instrucciones en pantalla para gestionar la clínica!

---

### **🏛️ Estructura y Módulos del Proyecto**
    
* `database.py`: Contiene la configuración del motor de SQLAlchemy y la conexión a la base de datos.
* `models.py`: Define el esquema de la base de datos a través de clases de Python (Modelos ORM).
* `create_tables.py`: Script de única ejecución para crear las tablas en la base de datos a partir de los modelos.
* `load_data.py`: Script de única ejecución para la carga inicial de datos desde la carpeta `dataset_turnos/`.
* `gestion_profesionales.py`: Script que demuestra la inserción de datos con ORM y SQL directo.
* `manipular_turnos.py`: Script que contiene la lógica para la actualización masiva de turnos.
* `cancelar_turnos.py`: Script con las funciones para el borrado condicional y seguro de turnos.
* `menu_interactivo.py`: Punto de entrada principal de la aplicación. Contiene la interfaz de usuario de consola que invoca a los procedimientos almacenados.
* `requirements.txt`: Lista de dependencias de Python para una fácil instalación del entorno.

---

*Desarrollado por Alejandro N. Herrera Soria - Linkedin: http://www.linkedin.com/in/alejandro-nelson-herrera-soria*