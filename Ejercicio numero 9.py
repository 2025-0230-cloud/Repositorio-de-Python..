#Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle while. El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.
""""""

numero = int(input("Por favor ingrese un número entero positivo para calcular su factorial: "))

if numero < 0:
    print("El factorial no está definido para números negativos. Por favor ingrese un número entero positivo.")

factorial = 1
contador = 1

while contador <= numero:
    factorial *= contador
    contador += 1

print("El factorial de", numero, "es:", factorial)
