import random
n_dimensiones = input("Ingrese el numero de dimensiones")
n_clases = input("Ingrese el numero de clases que quiere")
n_vectores = input("Ingrese el numero de vectores que quiere")
centro_masa = []

def generarVectores(n_dimensiones, n_vectores, dispersion):
    vectores = []
    if n_dimensiones == 2:
        cx = int(input("Ingrese cx para la clase "))
        cy = int(input("Ingrese cy para la clase "))
        centro_masa.append([cx, cy])
        for i in range(n_vectores):
            vx = (dispersion * random.uniform(-1,1)) + cx
            vy = (dispersion * random.uniform(-1,1)) + cy
            aux = [round(vx,2), round(vy,2)]
            vectores.append(aux)
    elif n_dimensiones == 3:
        cx = int(input("Ingrese cx para la clase "))
        cy = int(input("Ingrese cy para la clase "))
        cz = int(input("Ingrese cz para la clase "))
        centro_masa.append([cx, cy, cz])
        for i in range(n_vectores):
            vx = (dispersion * random.uniform(-1,1)) + cx
            vy = (dispersion * random.uniform(-1,1)) + cy
            vz = (dispersion * random.uniform(-1,1)) + cz
            aux = [round(vx, 2), round(vy, 2), round(vz, 2)]
            vectores.append(aux)
    else: 
        print("Ingrese una dimension 2 o 3")
    return vectores

def generarClases(n_clases, n_dimensiones, n_vectores):
    clases = []
    for i in range(n_clases):
        dispersion = int(input("Ingrese la dispersion para la clase"))
        aux = generarVectores(n_dimensiones, n_vectores, dispersion)
        clases.append(aux)
    return clases

def distancias(centro, punto, dimension):
    if dimension == 2 :
        return (((centro[0]-punto[0])**2) + ((centro[1]-punto[1])**2))**(1/2)





vectores = generarClases(n_clases, n_dimensiones, n_vectores)

print(*vectores)