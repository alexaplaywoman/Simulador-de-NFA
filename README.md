# Simulador de NFA en Python

Este proyecto es un simulador para autómatas finitos no deterministas (NFA) que toma un autómata definido en formato JSON y simula su ejecución con una cadena de entrada. Los resultados se exportan a un archivo JSON.

## Requisitos

- **Python 3.8 o superior**
- Biblioteca `python-dotenv` para manejar variables de entorno.

## Configuración del proyecto

Sigue los pasos a continuación para configurar y ejecutar el simulador:

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tu-usuario/nfa-simulator.git
cd nfa-simulator
```
### 2. Crear un entorno virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Crear un archivo `.env` 
Crea un archivo llamado .env en la raíz del proyecto con las siguientes variables:
```bash
RUTA_NFA=nfa01.json  # Ruta del archivo JSON que define el NFA
CADENA=010101        # Cadena de entrada para la simulación
```
- Utilizar como ejemplo el archivo nfa01.json 
### 4. Ejecutar el programa 
Esto generará un archivo simulacion.json con los resultados de la simulación.
