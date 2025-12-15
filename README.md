# TaximeterProject
Scalable Taximeter Project.

## Project Description

This project consists of the development of a scalable taximeter application simulator. The application manages the calculation of fares and travel time, adapting to different operational states (in motion, stopped at traffic lights, operational pauses, and service completion).

Key Features:

*   **Authentication:** An initial ID and password are required to access the system.
*   **Fare Calculation:** The cost of the service is calculated dynamically based on elapsed time and the time slot of use.
*   **State Management:** The system handles pauses and the resumption of journeys.
*   **Data Logging:** Upon service completion, a summary of the total time and cost is issued, and all relevant data is stored in a database.

## Tools Utilized

The project has been developed using the following technologies:

*   **Python:** Main programming language.
*   **SQLite3:** Database management system for local storage.
*   **Docker:** For containerization and consistent deployment.
*   **GUI Interface:** Graphical user interface for interaction (Tkinter).
*   **venv:** Python virtual environment for development isolation.

## Local Installation and Execution

Follow these steps to configure and run the project in your local environment.

### Prerequisites

*   Python 3.x installed.

### Execution Steps

1.  **Clone the repository:** ([Repository](https://github.com/iRuperth/TaximeterProject))

    ```bash
    git clone github.com
    cd TaximeterProject
    ```

2.  **Create the virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    Select the appropriate command for your operating system:

    **Linux / macOS:**

    ```bash
    source venv/bin/activate
    ```

    **Windows (Command Prompt or PowerShell):**

    ```bash
    venv\Scripts\activate
    ```

4.  **Install dependencies:**

    *   *Note: Currently, the project does not require the installation of external dependencies. However, if new libraries are incorporated in future development, use the following command to install them:*

    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute the application:**

    ```bash
    python main.py
    ```

## Execution with Docker

The application can be deployed using Docker for a more isolated and reproducible environment.

### Prerequisites

   *   [Docker Desktop](https://www.docker.com) installed and running.


### 1. Build the Docker Image

Navigate to the project's root directory and build the image using the following command:

```bash
docker build -t dockertaximeter .
```

## How to Contribute

Do you wish to add an improvement? We gladly accept contributions, but we request that you follow our workflow:

1.  **Request access** to the project from an administrator.
2.  **You will be assigned a dedicated branch** for your task.
3.  **Submit a Pull Request** for your changes to be reviewed and integrated.



# TaximeterProject
Scalable Taximeter Project.

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un simulador de aplicación de taxímetro escalable. La aplicación gestiona el cálculo de tarifas y tiempo de viaje, adaptándose a diferentes estados operativos (en movimiento, detenido por semáforos, pausas operativas y finalización del servicio).

Características principales:

*   **Autenticación:** Se requiere un identificador (ID) y una contraseña iniciales para acceder al sistema.
*   **Cálculo de Tarifas:** El costo del servicio se calcula dinámicamente en función del tiempo transcurrido y la franja horaria de uso.
*   **Gestión de Estados:** El sistema maneja las pausas y la reanudación de los trayectos.
*   **Registro de Datos:** Al finalizar el servicio, se emite un resumen del tiempo total y el costo, y se almacenan todos los datos pertinentes en una base de datos.

## Herramientas Utilizadas

El proyecto ha sido desarrollado utilizando las siguientes tecnologías:

*   **Python:** Lenguaje de programación principal.
*   **SQLite3:** Sistema de gestión de bases de datos para el almacenamiento local.
*   **Docker:** Para la contenedorización y un despliegue consistente.
*   **GUI Interface:** Interfaz gráfica de usuario para la interacción (Tkinter).
*   **venv:** Entorno virtual de Python para el aislamiento del desarrollo local.

## Instalación y Ejecución Local

Siga estos pasos para configurar y ejecutar el proyecto en su entorno local.

### Requisito

*   Python 3.x instalado.

### Pasos de Ejecución

1.  **Clonar el repositorio:** ([Repositorio](https://github.com/iRuperth/TaximeterProject))

    ```bash
    git clone https://github.com/iRuperth/TaximeterProject
    cd TaximeterProject

    ```

2.  **Crear el entorno virtual:**

    ```bash
    python -m venv venv
    ```

3.  **Activar el entorno virtual:**

    Seleccione el comando adecuado para su sistema operativo:

    **Linux / macOS:**

    ```bash
    source venv/bin/activate
    ```

    **Windows (Command Prompt o PowerShell):**

    ```bash
    venv\Scripts\activate
    ```

4.  **Instalar dependencias:**

    *   *Nota: Actualmente, el proyecto no requiere la instalación de dependencias externas. Sin embargo, si en un desarrollo futuro se incorporan nuevas librerías, utilice el siguiente comando para instalarlas:*

    ```bash
    pip install -r requirements.txt
    ```

5.  **Ejecutar la aplicación:**

    ```bash
    python main.py
    ```

## Ejecución con Docker

El despliegue de la aplicación puede realizarse utilizando Docker para un entorno más aislado y reproducible.

### Requisito

*   ([Docker Desktop] (https://www.docker.com)) instalado y en ejecución.

### 1. Construir la Imagen de Docker

Navegue al directorio raíz del proyecto y construya la imagen mediante el siguiente comando:

```bash
docker build -t dockertaximeter .


## Contribuciones

Agradecemos las contribuciones al proyecto. Si desea proponer una mejora, reportar un error o añadir una nueva funcionalidad, por favor siga el siguiente procedimiento:

1.  **Solicitud de Acceso:** Contacte con el administrador del repositorio o el mantenedor del proyecto para solicitar acceso de colaborador.
2.  **Asignación de Rama:** Se le proporcionará una rama específica (por ejemplo, `feature/nombre-de-la-mejora` o `bugfix/descripcion-del-fallo`) para que trabaje en los cambios.
3.  **Pull Request (PR):** Una vez completado su trabajo, envíe un *Pull Request* contra la rama principal (`main`/`master`) para su revisión.

Este proceso asegura la integración correcta y el mantenimiento de la calidad del código.

