texto = input("Introduce una frase cualquiera: ") # Solicita al usuario una frase

# Contadores para vocales y consonantes
vocales = 0
consonantes = 0

vocales_lista = "aeiouAEIOU" # Variable sobre las vocales, tanto mayúsculas como minúsculas

# Variable para saber si los caracteres estan dentro de la frase
for caracter in texto:
    if caracter.isalpha():  # Verifica si es una letra e ignora números, espacios y símbolos
        if caracter in vocales_lista:
            vocales += 1  # Es vocal
        else:
            consonantes += 1  # Es consonante (incluye ñ y letras con tilde)

# Mostrar resultados
print("Cantidad de vocales:", vocales)
print("Cantidad de consonantes:", consonantes)
