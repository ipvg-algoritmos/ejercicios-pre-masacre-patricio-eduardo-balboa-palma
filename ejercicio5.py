# Inicializar la matriz vacía
matriz = []

# Ingresar los elementos de la matriz 3x3
print("Ingrese los elementos de la matriz 3x3:")
for i in range(3):
    fila = []
    for j in range(3):
        num = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(num)
    matriz.append(fila)

# Contadores
positivos = 0
negativos = 0
ceros = 0

# Sumas de diagonales
suma_diagonal_principal = 0
suma_diagonal_secundaria = 0

# Recorrer la matriz
for i in range(3):
    for j in range(3):
        valor = matriz[i][j]

        # Contar positivos, negativos y ceros
        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1
        else:
            ceros += 1

        # Suma de la diagonal principal
        if i == j:
            suma_diagonal_principal += valor
        
        # Suma de la diagonal secundaria
        if i + j == 2:
            suma_diagonal_secundaria += valor

# Mostrar resultados
print("\nResultados:")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de ceros: {ceros}")

# Comparación entre diagonales
if suma_diagonal_principal > suma_diagonal_secundaria:
    print("La suma de la diagonal principal es MAYOR que la secundaria.")
elif suma_diagonal_principal < suma_diagonal_secundaria:
    print("La suma de la diagonal principal es MENOR que la secundaria.")
else:
    print("La suma de ambas diagonales es IGUAL.")