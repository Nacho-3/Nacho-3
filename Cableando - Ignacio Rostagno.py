def calcular_longitud_minima_de_cable(cantidad_pueblos, kilometro_megacentral, kilometros_pueblos):

    kilometros_pueblos.append(kilometro_megacentral)

    kilometros_pueblos.sort()

    distancias_consecutivas = []
    for i in range(1, len(kilometros_pueblos)):
        distancia = kilometros_pueblos[i] - kilometros_pueblos[i - 1]
        distancias_consecutivas.append(distancia)

    return sum(distancias_consecutivas)


cantidad_pueblos = int(input("Ingresa la cantidad de pueblitos: "))
kilometro_megacentral = int(input("Ingresa el kilómetro de la megacentral: "))
kilometros_pueblos = list(map(int, input("Ingresa los kilómetros de los pueblitos separados por espacio: ").split()))

longitud_minima = calcular_longitud_minima_de_cable(cantidad_pueblos, kilometro_megacentral, kilometros_pueblos)
print("La longitud mínima de cable necesaria es:", longitud_minima)
