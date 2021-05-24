# El Favor de las Guerreras

## Despliegue del entorno

### Instalacion de anaconda y librerias

Descargar en instalar [Anaconda](https://www.anaconda.com/products/individual)

Una vez instalado Anaconda, desde la aplicación de promt de anaconda *Anaconda Prompt* crear un entorno nuevo con el comando:

`conda create --name <nombre del entorno>`

Para activar el entorno creado ejecuntar el comando:

`conda activate <nombre del entorno>`

Abrir el navegador de Anaconda *Anaconda Navigator*, en *Aplications on* seleccionar el entorno creado. A continuación abrir la seccion *Environments* y buscar e instalar:
	
	- Python 3.7.9
	- Spyder 3.3.6
	- Tensorflow 2.3.0
	- ConfigParser 5.0.2
	
Una vez instaladas las librerias, abrir *Spyder* desde *Home* del navegador de Anaconda

### Ejecución y configuración

Para la ejecución de la aplicación abrir el programa *Spyder* instalado dentro de Anaconda

<img src="/doc/images/spyder.png">

Desde *Spyder* abrir el archivo `main.py` que esta en `\src\main\python` y pulsar F5 para ejecutar.

Para cambiar la configuración, abrir el archivo `param.properties` que esta en `\src\main\resources`. Hay 3 campos configurables:

	- MODO: Para elegir entre **Generar datos** (1), **Entrenar a la red neuronal** (2) o **Jugar** (3)
	- NUM_SIMULACIONES: En caso de haber elegido el modo de generar datos, este numero indica el numero de partidas que se van a simular
	- DIFICULTAD: Para elegir entre **Bot de acciones aleatorias** (1) o **Red neuronal entrenada**

