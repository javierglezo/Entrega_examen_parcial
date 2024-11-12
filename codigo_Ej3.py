from datos import localidades

"""Utilizo bfs Exploración Completa: BFS garantiza que explora todos los nodos alcanzables desde un nodo inicial, expandiéndose nivel por nivel. 
Esto es útil en un problema de conectividad, ya que asegura que si el grafo es conexo, cada nodo será visitado durante el recorrido."""
# Función para verificar si el grafo es conexo desde una localidad dada
def es_conexo_desde(localidad_inicial):
    visitados = set()
    
    # Función interna de BFS
    def bfs(origen):
        cola = [origen]
        visitados.add(origen)
        while cola:
            actual = cola.pop(0)
            for vecino, _ in localidades[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

    # Comenzamos la búsqueda desde la localidad inicial proporcionada
    bfs(localidad_inicial)
    
    # Verificamos si visitamos todas las localidades
    return len(visitados) == len(localidades)

# Función de menú para interactuar con el usuario dejando ver las localidades posibles
def menu():
    print("=== Verificar Conectividad del Grafo ===")
    print("Localidades disponibles:", ", ".join(localidades.keys()))
    
    while True:
        localidad_inicial = input("Ingrese el nombre de la localidad inicial para verificar (o 'salir' para terminar): ")
        
        if localidad_inicial.lower() == 'salir':
            print("Saliendo del programa.")
            break
        
        # Validamos si la localidad existe en el grafo
        if localidad_inicial not in localidades:
            print("Localidad no válida. Por favor, ingrese una localidad de la lista.")
        else:
            # Verificamos la conectividad desde la localidad ingresada
            conexo = es_conexo_desde(localidad_inicial)
            if conexo:
                print(f"El grafo es conexo desde {localidad_inicial}.")
            else:
                print(f"El grafo NO es conexo desde {localidad_inicial}.")

# Ejecutar el menú
menu()
