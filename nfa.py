import json
from typing import List, Dict, Union, Set
from dotenv import load_dotenv
import os

# Función: cargar_nfa
# Variables:
#   ruta: str - Ruta del archivo JSON que contiene la descripción del NFA.
# Retorna:
#   Dict - Representación del NFA como un diccionario.
def cargar_nfa(ruta: str) -> Dict:
    try:
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}.")
        raise
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta} no contiene un JSON válido.")
        raise

# Función: guardar_simulacion
# Variables:
#   ruta: str - Ruta del archivo donde se guardará la simulación.
#   simulacion: Dict - Diccionario que contiene los datos de la simulación.
# Realiza:
#   Guarda la simulación en formato JSON en el archivo especificado.
def guardar_simulacion(ruta: str, simulacion: Dict):
    try:
        with open(ruta, 'w') as archivo:
            json.dump(simulacion, archivo, indent=4)
    except IOError as e:
        print(f"Error: No se pudo escribir en el archivo {ruta}: {e}")
        raise

# Función: precomputar_transiciones
# Variables:
#   Delta: List[List[Union[str, List[str]]]] - Lista que describe las transiciones del NFA.
# Retorna:
#   Dict[tuple, List[str]] - Diccionario que mapea (estado, símbolo) a los estados de destino.
# Realiza:
#   Precalcula un diccionario para optimizar las búsquedas de transiciones.
def precomputar_transiciones(Delta: List[List[Union[str, List[str]]]]) -> Dict[tuple, List[str]]:
    transiciones = {}
    for origen, simbolo, destinos in Delta:
        transiciones[(origen, simbolo)] = destinos
    return transiciones

# Función: obtener_transiciones
# Variables:
#   transiciones: Dict[tuple, List[str]] - Diccionario precalculado de transiciones.
#   estados: Set[str] - Conjunto de estados actuales.
#   simbolo: str - Símbolo de entrada para la transición.
# Retorna:
#   Set[str] - Conjunto de nuevos estados alcanzables.
# Realiza:
#   Calcula los nuevos estados alcanzables a partir de los estados actuales y el símbolo de entrada.
def obtener_transiciones(transiciones: Dict[tuple, List[str]], estados: Set[str], simbolo: str) -> Set[str]:
    nuevos_estados = set()
    for estado in estados:
        if (estado, simbolo) in transiciones:
            nuevos_estados.update(transiciones[(estado, simbolo)])
    return nuevos_estados

# Función: simular_nfa
# Variables:
#   nfa: Dict - Diccionario que describe el NFA.
#   cadena: str - Cadena de entrada que se procesará.
# Retorna:
#   Dict - Diccionario que contiene el resultado de la simulación.
# Realiza:
#   Simula el procesamiento de la cadena por el NFA y genera los resultados paso a paso.
def simular_nfa(nfa: Dict, cadena: str) -> Dict:
    transiciones = precomputar_transiciones(nfa['Delta'])  # Precomputar las transiciones
    estados_actuales = {nfa['q0']}  # Inicializar con el estado inicial
    resultado = [list(estados_actuales)]  # Registrar el estado inicial en el resultado

    for simbolo in cadena:
        estados_actuales = obtener_transiciones(transiciones, estados_actuales, simbolo)  # Actualizar estados
        resultado.append(list(estados_actuales))  # Registrar los nuevos estados

    # Verificar si algún estado actual es de aceptación
    aceptada = any(estado in nfa['F'] for estado in estados_actuales)

    return {
        "type": "simulacion_nfa",
        "dfa": "nfa01.json",
        "cadena": cadena,
        "resultado": resultado,
        "aceptada": aceptada
    }

# Programa principal
# Realiza:
#   Carga un NFA desde un archivo, simula su funcionamiento con una cadena de entrada,
#   y guarda los resultados en un archivo JSON.
def main():
    # Cargar variables del archivo .env
    load_dotenv()
    ruta_nfa = os.getenv("RUTA_NFA")  # Ruta del archivo que contiene el NFA
    cadena = os.getenv("CADENA")      # Cadena de entrada para la simulación
    ruta_salida = "simulacion.json"  # Ruta del archivo para guardar la simulación

    try:
        # Cargar el NFA desde el archivo
        nfa = cargar_nfa(ruta_nfa)

        # Simular el NFA con la cadena dada
        simulacion = simular_nfa(nfa, cadena)

        # Guardar la simulación en el archivo de salida
        guardar_simulacion(ruta_salida, simulacion)
        print(f"Simulación guardada en {ruta_salida}")
    except Exception as e:
        print(f"Error durante la simulación: {e}")

if __name__ == "__main__":
    main()
