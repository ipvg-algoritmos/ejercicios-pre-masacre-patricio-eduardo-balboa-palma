lista = [5, 8, 12, 3, 9, 14, 7, 1, 6, 11] # Esta es la lista
print("Lista de números:", lista) # Print para saber que números hay en la lista

buscar_numero = int(input("Introduce el número que buscas en la lista: ")) # Solicita al usuario el número a buscar

if buscar_numero in lista: # Variable para saber si el número está en la lista
    posicion = lista.index(buscar_numero)
    print(f"El número {buscar_numero} se encuentra en la lista en la posición {posicion}.")
else:
    print(f"El número {buscar_numero} no se encuentra en la lista.")