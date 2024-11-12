
"""
import heapq
import tracemalloc
from datos import localidades  # Se asume que 'localidades' es un diccionario con el grafo definido

# Algoritmo de Dijkstra para encontrar la ruta más corta entre dos localidades
def ruta_mas_corta(origen, destino):
    distancias = {localidad: float('inf') for localidad in localidades}
    distancias[origen] = 0
    camino = {origen: [origen]}
    
    # Usamos una cola de prioridad para gestionar las localidades a visitar
    cola = [(0, origen)]
    
    while cola:
        # Extraemos la localidad con la distancia más corta actual
        dist_actual, actual = heapq.heappop(cola)
        
        # Si llegamos al destino, retornamos el camino y la distancia
        if actual == destino:
            return camino[actual], dist_actual
        
        # Recorremos los vecinos de la localidad actual
        for vecino, distancia in localidades[actual]:
            nueva_dist = dist_actual + distancia
            # Si encontramos una distancia más corta, la actualizamos
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                camino[vecino] = camino[actual] + [vecino]
                heapq.heappush(cola, (nueva_dist, vecino))
    
    # Si no se encuentra una ruta al destino
    return None, float('inf')

# Análisis de Eficiencia con tracemalloc
def analizar_eficiencia(origen, destino):
    # Iniciar el monitoreo de memoria
    tracemalloc.start()
    
    # Ejecutar la función y medir el tiempo de ejecución
    ruta, distancia = ruta_mas_corta(origen, destino)
    
    # Obtener el uso actual y el pico de memoria
    uso_memoria, pico_memoria = tracemalloc.get_traced_memory()
    
    # Detener el monitoreo de memoria
    tracemalloc.stop()
    
    # Mostrar resultados
    print(f"Ruta más corta de {origen} a {destino}: {' -> '.join(ruta) if ruta else 'No hay ruta'}")
    print(f"Distancia total: {distancia} km" if distancia != float('inf') else "Destino inalcanzable")
    print(f"Uso de memoria: {uso_memoria / 1024:.2f} KB")
    print(f"Pico de memoria: {pico_memoria / 1024:.2f} KB")

# Ejemplo de uso
origen = "Madrid"
destino = "Villanueva de la Cañada"
analizar_eficiencia(origen, destino)
"""

import tracemalloc
from datos import localidades  # Se asume que 'localidades' es un diccionario con el grafo definido

# Función para identificar localidades con todas las conexiones menores a 15 km
def localidades_con_conexiones_cortas():
    localidades_cortas = []
    for localidad, conexiones in localidades.items():
        # Comprobar si todas las distancias de las conexiones son menores a 15
        if all(dist < 15 for _, dist in conexiones):
            localidades_cortas.append(localidad)
    return localidades_cortas

# Función para ejecutar y analizar el uso de memoria de la función anterior
def analizar_eficiencia_localidades_cortas():
    # Iniciar el monitoreo de memoria
    tracemalloc.start()
    
    # Ejecutar la función y almacenar el resultado
    resultado = localidades_con_conexiones_cortas()
    
    # Obtener el uso actual y el pico de memoria
    uso_memoria, pico_memoria = tracemalloc.get_traced_memory()
    
    # Detener el monitoreo de memoria
    tracemalloc.stop()
    
    # Mostrar resultados
    print("Localidades con todas las conexiones menores a 15 km:", resultado)
    print(f"Uso de memoria: {uso_memoria / 1024:.2f} KB")
    print(f"Pico de memoria: {pico_memoria / 1024:.2f} KB")

# Ejecutar el análisis de eficiencia
analizar_eficiencia_localidades_cortas()
