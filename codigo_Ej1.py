from datos import localidades
import heapq

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

# Función para mostrar el menú e interactuar con el usuario
def mostrar_menu():
    print("Bienvenido al sistema de análisis de rutas de la Comunidad de Madrid.")
    while True:
        print("\n--- Menú Principal ---")
        print("1. Calcular ruta más corta entre dos localidades")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Solicitar origen y destino al usuario
            origen = input("Ingrese la localidad de origen cuidado tildes: ").strip()
            destino = input("Ingrese la localidad de destino cuidado tildes: ").strip()
            
            # Verificar que ambas localidades existen en el grafo
            if origen not in localidades:
                print(f"Error: La localidad '{origen}' no está en el grafo.")
                continue
            if destino not in localidades:
                print(f"Error: La localidad '{destino}' no está en el grafo.")
                continue
            
            # Calcular y mostrar la ruta más corta
            ruta, distancia = ruta_mas_corta(origen, destino)
            if ruta:
                print("Ruta más corta:", " -> ".join(ruta))
                print("Distancia total:", distancia, "km")
            else:
                print("No hay una ruta disponible entre las localidades seleccionadas.")
        
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

# Ejecución del programa
if __name__ == "__main__":
    mostrar_menu()










