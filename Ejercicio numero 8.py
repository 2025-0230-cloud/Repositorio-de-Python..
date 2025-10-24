#Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término, donde el valor de n lo ingresa el usuario, utilizando un bucle for.
""""""

N=int(input("Por favor ingrese el número de términos de la serie de Fibonacci que desea ver: "))
a, b = 0, 1
print("Serie de Fibonacci hasta", N, "términos:")

for _ in range(N):
    print(a)
    a, b = b, a + b