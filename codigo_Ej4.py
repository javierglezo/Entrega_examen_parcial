from datos import localidades


# Función para encontrar todas las rutas posibles sin ciclos entre dos localidades
def rutas_sin_ciclos(origen, destino):
    rutas = []

    def dfs(actual, camino):
        # Si llegamos al destino, añadimos el camino a la lista de rutas
        if actual == destino:
            rutas.append(camino)
            return
        # Exploramos los vecinos del nodo actual
        for vecino, _ in localidades[actual]:
            if vecino not in camino:  # Evitamos ciclos
                dfs(vecino, camino + [vecino])

    # Iniciamos la búsqueda desde el origen
    dfs(origen, [origen])
    return rutas

# Función de menú para interactuar con el usuario
def menu():
    print("=== Rutas Alternativas sin Ciclos ===")
    print("Localidades disponibles:", ", ".join(localidades.keys()))

    while True:
        origen = input("Ingrese el nombre de la localidad de origen (o 'salir' para terminar): ")
        
        if origen.lower() == 'salir':
            print("Saliendo del programa.")
            break
        
        if origen not in localidades:
            print("Localidad de origen no válida. Por favor, ingrese una localidad de la lista.")
            continue

        destino = input("Ingrese el nombre de la localidad de destino: ")
        
        if destino not in localidades:
            print("Localidad de destino no válida. Por favor, ingrese una localidad de la lista.")
            continue

        # Encontrar y mostrar las rutas sin ciclos
        rutas = rutas_sin_ciclos(origen, destino)
        if rutas:
            print(f"Rutas posibles sin ciclos entre {origen} y {destino}:")
            for ruta in rutas:
                print(" -> ".join(ruta))
        else:
            print(f"No hay rutas posibles sin ciclos entre {origen} y {destino}.")

# Ejecutar el menú
menu()
