# Escribe un programa que pida al usuario un número entero positivo. El programa debe contar cuántos dígitos tiene el número utilizando un bucle while.
""""""

número = int(input("por favor ingrese un número entero postivo:"))

if número >= 1:
     print("Es entero positivo")

     contador =0
     temp = número

     while temp > 0:
       temp //= 10
       contador += 1
     print("El número de dígitos en", número, "es:", contador)

else:
    print("Debe ingresar un número mayor o igual a 1. Intente de nuevo.")

