#Escribe un programa que pida al usuario que ingrese un número entero positivo. El programa debe mostrar todos los números del 1 hasta el número ingresado, uno por uno, utilizando un bucle while.
""""""
numero = int(input("por favor ingrese un numero entero positivo:"))

if numero >=1: 
    print("El numero ingresado es un entero positivo")

else:
    print("Debe ingrsear numeros mayor o igual a 1. Intente de nuevo.") 

contador1 =1

while contador1 <= numero:
    print (contador1)
    contador1 +=1