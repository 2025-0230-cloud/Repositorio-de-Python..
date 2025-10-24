#Escribe un programa que imprima la tabla de multiplicar de un número dado por el usuario, desde el 1 hasta el 10, utilizando un bucle for.
""""""

numero= int(input("Por favor ingrese un número para ver su tabla de multiplicar: "))

print("La tabla de multiplicar del", numero, "es:")

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)