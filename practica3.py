import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def menu_metodo():
    print("\nSeleccione el metodo de clasificacion:")
    print("1. Distancia Euclideana")
    print("2. Distancia de Mahalanobis")
    print("3. Probabilidad Maxima (Bayes)")
    opcion = input("Ingrese el numero de la opcion: ")
    return {
        '1': 'euclideana',
        '2': 'mahalanobis',
        '3': 'probabilidad'
    }.get(opcion, 'euclideana')

def validar_limites(punto, restriccion):
    return all(restriccion[i][0] <= punto[i] <= restriccion[i][1] for i in range(len(punto)))

def generar_centro_manual(n_dimensiones, restriccion):
    while True:
        centro = [float(input(f"Ingrese coordenada {['X', 'Y', 'Z'][i]} del centro (entre {restriccion[i][0]} y {restriccion[i][1]}): ")) 
                 for i in range(n_dimensiones)]
        if validar_limites(centro, restriccion):
            return centro
        print("Centro fuera de limites. Intente nuevamente.")

def generar_dispersion_manual(clase_num):
    return float(input(f"\nDispersion para clase {clase_num + 1}: "))

def generar_centro_automatico(n_dimensiones, restriccion):
    return [random.uniform(axis[0], axis[1]) for axis in restriccion]

def generar_vectores(centro, n_vectores, dispersion, n_dimensiones, restriccion):
    vectores = []
    for _ in range(n_vectores):
        while True:
            punto = [random.gauss(c, dispersion) for c in centro]
            if validar_limites(punto, restriccion):
                vectores.append(punto)
                break
    return vectores

def calcular_covarianza_manual(vectores, centro_real):
    n = len(vectores)
    dim = len(centro_real)
    cov_matrix = np.zeros((dim, dim))
    
    for punto in vectores:
        diff = np.array(punto) - centro_real
        cov_matrix += np.outer(diff, diff)
    
    if n > 1:
        cov_matrix /= (n - 1)
    return cov_matrix

def generar_clase(n_dimensiones, n_vectores, restriccion, modo, clase_num=None):
    if modo == "manual":
        dispersion = generar_dispersion_manual(clase_num)
        centro = generar_centro_manual(n_dimensiones, restriccion)
    else:
        dispersion = 5
        centro = generar_centro_automatico(n_dimensiones, restriccion)
    
    vectores = generar_vectores(centro, n_vectores, dispersion, n_dimensiones, restriccion)
    vectores_array = np.array(vectores)
    
    centro_real = np.mean(vectores_array, axis=0).tolist()
    cov_matrix = calcular_covarianza_manual(vectores, centro_real)
    
    try:
        inv_cov_matrix = np.linalg.inv(cov_matrix)
    except np.linalg.LinAlgError:
        inv_cov_matrix = np.linalg.pinv(cov_matrix)
    
    return {
        'vectores': vectores,
        'centro': centro_real,
        'dispersion': dispersion,
        'cov_matrix': cov_matrix,
        'inv_cov_matrix': inv_cov_matrix
    }
def clasificar_punto(punto, clases, metodo='euclideana'):
    punto = np.array(punto)
    
    if metodo == 'probabilidad':
        probabilidades = []
        for clase in clases:
            centro = np.array(clase['centro'])
            cov_matrix = clase['cov_matrix']
            inv_cov = clase['inv_cov_matrix']
            diff = punto - centro
            
            # Formula de probabilidad
            d = len(punto)
            det_cov = np.linalg.det(cov_matrix)
            
            if det_cov <= 0:
                prob = 0.0
            else:
                termino_normalizacion = (2 * np.pi)**(d/2) * np.sqrt(det_cov)
                exponente = -0.5 * np.dot(diff.T, np.dot(inv_cov, diff))
                prob = np.exp(exponente) / termino_normalizacion
            
            probabilidades.append(prob)
        
        # Normalizacion y resultados
        prob_total = np.array(probabilidades)
        if np.sum(prob_total) > 0:
            prob_total /= np.sum(prob_total)
        
        print("\nProbabilidades normalizadas:")
        for i, prob in enumerate(prob_total):
            print(f"Clase {i+1}: {prob} : {prob*100:.2f}%")
        
        return np.argmax(prob_total)
    
    else:  # Para Euclideana y Mahalanobis
        distancias = []
        for clase in clases:
            centro = np.array(clase['centro'])
            if metodo == 'euclideana':
                dist = np.linalg.norm(punto - centro)
            else:  # Mahalanobis
                diff = punto - centro
                inv_cov = clase['inv_cov_matrix']
                distancia = np.sqrt(np.dot(diff.T, np.dot(inv_cov, diff)))
                dist = distancia
            distancias.append(dist)
        
        return np.argmin(distancias)

def graficar(punto, clases, clase_idx, restriccion, metodo):
    colores = [
        "blue", "mediumblue", "darkblue", "royalblue", "navy",
        "red", "darkred", "firebrick", "crimson",
        "green", "darkgreen", "forestgreen", "seagreen",
        "darkorange", "chocolate", "saddlebrown",
        "purple", "indigo", "darkviolet", "mediumpurple",
        "gray", "dimgray", "darkgray", "slategray",
        "teal", "darkcyan"]
    random.shuffle(colores)
    fig = plt.figure(figsize=(10, 7))
    titulo_metodo = {
        'euclideana': 'Euclideana',
        'mahalanobis': 'Mahalanobis',
        'probabilidad': 'Probabilidad Maxima'
    }[metodo]
    
    if len(punto) == 2:
        ax = fig.add_subplot()
        ax.set(xlim=restriccion[0], ylim=restriccion[1], 
              xlabel='X', ylabel='Y')
        ax.scatter(punto[0], punto[1], c='black', marker='X', s=200)
    else:
        ax = fig.add_subplot(111, projection='3d')
        ax.set(zlim=restriccion[2], xlabel='X', ylabel='Y', zlabel='Z')
        ax.scatter(punto[0], punto[1], punto[2], c='black', marker='X', s=200)
    
    # Crear leyenda con colores
    handles = []
    labels = []
    
    for i, clase in enumerate(clases):
        datos = np.array(clase['vectores'])
        centro = clase['centro']
        color = colores[i % len(colores)]
        
        # Etiqueta con clase y color
        label = f'Clase {i+1} ({color.capitalize()})'
        
        if len(punto) == 2:
            scatter = ax.scatter(datos[:,0], datos[:,1], c=color, alpha=0.6, label=label)
            ax.scatter(centro[0], centro[1], c=color, marker='s', s=100)
        else:
            scatter = ax.scatter(datos[:,0], datos[:,1], datos[:,2], c=color, alpha=0.6, label=label)
            ax.scatter(centro[0], centro[1], centro[2], c=color, marker='s', s=100)
        
        handles.append(scatter)
        labels.append(label)
        
        # Linea de conexion
        if i == clase_idx:
            linea_color = 'red' if metodo == 'mahalanobis' else 'orange'
            if len(punto) == 2:
                ax.plot([punto[0], centro[0]], [punto[1], centro[1]], 
                        c=linea_color, linestyle='--', linewidth=2)
            else:
                ax.plot([punto[0], centro[0]], [punto[1], centro[1]], [punto[2], centro[2]], 
                        c=linea_color, linestyle='--', linewidth=2)
    
    # Configurar leyenda
    plt.legend(handles, labels, loc='upper left', bbox_to_anchor=(1, 1))
    plt.title(f"Clasificacion usando {titulo_metodo}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    n_dimensiones = int(input("\nIngrese dimension(2/3): "))
    restriccion = [(-100, 100)] * n_dimensiones
    n_clases = int(input("Numero de clases: "))
    n_vectores = int(input("Vectores por clase: "))
    modo = input("Modo de generacion (manual/automatico): ").lower()
    
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
            print("El punto esta fuera del limite :(")
            continue
        
        clase_idx = clasificar_punto(punto, clases, metodo)
        print(f"\nEl punto pertenece a la Clase {clase_idx + 1}")
        graficar(punto, clases, clase_idx, restriccion, metodo)
        
        print("\nQue desea hacer?")
        print("1. Probar otro punto")
        print("2. Cambiar metodo de clasificacion")
        print("3. Salir del programa")
        opcion = input("Ingrese el numero de la opcion: ")
        
        if opcion == '1':
            continue
        elif opcion == '2':
            metodo = menu_metodo()
        elif opcion == '3':
            print("\nAdioss")
            break
        else:
            print("Opcion no valida ;(")

if __name__ == "__main__":
    main()