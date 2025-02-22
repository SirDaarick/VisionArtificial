import matplotlib.pyplot as plt
import random

c1 = ((1,2), (2,3), (0,2), (1,1), (2,2))
c2 = ((6,7), (7,6), (5,7), (6,8), (7,7))
c3 = ((11,12), (12,11), (10,12), (11,10), (12,12))
c4 = ((16,5), (15,6), (16,4), (17,5), (15,5))
c5 = ((21,16), (22,15), (20,16), (21,17), (22,16))
restriccion = ((0,30), (0,30)) #Restricciones X, Restricciones Y
#alumno = (11,9)


def centro_masa(vectores):
    sumatoria = [0,0]
    centro = [0,0]
    for vector in vectores :
        sumatoria[0] += vector[0]
        sumatoria[1] += vector[1]
    
    centro[0] = sumatoria[0] / len(vectores)
    centro[1] = sumatoria[1] / len(vectores)
    
    return centro 


def distancia(punto, centro):
    return (((centro[0]-punto[0])**2) + ((centro[1]-punto[1])**2))**(1/2)


def clasificar(alumno, *clases) :
    distancias = []
    for i in clases :
        distancias.append(distancia(alumno, centro_masa(i)))

    return distancias.index(min(distancias)) + 1
    # esto retorna los vectores de la clase a la que pertenece el
    # vector que se ingreso     
    #return clases[distancias.index(min(distancias))]

def pedirVector():
    x = int(input("Ingrese la componente X de su vector:"))
    y = int(input("Ingrese la componente Y de su vector:"))
    alumno = [x, y]
    if((restriccion[0][1] >= alumno[0] >= restriccion[0][0]) and (restriccion[1][1] >= alumno[1] >= restriccion[1][0])):
        return alumno
    else:
        print("Su vector no pertenece a ninguna clase :(")
        return pedirVector()

def graficar(restriccion, punto, clase_asignada, *clases ):
    i = 0
    colores = [
    "blue", "mediumblue", "darkblue", "royalblue", "navy",
    "red", "darkred", "firebrick", "crimson",
    "green", "darkgreen", "forestgreen", "seagreen",
    "darkorange", "chocolate", "saddlebrown",
    "purple", "indigo", "darkviolet", "mediumpurple",
    "gray", "dimgray", "darkgray", "slategray",
    "teal", "darkcyan"]
    random.shuffle(colores)
    fig, ax = plt.subplots()
    fig.suptitle("Clases")
    ax.set_title("Clases")
    ax.set_xlim([restriccion[0][0], restriccion[0][1]])  # Límites del eje X
    ax.set_ylim([restriccion[1][0], restriccion[1][1]])  # Límites del eje Y
    ax.scatter(punto[0], punto[1], color = "blue", label = "Alumno")
    for clase in clases : 
        x = [punto[0] for punto in clase]
        y = [punto[1] for punto in clase]
        ax.scatter(x, y, color = colores[i % len(colores)], label = f"Clase {i + 1}")
        i+=1
    centro_asignado = centro_masa(clase_asignada)
    ax.plot([centro_asignado[0], punto[0]], [centro_asignado[1], punto[1]], color = "red", label = "asignado")
    ax.legend()
    plt.show()




stop = 0

while(stop != 1):
    
    alumno = pedirVector()
    indice_clase = clasificar(alumno, c1, c2, c3, c4, c5)
    clase_asignada = (c1,c2,c3,c4,c5)[indice_clase - 1]
    print(f"El vector pertenece a la clase {indice_clase}")
    graficar(restriccion, alumno,clase_asignada, c1, c2, c3, c4, c5)
    print(f"El vector pertenece a la clase {indice_clase}")
    pregunta = input("Quieres clasificar otro vector? (S/N)")
    if pregunta.lower() == 'n':
        stop = 1
    else:
        stop = 0
