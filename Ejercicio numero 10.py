#Escribe un programa que pida al usuario ingresar una contraseña y repita la solicitud mientras la contraseña ingresada sea incorrecta. El programa debe continuar hasta que el usuario ingrese la contraseña correcta. Utiliza una estructura whilepara simular un do while.
""""""

contraseña_correcta = "segura123"
contraseña_ingresada = input("Por favor, ingrese la contraseña: ")

while True:
    contraseña_ingresada = input("Por favor, ingrese la contraseña: ")
    
    if contraseña_ingresada == contraseña_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Intente de nuevo.")