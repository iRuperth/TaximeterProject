# TaximeterProject
Scalable Taximeter Project.


Aplicación de un simulador de Taximetro, el mismo viene con funciones de marcar el tiempo y costo a medida de que el taxi comienza su recorrido, se detiene por semaforos o pausas fortuitas y al finalizar el recorrido.
Solicita en primera instancia un Id y contraseña para acceder al programa.
Tras estas funciones, imprime un texto en el que refleja el tiempo con la aplicación en funcionamiento, el coste que va dependiendo de las horas en las que se usa el taxi.
Todo esto es guardado en una base de datos.

Herramientas utilizadas.

Python, Docker, SQLite3, GUI interface, y venv como entorno virtual.

Instalación y ejecución inicial. ( Local ).

python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows

En este caso, no se necesitará instalar ninguna dependencia.

Ejecutamos la aplicación.

python main.py


Ahora, para ejecutarlo con Docker.

Comenzamos construyendo la imagen.

docker build -t dockertaximeter .

Ejecutamos el contenedor.

Esto en modo normal, para producción.
docker run -it dockertaximeter

Esto en modo persistente (Base de datos guardada en HOST)
docker run -it -v "$(pwd)/data:/TaximeterProject/data" dockertaximeter


Comandos para inspección o pruebas.

docker run -it dockertaximeter bash
ls /TaximeterProject/data
python main.py





