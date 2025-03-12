import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def menu_metodo():
    print("\nSeleccione el método de clasificación:")
    print("1. Distancia Euclideana")
    print("2. Distancia de Mahalanobis")
    opcion = input("Ingrese el número de la opción: ")
    return 'euclideana' if opcion == '1' else 'mahalanobis'

def validar_limites(punto, restriccion):
    return all(restriccion[i][0] <= punto[i] <= restriccion[i][1] for i in range(len(punto)))

def generar_centro_manual(n_dimensiones, restriccion):
    while True:
        centro = [float(input(f"Ingrese coordenada {['X', 'Y', 'Z'][i]} del centro (entre {restriccion[i][0]} y {restriccion[i][1]}): ")) 
                 for i in range(n_dimensiones)]
        if validar_limites(centro, restriccion):
            return centro
        print("Centro fuera de límites. Intente nuevamente.")

def generar_dispersión_manual(clase_num):
    return float(input(f"\nDispersión para clase {clase_num + 1}: "))

def generar_centro_automatico(n_dimensiones, restriccion):
    return [random.uniform(axis[0], axis[1]) for axis in restriccion]

def generar_vectores(centro, n_vectores, dispersion, n_dimensiones, restriccion):
    vectores = []
    for _ in range(n_vectores):
        while True:
            punto = [(dispersion * random.gauss(0, 1)) + c for c in centro]
            if validar_limites(punto, restriccion):
                vectores.append(punto)
                break
    return vectores

def generar_clase(n_dimensiones, n_vectores, restriccion, modo, clase_num=None):
    if modo == "manual":
        dispersion = generar_dispersión_manual(clase_num)
        centro = generar_centro_manual(n_dimensiones, restriccion)
    else:
        dispersion = 5
        centro = generar_centro_automatico(n_dimensiones, restriccion)
    
    vectores = generar_vectores(centro, n_vectores, dispersion, n_dimensiones, restriccion)
    cov_matrix = np.cov(np.array(vectores).T)
    try:
        inv_cov_matrix = np.linalg.inv(cov_matrix)
    except np.linalg.LinAlgError:
        inv_cov_matrix = np.linalg.pinv(cov_matrix)
    
    return {
        'vectores': vectores,
        'centro': centro,
        'dispersion': dispersion,
        'cov_matrix': cov_matrix,
        'inv_cov_matrix': inv_cov_matrix
    }

def clasificar_punto(punto, clases, metodo):
    distancias = []
    for clase in clases:
        if metodo == 'euclideana':
            dist = math.dist(punto, clase['centro'])
        else:
            diff = np.array(punto) - np.array(clase['centro'])
            dist = np.sqrt(np.dot(np.dot(diff, clase['inv_cov_matrix']), diff.T))
        distancias.append(dist)
    return np.argmin(distancias)

def graficar(punto, clases, clase_idx, restriccion, metodo):
    colores = ["blue", "green", "red", "purple", "orange", "cyan", "magenta"]
    fig = plt.figure(figsize=(10, 7))
    
    if len(punto) == 2:
        ax = fig.add_subplot()
        ax.set(xlim=restriccion[0], ylim=restriccion[1], 
              xlabel='X', ylabel='Y')
        ax.scatter(punto[0], punto[1], c='black', marker='X', s=200)
    else:
        ax = fig.add_subplot(111, projection='3d')
        ax.set(zlim=restriccion[2], xlabel='X', ylabel='Y', zlabel='Z')
        ax.scatter(punto[0], punto[1], punto[2], c='black', marker='X', s=200)
    
    for i, clase in enumerate(clases):
        datos = np.array(clase['vectores'])
        centro = clase['centro']
        
        if len(punto) == 2:
            ax.scatter(datos[:,0], datos[:,1], c=colores[i], alpha=0.6, 
                      label=f'Clase {i+1} (σ={clase["dispersion"]})')
            ax.scatter(centro[0], centro[1], c=colores[i], marker='s', s=100)
        else:
            ax.scatter(datos[:,0], datos[:,1], datos[:,2], c=colores[i], alpha=0.6)
            ax.scatter(centro[0], centro[1], centro[2], c=colores[i], marker='s', s=100)
        
        if i == clase_idx:
            linea_color = 'red' if metodo == 'mahalanobis' else 'orange'
            if len(punto) == 2:
                ax.plot([punto[0], centro[0]], [punto[1], centro[1]], 
                        c=linea_color, linestyle='--', linewidth=2)
            else:
                ax.plot([punto[0], centro[0]], [punto[1], centro[1]], [punto[2], centro[2]], 
                        c=linea_color, linestyle='--', linewidth=2)
    
    plt.title(f"Clasificación usando Distancia {metodo.capitalize()}")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("¡Bienvenido al Sistema de Clasificación Multidimensional!")
    n_dimensiones = int(input("\nIngrese dimensión del espacio (2/3): "))
    restriccion = [(0, 30)] * n_dimensiones
    n_clases = int(input("Número de clases: "))
    n_vectores = int(input("Vectores por clase: "))
    modo = input("Modo de generación (manual/automatico): ").lower()
    
    clases = []
    for i in range(n_clases):
        print(f"\nConfigurando Clase {i+1}:")
        clase = generar_clase(n_dimensiones, n_vectores, restriccion, modo, i)
        clases.append(clase)
    
    metodo = menu_metodo()
    
    while True:
        print("\n" + "-"*50)
        punto = [float(input(f"Ingrese coordenada {['X', 'Y', 'Z'][i]} del punto: ")) for i in range(n_dimensiones)]
        
        if not validar_limites(punto, restriccion):
            print("¡Punto fuera de los límites del espacio!")
            continue
        
        clase_idx = clasificar_punto(punto, clases, metodo)
        print(f"\nEl punto pertenece a la Clase {clase_idx + 1}")
        graficar(punto, clases, clase_idx, restriccion, metodo)
        
        continuar = input("\n¿Probar otro punto? (s/n): ").lower()
        if continuar != 's':
            cambiar_metodo = input("¿Quieres probar otro método de clasificación? (s/n): ").lower()
            if cambiar_metodo == 's':
                metodo = menu_metodo()
            else:
                break

if __name__ == "__main__":
    main()
