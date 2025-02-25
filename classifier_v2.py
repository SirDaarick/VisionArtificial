import random
n_dimensiones = input("Ingrese el numero de dimensiones")
n_clases = input("Ingrese el numero de clases que quiere")
n_vectores = input("Ingrese el numero de vectores que quiere")

def generarClases(n_dimensiones, n_clases, n_vectores):
    clases = []
    
    for i in range(n_clases): 
        for j in range(n_vectores):
            for k in range(n_dimensiones):
                clases[i][j][k].append(random.randint())
                
    return clases 

print(generarClases(n_dimensiones, n_clases, n_vectores))
                