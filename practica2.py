import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importar herramientas 3D
import math

<<<<<<< HEAD
# Funcion para validar si un punto esta dentro de los limites
=======
# Función para validar si un punto está dentro de los límites
>>>>>>> refs/remotes/origin/main
def validar_limites(punto, restriccion):
    for i in range(len(punto)):
        if not (restriccion[i][0] <= punto[i] <= restriccion[i][1]):
            return False
    return True

<<<<<<< HEAD
# Funcion para generar vectores de manera manual
=======
# Función para generar vectores de manera manual
>>>>>>> refs/remotes/origin/main
def generarVectoresManual(n_dimensiones, n_vectores, dispersion, restriccion):
    vectores = []
    while True:
        if n_dimensiones == 2:
            cx = float(input("Ingrese cx para la clase (entre {} y {}): ".format(restriccion[0][0], restriccion[0][1])))
            cy = float(input("Ingrese cy para la clase (entre {} y {}): ".format(restriccion[1][0], restriccion[1][1])))
            centro = [cx, cy]
        elif n_dimensiones == 3:
            cx = float(input("Ingrese cx para la clase (entre {} y {}): ".format(restriccion[0][0], restriccion[0][1])))
            cy = float(input("Ingrese cy para la clase (entre {} y {}): ".format(restriccion[1][0], restriccion[1][1])))
            cz = float(input("Ingrese cz para la clase (entre {} y {}): ".format(restriccion[2][0], restriccion[2][1])))
            centro = [cx, cy, cz]
        
        if validar_limites(centro, restriccion):
            centro_masa.append(centro)
            break
        else:
<<<<<<< HEAD
            print("El centro de masa esta fuera de los limites :(")
=======
            print("¡El centro de masa está fuera de los límites! Intente nuevamente.")
>>>>>>> refs/remotes/origin/main

    for i in range(n_vectores):
        while True:
            if n_dimensiones == 2:
                vx = (dispersion * random.uniform(-1, 1)) + cx
                vy = (dispersion * random.uniform(-1, 1)) + cy
                punto = [vx, vy]
            elif n_dimensiones == 3:
                vx = (dispersion * random.uniform(-1, 1)) + cx
                vy = (dispersion * random.uniform(-1, 1)) + cy
                vz = (dispersion * random.uniform(-1, 1)) + cz
                punto = [vx, vy, vz]
            
            if validar_limites(punto, restriccion):
                vectores.append(punto)
                break
    return vectores

<<<<<<< HEAD
# Funcion para generar vectores de manera automatica
=======
# Función para generar vectores de manera automática
>>>>>>> refs/remotes/origin/main
def generarVectoresAutomatico(n_dimensiones, n_vectores, dispersion, restriccion):
    vectores = []
    while True:
        if n_dimensiones == 2:
            cx = random.uniform(restriccion[0][0], restriccion[0][1])
            cy = random.uniform(restriccion[1][0], restriccion[1][1])
            centro = [cx, cy]
        elif n_dimensiones == 3:
            cx = random.uniform(restriccion[0][0], restriccion[0][1])
            cy = random.uniform(restriccion[1][0], restriccion[1][1])
            cz = random.uniform(restriccion[2][0], restriccion[2][1])
            centro = [cx, cy, cz]
        
        if validar_limites(centro, restriccion):
            centro_masa.append(centro)
            break

    for i in range(n_vectores):
        while True:
            if n_dimensiones == 2:
                vx = (dispersion * random.uniform(-1, 1)) + cx
                vy = (dispersion * random.uniform(-1, 1)) + cy
                punto = [vx, vy]
            elif n_dimensiones == 3:
                vx = (dispersion * random.uniform(-1, 1)) + cx
                vy = (dispersion * random.uniform(-1, 1)) + cy
                vz = (dispersion * random.uniform(-1, 1)) + cz
                punto = [vx, vy, vz]
            
            if validar_limites(punto, restriccion):
                vectores.append(punto)
                break
    return vectores

<<<<<<< HEAD
# Funcion para generar clases (manual o automatico)
=======
# Función para generar clases (manual o automático)
>>>>>>> refs/remotes/origin/main
def generarClases(n_clases, n_dimensiones, n_vectores, modo, restriccion):
    clases = []
    for i in range(n_clases):
        if modo == "manual":
<<<<<<< HEAD
            dispersion = float(input(f"Ingrese la dispersion para la clase {i + 1}: "))
            aux = generarVectoresManual(n_dimensiones, n_vectores, dispersion, restriccion)
        elif modo == "automatico":
            dispersion = 5  # Dispersion fija para el modo automatico
=======
            dispersion = float(input(f"Ingrese la dispersión para la clase {i + 1}: "))
            aux = generarVectoresManual(n_dimensiones, n_vectores, dispersion, restriccion)
        elif modo == "automatico":
            dispersion = 5  # Dispersión fija para el modo automático
>>>>>>> refs/remotes/origin/main
            aux = generarVectoresAutomatico(n_dimensiones, n_vectores, dispersion, restriccion)
        clases.append(aux)
    return clases

<<<<<<< HEAD
# Funcion para graficar en 2D o 3D
=======
# Función para graficar en 2D o 3D
>>>>>>> refs/remotes/origin/main
def graficar(punto, centro_masa, clase_asignada, restriccion, *clases):
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

<<<<<<< HEAD
    if len(punto) == 2:  # Graficacion en 2D
        fig, ax = plt.subplots()
        fig.suptitle("Clases")
        ax.set_title("Clases")
        ax.set_xlim([restriccion[0][0], restriccion[0][1]])  # Limites del eje X
        ax.set_ylim([restriccion[1][0], restriccion[1][1]])  # Limites del eje Y
        ax.scatter(punto[0], punto[1], color="blue", label="Punto de interes")
=======
    if len(punto) == 2:  # Graficación en 2D
        fig, ax = plt.subplots()
        fig.suptitle("Clases")
        ax.set_title("Clases")
        ax.set_xlim([restriccion[0][0], restriccion[0][1]])  # Límites del eje X
        ax.set_ylim([restriccion[1][0], restriccion[1][1]])  # Límites del eje Y
        ax.scatter(punto[0], punto[1], color="blue", label="Punto de interés")
>>>>>>> refs/remotes/origin/main
        for clase in clases:
            x = [punto[0] for punto in clase]
            y = [punto[1] for punto in clase]
            ax.scatter(x, y, color=colores[i % len(colores)], label=f"Clase {i + 1}")
            i += 1
        centro_asignado = centro_masa[clase_asignada]
<<<<<<< HEAD
        ax.plot([centro_asignado[0], punto[0]], [centro_asignado[1], punto[1]], color="red", label="Distancia mas corta")
        ax.legend()
    else:  # Graficacion en 3D
=======
        ax.plot([centro_asignado[0], punto[0]], [centro_asignado[1], punto[1]], color="red", label="Distancia más corta")
        ax.legend()
    else:  # Graficación en 3D
>>>>>>> refs/remotes/origin/main
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        fig.suptitle("Clases")
        ax.set_title("Clases")
<<<<<<< HEAD
        ax.set_xlim([restriccion[0][0], restriccion[0][1]])  # Limites del eje X
        ax.set_ylim([restriccion[1][0], restriccion[1][1]])  # Limites del eje Y
        ax.set_zlim([restriccion[2][0], restriccion[2][1]])  # Limites del eje Z
        ax.scatter(punto[0], punto[1], punto[2], color="blue", label="Punto de interes")
=======
        ax.set_xlim([restriccion[0][0], restriccion[0][1]])  # Límites del eje X
        ax.set_ylim([restriccion[1][0], restriccion[1][1]])  # Límites del eje Y
        ax.set_zlim([restriccion[2][0], restriccion[2][1]])  # Límites del eje Z
        ax.scatter(punto[0], punto[1], punto[2], color="blue", label="Punto de interés")
>>>>>>> refs/remotes/origin/main
        for clase in clases:
            x = [punto[0] for punto in clase]
            y = [punto[1] for punto in clase]
            z = [punto[2] for punto in clase]
            ax.scatter(x, y, z, color=colores[i % len(colores)], label=f"Clase {i + 1}")
            i += 1
        centro_asignado = centro_masa[clase_asignada]
<<<<<<< HEAD
        ax.plot([centro_asignado[0], punto[0]], [centro_asignado[1], punto[1]], [centro_asignado[2], punto[2]], color="red", label="Distancia mas corta")
        ax.legend()
    plt.show()

# Menu principal
=======
        ax.plot([centro_asignado[0], punto[0]], [centro_asignado[1], punto[1]], [centro_asignado[2], punto[2]], color="red", label="Distancia más corta")
        ax.legend()
    plt.show()

# Menú principal
>>>>>>> refs/remotes/origin/main
def main():
    global centro_masa
    centro_masa = []  # Reiniciar la lista de centros de masa

<<<<<<< HEAD
    n_dimensiones = int(input("Ingrese el numero de dimensiones (2 o 3): "))
    while n_dimensiones not in [2, 3]:
        print("Dimension no valida. Intente nuevamente.")
        n_dimensiones = int(input("Ingrese el numero de dimensiones (2 o 3): "))

    # Definir restricciones segun el numero de dimensiones
    if n_dimensiones == 2:
        restriccion = ((0, 30), (0, 30))  # Limites para X e Y
    elif n_dimensiones == 3:
        restriccion = ((0, 30), (0, 30), (0, 30))  # Limites para X, Y y Z

    n_clases = int(input("Ingrese el numero de clases que quiere: "))
    n_vectores = int(input("Ingrese el numero de vectores que quiere: "))

    modo = input("modo manual o automatico? (manual/automatico): ").lower()
    while modo not in ["manual", "automatico"]:
        print("Modo no valido. Intente nuevamente.")
        modo = input("manual o automatico? (manual/automatico): ").lower()

    vectores = generarClases(n_clases, n_dimensiones, n_vectores, modo, restriccion)

    while True:
        # Ingreso del punto de interes
        while True:
            if n_dimensiones == 2:
                punto = [
                    float(input("Ingrese la coordenada X del punto (entre {} y {}): ".format(restriccion[0][0], restriccion[0][1]))),
                    float(input("Ingrese la coordenada Y del punto (entre {} y {}): ".format(restriccion[1][0], restriccion[1][1])))]
            elif n_dimensiones == 3:
                punto = [
                    float(input("Ingrese la coordenada X del punto (entre {} y {}): ".format(restriccion[0][0], restriccion[0][1]))),
                    float(input("Ingrese la coordenada Y del punto (entre {} y {}): ".format(restriccion[1][0], restriccion[1][1]))),
                    float(input("Ingrese la coordenada Z del punto (entre {} y {}): ".format(restriccion[2][0], restriccion[2][1])))]
            
            if validar_limites(punto, restriccion):
                break
            else:
                print("El punto esta fuera de los limites! :(")

        # Calcular la clase mas cercana
        distancias_a_punto = [math.dist(punto, centro) for centro in centro_masa]
        clase_asignada = distancias_a_punto.index(min(distancias_a_punto))

        print(f"El punto pertenece a la clase {clase_asignada + 1} (centro de masa: {centro_masa[clase_asignada]})")

        # Graficar
        graficar(punto, centro_masa, clase_asignada, restriccion, *vectores)

        # Preguntar si desea probar con otro vector o salir
        opcion = input("Quieres probar con otro vector? (si/no): ").lower()
        if opcion != "si":
            break
=======
    n_dimensiones = int(input("Ingrese el número de dimensiones (2 o 3): "))
    while n_dimensiones not in [2, 3]:
        print("Dimensión no válida. Intente nuevamente.")
        n_dimensiones = int(input("Ingrese el número de dimensiones (2 o 3): "))

    # Definir restricciones según el número de dimensiones
    if n_dimensiones == 2:
        restriccion = ((0, 30), (0, 30))  # Límites para X e Y
    elif n_dimensiones == 3:
        restriccion = ((0, 30), (0, 30), (0, 30))  # Límites para X, Y y Z

    n_clases = int(input("Ingrese el número de clases que quiere: "))
    n_vectores = int(input("Ingrese el número de vectores que quiere: "))

    modo = input("¿Desea el modo manual o automático? (manual/automatico): ").lower()
    while modo not in ["manual", "automatico"]:
        print("Modo no válido. Intente nuevamente.")
        modo = input("¿Desea el modo manual o automático? (manual/automatico): ").lower()

    vectores = generarClases(n_clases, n_dimensiones, n_vectores, modo, restriccion)

    # Ingreso del punto de interés
    while True:
        if n_dimensiones == 2:
            punto = [
                float(input("Ingrese la coordenada X del punto (entre {} y {}): ".format(restriccion[0][0], restriccion[0][1]))),
                float(input("Ingrese la coordenada Y del punto (entre {} y {}): ".format(restriccion[1][0], restriccion[1][1])))]
        elif n_dimensiones == 3:
            punto = [
                float(input("Ingrese la coordenada X del punto (entre {} y {}): ".format(restriccion[0][0], restriccion[0][1]))),
                float(input("Ingrese la coordenada Y del punto (entre {} y {}): ".format(restriccion[1][0], restriccion[1][1]))),
                float(input("Ingrese la coordenada Z del punto (entre {} y {}): ".format(restriccion[2][0], restriccion[2][1])))]
        
        if validar_limites(punto, restriccion):
            break
        else:
            print("¡El punto está fuera de los límites! Intente nuevamente.")

    # Calcular la clase más cercana
    distancias_a_punto = [math.dist(punto, centro) for centro in centro_masa]
    clase_asignada = distancias_a_punto.index(min(distancias_a_punto))

    print(f"El punto pertenece a la clase {clase_asignada + 1} (centro de masa: {centro_masa[clase_asignada]})")

    # Graficar
    graficar(punto, centro_masa, clase_asignada, restriccion, *vectores)

    print("Vectores generados:")
    for i, clase in enumerate(vectores):
        print(f"Clase {i + 1}: {clase}")
>>>>>>> refs/remotes/origin/main

# Ejecutar el programa
if __name__ == "__main__":
    main()