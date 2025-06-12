def calcular_promedio():
    suma = 0
    contador = 0

    while True:
        try:
            numero = float(input("ingrese un número (negativo para terminar): "))
        except ValueError:
            print("por favor, ingrese un número válido.")
            continue

        if numero < 0:
            break

        suma += numero
        contador += 1

    if contador > 0:
        promedio = suma / contador
        print(f"el promedio de los {contador} números ingresados es: {promedio}")
    else:
        print("no se ingresaron números válidos.")