#Saludar al usario 
print("Bienvenido Usario")
#Mostrar los usarios registrados en el equipo
print("User1: pedro \nUser2: ange")
user = int(input("Selecione el usario que sea utilizar (1-2): "))
if user == 1:
    print("Seleciono el usario pedro")
    con1 = input("Escriba la contraseña: ")
    if con1 == "1234":
        print("Ingresaste con exito")
    else:
        print("Contraseña incorrecta \nCerando sección del equipo")
elif user == 2:
    print("Seleciono el usario ange")
    con2 = input("Escriba la contraseña: ")
    if con2 == "a4s1":
        print ("Ingresaste con exito")
    else:
        print("Contraseña incorrecta \nCerando sección del equipo")
else:
    print("Usario existente en el equipo \nCerando sección del equipo")