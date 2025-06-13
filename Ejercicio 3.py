#numeros que desea ingresar el usuario
numeros = input("Ingresa aqui tus numeros: ")
#eliminar números con el  primer negativo
numeros_filtrados = []
for n in numeros.split():
    if int(n) < 0:
        break
    numeros_filtrados.append(n)
#para convertir en numeros enteros y guardarlos en una lista
lista = [int(n) for n in numeros_filtrados]
#encontrar numero mayor y menor usando un for (sin usar max ni min)
if lista:
    mayor = lista[0]
    menor = lista[0]
    for n in lista[1:]:
        if n > mayor:
            mayor = n
        if n < menor:
            menor = n
    #Aqui para mostrar el resultado
    print(f"El numero mayor es: {mayor}")
    print(f"El numero menor es: {menor}")
else:
    print("No se ingresaron números válidos.")
