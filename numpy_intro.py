import numpy as np

""" Numpy Arrays normales """
arr_1 = np.array([1, 2, 3, 4, 5])

arr_2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ])

arr_1[2] = 99
arr_2[1][2] = 111

arr_2.shape = (1, 9)

""" Data Types """
arr_int8 = np.array([11, 22, 33, 44, 55, 66, 77, 88, 127], dtype='int8')


""" Arreglos Automáticos Comunes """
ceros_1 = np.zeros(3)
ceros_2 = np.zeros((2, 2))

unos_1 = np.ones((4, 5))

identidad = np.identity(4)
eye_matrix = np.eye(3, 4)

a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
unos_2 = np.ones_like(a)

pasos_1 = np.arange(11, 100, 11)
pasos_2 = np.arange(11, 100, 11).reshape((3, 3))

lineal = np.linspace(0, 1, 10) # Arreglo de distribución uiforme

aleatorios = np.random.random(100)
aleatorios *= 5

""" Atributos y Propiedades de los Arreglos """
arr_3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype='uint16')
print("\n------ Propiedades de los Arreglos ------")
print(f"Forma (shape): {arr_3.shape}")
print(f"Dimensiones (ndim): {arr_3.ndim}")
print(f"Tipo de Datos (dtype): {arr_3.dtype}")
print(f"Número total de elementos (size): {arr_3.size}")

""" Operaciones Matemáticas """
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

print("\n------ Operaciones Matemáticas ------")
print(f"Suma: {arr1 + arr2}")
print(f"Multiplicación: {arr1 * arr2}")
print(f"Potencia: {arr1**2}")
print(f"Seno: {np.sin(np.radians(arr2))}")

arr3 = np.arange(1, 10).reshape((3, 3))
arr4 = np.arange(11, 100, 11).reshape((3, 3))

print(f"\nSuma: {arr3 + arr4}")
print(f"Multiplicación: {arr3 * arr4}")
print(f"Potencia: {arr3**2}")
print(f"Coseno: {np.cos(np.radians(arr4))}")


""" Indexación y Slicing (Rebanado) """
matriz = np.array([
    [10, 20, 30], 
    [40, 50, 60], 
    [70, 80, 90]
    ])

print(matriz[1, 2], end="\n\n")
print(matriz[0, :], end="\n\n")
print(matriz[:, 1], end="\n\n")
print(matriz[:2, :2], end="\n\n")

""" Manipulaicón de Dimensiones (Rshaping) """
original = np.arange(12)
reestructurado = original.reshape((3, 4))
transpuesta = reestructurado.T



""" Estadística y Agregación """
print("\n----- Estadística -----")

data = np.array([[1, 2], [3, 4]])
print("Sumatoria", np.sum(data))
print("Promedio", np.mean(data))
print("Desviación Estándar", np.std(data))
print("Suma por columnas", np.sum(data, axis=0))
print("Suma por filas", np.sum(data, axis=1))
print("Máximo ", np.max(data)," y Mínimo", np.min(data))


""" Máscaras Booleanas """
numeros = np.array([1, 15, 8, 20, 3, 12, 10])
mayores_a10 = numeros[numeros > 10]
print(mayores_a10)


""" Más funciones """
numeros.sort()
print(numeros)

a = np.array([11, 22, 33, 44])
b = np.array([55, 66, 77, 88])

print(np.concatenate((b, a)))

a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])

print(np.vstack((a1, a2)))
print(np.hstack((a1, a2)))

a = np.array([11, 11, 22, 33, 44, 11, 55, 33, 44, 33, 11, 99])

print(np.unique(a))




