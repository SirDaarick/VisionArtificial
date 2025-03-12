import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def validar_limites(punto, restriccion):
    for i in range(len(punto)):
        if not (restriccion[i][0] <= punto[i] <= restriccion[i][1]):
            return False
    return True

def generar_centro_manual(n_dimensiones, restriccion):
    while True:
        centro = []
        for i in range(n_dimensiones):
            valor = float(input(f"Ingrese coordenada {['X', 'Y', 'Z'][i]} del centro (entre {restriccion[i][0]} y {restriccion[i][1]}): "))
            centro.append(valor)
        
        if validar_limites(centro, restriccion):
            return centro
        print("El centro está fuera de los límites. Intente nuevamente.")

def generar_centro_automatico(n_dimensiones, restriccion):
    centro = [random.uniform(axis[0], axis[1]) for axis in restriccion]
    return centro

def generar_vectores(centro, n_vectores, dispersion, n_dimensiones, restriccion):
    vectores = []
    for _ in range(n_vectores):
        while True:
            punto = [(dispersion * random.uniform(-1, 1)) + c for c in centro]
            if validar_limites(punto, restriccion):
                vectores.append(punto)
                break
    return vectores

def generar_clase_manual(n_dimensiones, n_vectores, dispersion, restriccion):
    centro = generar_centro_manual(n_dimensiones, restriccion)
    vectores = generar_vectores(centro, n_vectores, dispersion, n_dimensiones, restriccion)
    return vectores, centro

def generar_clase_automatico(n_dimensiones, n_vectores, restriccion):
    dispersion = 5
    centro = generar_centro_automatico(n_dimensiones, restriccion)
    vectores = generar_vectores(centro, n_vectores, dispersion, n_dimensiones, restriccion)
    return vectores, centro

def generar_clases(modo, n_clases, n_dimensiones, n_vectores, restriccion):
    clases = []
    centros_masa = []
    
    for i in range(n_clases):
        if modo == "manual":
            dispersion = float(input(f"Ingrese dispersión para clase {i+1}: "))
            vectores, centro = generar_clase_manual(n_dimensiones, n_vectores, dispersion, restriccion)
        else:
            vectores, centro = generar_clase_automatico(n_dimensiones, n_vectores, restriccion)
        
        clases.append(vectores)
        centros_masa.append(centro)
    
    return clases, centros_masa

def obtener_punto(n_dimensiones, restriccion):
    while True:
        punto = []
        for i in range(n_dimensiones):
            valor = float(input(f"Ingrese coordenada {['X', 'Y', 'Z'][i]} (entre {restriccion[i][0]} y {restriccion[i][1]}): "))
            punto.append(valor)
        
        if validar_limites(punto, restriccion):
            return punto
        print("Punto fuera de los límites. Intente nuevamente.")

def calcular_clase_cercana(punto, centros_masa):
    distancias = [math.dist(punto, centro) for centro in centros_masa]
    return distancias.index(min(distancias))

def graficar(punto, centros_masa, clase_idx, restriccion, clases):
    colores = ["blue", "red", "green", "purple", "orange", "cyan", "magenta", "yellow", "black", "brown"]
    fig = plt.figure()
    
    if len(punto) == 2:
        ax = fig.add_subplot()
        ax.set_xlim(restriccion[0])
        ax.set_ylim(restriccion[1])
        ax.scatter(punto[0], punto[1], c='black', marker='x', s=100)
    else:
        ax = fig.add_subplot(111, projection='3d')
        ax.set_zlim(restriccion[2])
        ax.scatter(punto[0], punto[1], punto[2], c='black', marker='x', s=100)
    
    ax.set_xlim(restriccion[0])
    ax.set_ylim(restriccion[1])
    plt.title("Clasificación de Puntos")

    for i, (clase, centro) in enumerate(zip(clases, centros_masa)):
        datos = list(zip(*clase))
        if len(punto) == 2:
            ax.scatter(datos[0], datos[1], c=colores[i%10], label=f'Clase {i+1}')
            ax.plot([centro[0], punto[0]], [centro[1], punto[1]], c='gray', linestyle='--')
        else:
            ax.scatter(datos[0], datos[1], datos[2], c=colores[i%10], label=f'Clase {i+1}')
            ax.plot([centro[0], punto[0]], [centro[1], punto[1]], [centro[2], punto[2]], c='gray', linestyle='--')
        
        ax.scatter(centro[0], centro[1], centro[2] if len(centro)==3 else 0, 
                c=colores[i%10], marker='s', s=50, edgecolor='black')
    
    plt.legend()
    plt.show()

def main():
    # Configuración inicial
    n_dimensiones = int(input("Ingrese dimensiones (2/3): "))
    restriccion = [(0, 30)] * n_dimensiones
    n_clases = int(input("Número de clases: "))
    n_vectores = int(input("Vectores por clase: "))
    modo = input("Modo (manual/automatico): ").lower()

    # Generar clases
    clases, centros_masa = generar_clases(modo, n_clases, n_dimensiones, n_vectores, restriccion)

    # Bucle principal
    while True:
        punto = obtener_punto(n_dimensiones, restriccion)
        clase_idx = calcular_clase_cercana(punto, centros_masa)
        print(f"El punto pertenece a la clase {clase_idx + 1}")
        graficar(punto, centros_masa, clase_idx, restriccion, clases)
        
        if input("¿Probar otro punto? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    main()