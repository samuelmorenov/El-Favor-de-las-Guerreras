# El Favor de las Guerreras

## Despliegue del entorno

### Instalación de anaconda y librerías

Descargar en instalar [Anaconda](https://www.anaconda.com/products/individual)

Una vez instalado Anaconda, desde la aplicación de promt de anaconda *Anaconda Prompt* crear un entorno nuevo con el comando:

`conda create --name <nombre del entorno>`

Para activar el entorno creado ejecuntar el comando:

`conda activate <nombre del entorno>`

Abrir el navegador de Anaconda *Anaconda Navigator*, en *Aplications on* seleccionar el entorno creado. A continuación abrir la sección *Environments* y buscar e importar el archivo anaconda.yaml para que se instalen las librerías necesarias.

### Ejecución y configuración

Para la ejecución de la aplicación abrir el programa *Spyder*  desde *Home* del navegador de Anaconda

<img src="/doc/images/spyder.png">

Desde *Spyder* abrir el archivo `main.py` que está en `\src\main\python` y pulsar F5 para ejecutar.

Para cambiar la configuración, abrir el archivo `param.properties` que está en `\src\main\resources`. Hay 3 campos configurables:

- MODO: Para elegir entre **Generar datos** (1), **Entrenar a la red neuronal** (2) o **Jugar** (3)
	
- NUM_SIMULACIONES: En caso de haber elegido el modo de generar datos, este numero indica el numero de partidas que se van a simular
	
- DIFICULTAD: Para elegir entre **Bot de acciones aleatorias** (1) o **Red neuronal entrenada** (2)
