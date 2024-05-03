#Preguntar al usario la edad
#Realizar la linea de comando sobre si el usario es menor
edad = int(input("Ingrese la edad: "))
if edad >= 0 and edad <=17:
    print(f"Usted es clasificado como menor edad, su edad es {edad}")
#Realizar la linea de comando sobre si el usario es mayor
elif edad >= 18 and edad <= 100:
    print(f"Usted es clasificado como mayor edad, su edad es {edad}")
#Mostrar el  error si el digito supera 101
else:
    print("La edad que se ingreso no se clasificar")