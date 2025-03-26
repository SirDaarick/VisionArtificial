import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Funciones de clasificación
def menu_metodo():
    print("\nSeleccione el método de clasificación:")
    print("1. Distancia Euclideana")
    print("2. Distancia de Mahalanobis")
    print("3. Máxima Probabilidad")
    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == '1':
        return 'euclideana'
    elif opcion == '2':
        return 'mahalanobis'
    elif opcion == '3':
        return 'maxima_probabilidad'
    else:
        raise ValueError("Opción no válida.")

def calcular_covarianza_manual(vectores, centro_real):
    n = len(vectores)  # Número de observaciones
    dim = len(centro_real)  # Número de dimensiones
    cov_matrix = np.zeros((dim, dim))  # Inicializar matriz de ceros
    
    for punto in vectores:
        diff = np.array(punto) - centro_real  # Diferencia con la media
        cov_matrix += np.outer(diff, diff)  # Producto externo y acumular
    
    if n > 1:
        cov_matrix /= (n - 1)  # Normalizar por n-1 (covarianza muestral)
    
    return cov_matrix

def clasificar_euclideana(punto, clases):
    distancias = []
    punto = np.array(punto)
    
    for clase in clases:
        centro = np.array(clase['centro_rgb'])
        dist = np.linalg.norm(punto - centro)  # Distancia euclidiana
        distancias.append(dist)
    
    return np.argmin(distancias), distancias

def clasificar_mahalanobis(punto, clases):
    distancias = []
    punto = np.array(punto)
    
    for clase in clases:
        centro = np.array(clase['centro_rgb'])
        inv_cov = clase['inv_cov_matrix']
        diff = punto - centro
        mahalanobis = np.dot(diff.T, np.dot(inv_cov, diff))  # Distancia de Mahalanobis
        dist = np.sqrt(mahalanobis)
        distancias.append(dist)
    
    return np.argmin(distancias), distancias

def clasificar_maxima_probabilidad(punto, clases):
    probabilidades = []
    punto = np.array(punto)
    
    for clase in clases:
        centro = np.array(clase['centro_rgb'])
        cov_matrix = np.array(clase['cov_matrix'])
        inv_cov_matrix = np.array(clase['inv_cov_matrix'])
        diff = punto - centro
        
        # Calcular exponente de la PDF
        exponente = -0.5 * np.dot(diff.T, np.dot(inv_cov_matrix, diff))
        
        # Calcular factor normalizador
        d = len(centro)  # Número de dimensiones
        factor_normalizador = 1 / ((2 * np.pi) ** (d / 2) * np.sqrt(np.linalg.det(cov_matrix)))
        
        # Calcular probabilidad
        probabilidad = factor_normalizador * np.exp(exponente)
        probabilidades.append(probabilidad)
    
    # Normalizar las probabilidades para que sumen 1
    suma_probabilidades = sum(probabilidades)
    probabilidades_normalizadas = [p / suma_probabilidades for p in probabilidades]
    
    return np.argmax(probabilidades_normalizadas), probabilidades_normalizadas

def clasificar_punto(punto, clases, metodo='euclideana'):
    if metodo == 'euclideana':
        return clasificar_euclideana(punto, clases)
    elif metodo == 'mahalanobis':
        return clasificar_mahalanobis(punto, clases)
    elif metodo == 'maxima_probabilidad':
        return clasificar_maxima_probabilidad(punto, clases)
    else:
        raise ValueError("Método de clasificación no válido.")

def menu_principal():
    print("\n¿Qué deseas hacer?")
    print("1. Graficar otro punto (usar el mismo método)")
    print("2. Cambiar el método de clasificación")
    print("3. Salir del programa")
    opcion = input("Ingrese el número de la opción: ")
    return opcion

# Cargar la imagen
ruta_imagen = "paisaje.jpg"
imagen = Image.open(ruta_imagen)
imagen = np.array(imagen)

# Preguntar al usuario cuántas clases desea crear
num_clases = int(input("¿Cuántas clases deseas crear? "))

# Preguntar cuántos puntos aleatorios desea generar por clase
num_puntos_por_clase = int(input("¿Cuántos puntos aleatorios deseas generar por clase? "))

# Lista para almacenar los puntos de todas las clases
clases = []

# Lista de colores para cada clase
colores = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'orange', 'purple', 'pink', 'brown']

# Mostrar la imagen y permitir al usuario seleccionar regiones para cada clase
plt.figure(1)
plt.imshow(imagen)
plt.title("Selecciona dos esquinas para cada clase")
plt.axis("on")

for i in range(num_clases):
    print(f"Selecciona dos esquinas para la clase {i + 1}")
    points = plt.ginput(2)  # Esperar a que el usuario seleccione dos puntos
    x_min, y_min = min(points[0][0], points[1][0]), min(points[0][1], points[1][1])
    x_max, y_max = max(points[0][0], points[1][0]), max(points[0][1], points[1][1])
    ancho = x_max - x_min
    alto = y_max - y_min

    # Dibujar el rectángulo en la imagen
    rect = plt.Rectangle((x_min, y_min), ancho, alto, edgecolor=colores[i], linewidth=2, fill=False)
    plt.gca().add_patch(rect)

    # Generar puntos aleatorios dentro de la región seleccionada
    x_rand = x_min + ancho * np.random.rand(num_puntos_por_clase)
    y_rand = y_min + alto * np.random.rand(num_puntos_por_clase)
    x_rand = x_rand.astype(int)
    y_rand = y_rand.astype(int)

    # Graficar los puntos aleatorios con el color correspondiente a la clase
    scatter = plt.scatter(x_rand, y_rand, c=colores[i], marker='o', s=50, edgecolor='black', label=f"Clase {i + 1}")

    # Extraer los valores RGB de los puntos generados
    rgb = imagen[y_rand, x_rand]
    int_rgb = [[int(c) for c in pixel] for pixel in rgb]  # Convertir a enteros

    # Calcular el centroide en el espacio RGB
    centro_rgb = np.mean(int_rgb, axis=0)

    # Calcular la matriz de covarianza y su inversa
    cov_matrix = calcular_covarianza_manual(int_rgb, centro_rgb)
    inv_cov_matrix = np.linalg.inv(cov_matrix)

    # Almacenar la información de la clase
    clases.append({
        'puntos': int_rgb,
        'centro_rgb': centro_rgb,  # Centro en el espacio RGB
        'cov_matrix': cov_matrix,
        'inv_cov_matrix': inv_cov_matrix
    })

    # Actualizar la gráfica después de cada clase
    plt.draw()
    plt.pause(0.1)

# Mostrar la leyenda con los colores de cada clase
plt.legend()
plt.title("Puntos aleatorios generados para todas las clases")

# Pedir al usuario que coloque un punto en la gráfica
print("\nAhora, coloca un punto en la gráfica haciendo clic.")
punto_usuario = plt.ginput(1)  # Capturar un solo clic del usuario
x_usuario, y_usuario = int(punto_usuario[0][0]), int(punto_usuario[0][1])

# Graficar el punto del usuario
punto_anterior = plt.scatter(x_usuario, y_usuario, c='black', marker='x', s=100, linewidths=2, label="Punto del usuario")

# Extraer el valor RGB del punto del usuario
rgb_usuario = imagen[y_usuario, x_usuario]
rgb_usuario = [int(c) for c in rgb_usuario]  # Convertir a enteros

# Actualizar la gráfica
plt.legend()
plt.draw()
plt.pause(0.1)

# Seleccionar el método de clasificación
metodo = menu_metodo()

# Bucle principal del programa
texto_clase = None  # Para almacenar el texto de la clase asignada
while True:
    # Clasificar el punto del usuario
    if metodo == 'euclideana':
        clase_asignada, distancias = clasificar_punto(rgb_usuario, clases, metodo)
        print(f"\nEl punto del usuario ha sido clasificado en la Clase {clase_asignada + 1} usando el método {metodo}.")
        print("\nDistancias Euclideanas a cada clase:")
        for i, distancia in enumerate(distancias):
            print(f"Clase {i + 1}: {distancia:.2f}")
    elif metodo == 'mahalanobis':
        clase_asignada, distancias = clasificar_punto(rgb_usuario, clases, metodo)
        print(f"\nEl punto del usuario ha sido clasificado en la Clase {clase_asignada + 1} usando el método {metodo}.")
        print("\nDistancias de Mahalanobis a cada clase:")
        for i, distancia in enumerate(distancias):
            print(f"Clase {i + 1}: {distancia:.2f}")
    elif metodo == 'maxima_probabilidad':
        clase_asignada, probabilidades = clasificar_punto(rgb_usuario, clases, metodo)
        print(f"\nEl punto del usuario ha sido clasificado en la Clase {clase_asignada + 1} usando el método {metodo}.")
        print("\nProbabilidades de pertenencia a cada clase (normalizadas):")
        for i, probabilidad in enumerate(probabilidades):
            print(f"Clase {i + 1}: {probabilidad:.6f}")

    # Imprimir los centroides de cada clase
    print("\nCentroides de cada clase (en espacio RGB):")
    for i, clase in enumerate(clases):
        print(f"Clase {i + 1}: {clase['centro_rgb']}")

    # Mostrar la clase asignada en la gráfica
    if texto_clase:
        texto_clase.remove()  # Eliminar el texto anterior si existe
    texto_clase = plt.text(x_usuario + 10, y_usuario + 10, f"Clase {clase_asignada + 1}", fontsize=12, color='black',
                           bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))

    # Actualizar la gráfica
    plt.draw()
    plt.pause(0.1)

    # Mostrar el menú principal
    opcion = menu_principal()

    if opcion == '1':
        # Borrar el punto anterior
        punto_anterior.remove()
        # Pedir al usuario que coloque un nuevo punto en la gráfica
        print("\nAhora, coloca un punto en la gráfica haciendo clic.")
        punto_usuario = plt.ginput(1)  # Capturar un solo clic del usuario
        x_usuario, y_usuario = int(punto_usuario[0][0]), int(punto_usuario[0][1])

        # Graficar el nuevo punto del usuario
        punto_anterior = plt.scatter(x_usuario, y_usuario, c='black', marker='x', s=100, linewidths=2, label="Punto del usuario")

        # Extraer el valor RGB del nuevo punto del usuario
        rgb_usuario = imagen[y_usuario, x_usuario]
        rgb_usuario = [int(c) for c in rgb_usuario]  # Convertir a enteros

        # Actualizar la gráfica
        plt.legend()
        plt.draw()
        plt.pause(0.1)
    elif opcion == '2':
        # Cambiar el método de clasificación
        metodo = menu_metodo()
    elif opcion == '3':
        # Salir del programa
        print("¡Gracias por usar el programa!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

# Mantener la gráfica abierta hasta que el usuario la cierre
plt.show()