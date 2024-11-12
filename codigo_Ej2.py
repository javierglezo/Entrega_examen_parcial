from datos import localidades

# Función para identificar localidades con todas las conexiones menores a 15 km en una lista vacia::
def localidades_con_conexiones_cortas():
    localidades_cortas = []
    for localidad, conexiones in localidades.items():
        # Comprobar si todas las distancias de las conexiones son menores a 15
        if all(dist < 15 for _, dist in conexiones):
            localidades_cortas.append(localidad)
    return localidades_cortas

# Ejemplo de uso
resultado = localidades_con_conexiones_cortas()
print("Localidades con todas las conexiones menores a 15 km:", resultado)
