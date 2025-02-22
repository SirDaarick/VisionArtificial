clases = {
    "c1" : ((1,2), (2,3), (0,2), (1,1), (2,2)),
    "c2" :((6,7), (7,6), (5,7), (6,8), (7,7)),
    "c3" : ((11,12), (12,11), (10,12), (11,10), (12,12)),
    "c4" : ((16,5), (15,6), (16,4), (17,5), (15,5)),
    "c5" : ((21,16), (22,15), (20,16), (21,17), (22,16))
}

alumno = (11,9)

clases.update()


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

def clasificar(alumno, clases) :
    distancias = []
    for i in clases :
        distancias.append(distancia(alumno, centro_masa(clases[i])))

                
    minimo = min(distancias)
    
    
    
    return minimo

print(clasificar(alumno, clases))