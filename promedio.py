#Saludar al usario
print("Bienvenido usario\nIngrese las notas")
#Usario ingre las notas
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))
#Realizar el calculo
pn = (n1 + n2 + n3) 
p = (pn / 3)
# Si el Alumno aprovo
if p >= 4.0:
    print(f"Aprovaste \nCon un promedio de {p}")
# Si el Alumno reprovo
elif p <= 4.0:
    print(f"Reprovaste \nCon un promedio de {p}")
#Si ocurre un error
else:
    print("No se pudo realizar la operacion \n ingrese los datos nuevamente")