#Escribe un programa que pida al usuario un número entero positivo y luego imprima todos los números impares desde 1 hasta el número ingresado utilizando un bucle while.
""""""

numero = int(input("Por favor ingrese un número entero positivo: "))

if numero >= 1:
    print("El número ingresado es un entero positivo.")

    contador = 1

    while contador <= numero:
        if contador % 2 != 0:
            print(contador)
        contador += 1
else:
    print("Debe ingresar un número mayor o igual a 1. Intente de nuevo.")