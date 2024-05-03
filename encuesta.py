T = 0
#Saludar al visitante
print("Bienvenido usario \n si desea conseguir regalos complete la encuesta")
print("Pregunta 1 \n¿Cuál de los siguientes animales vive en el agua?")
print("A.Perro \nB.Cocodrilo \nC.Conejo \nD.Tiburón")
Res = input("Ingrese la respuesta: ") 
if Res == "A":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
elif Res == "B":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
elif Res == "C":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
elif Res == "D":
    print("Respeusta correcta \nobtuviste 1.0 punto")
    T += 1
else:
    print("Respuesta no existente\nobtuviste 0 punto")
    T += 0
    
print("Pregunta 2 \n¿Cuál es el río más largo del mundo?")
print("A.Yangtsé \nB.Nilo \nC.Amazonas \nD.Mississippi")
Res = input("Ingrese la respuesta: ") 
if Res == "A":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
elif Res == "B":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
elif Res == "C":
    print("Respeusta correcta \nobtuviste 1.0 punto")
    T += 1
elif Res == "D":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
else:
    print("Respuesta no existente\nobtuviste 0 punto")
    T += 0

print("Pregunta 3 \n¿Cuál de los siguientes elementos es un gas noble?")
print("A.Oxígeno \nB.Helio \nC.Hidrógeno \nD.Carbono")
Res = input("Ingrese la respuesta: ") 
if Res == "A":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
elif Res == "B":
    print("Respeusta correcta \nobtuviste 1.0 punto")
    T += 1
elif Res == "C":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
elif Res == "D":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
else:
    print("Respuesta no existente\nobtuviste 0 punto")
    T += 0
print("Pregunta 4 \n¿Quién escribió la famosa novela 'Cien años de soledad'?")
print("A.Gabriel García Márquez \nB.Pablo Neruda \nC.Mario Vargas Llosa \nD.Julio Cortázar")
Res = input("Ingrese la respuesta: ") 
if Res == "A":
    print("Respeusta correcta \nobtuviste 1.0 punto")
    T += 1
elif Res == "B":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
elif Res == "C":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
elif Res == "D":
    print("Respeusta incorrecta \nobtuviste 0.5 punto")
    T += 0.5
else:
    print("Respuesta no existente\nobtuviste 0 punto")
    T += 0

if T > 3:
    print(f"Conseguiste un iphone 18 pro max \nCon un puntaje de {T} ")
elif T == 3:
    print(f"Conseguiste un playstaion 5 \nCon un puntaje de {T} ")
elif T < 3:
    print(f"Conseguiste nada\nCon un puntaje de {T} ")
else:
    print("Error de encuesta \n Realize nuevamente la encuesta")