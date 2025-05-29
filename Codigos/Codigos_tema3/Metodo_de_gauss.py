import numpy as np

def gauss_elimination(A, b):
    """
    Función para resolver un sistema de ecuaciones lineales utilizando el Método de Gauss.

    Parámetros:
    A (numpy.ndarray): Matriz de coeficientes del sistema.
    b (numpy.ndarray): Vector de términos independientes.

    Devuelve:
    numpy.ndarray: Vector de soluciones del sistema.
    """
    n = len(b)
    
    # Eliminación gaussiana
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            b[j] -= factor * b[i]
            A[j, i:] -= factor * A[i, i:]
    
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x

# Ejemplo de sistema de ecuaciones lineales
A = np.array([[2, -1, 1],
              [3, 3, 9],
              [3, 3, 5]], dtype=float)
b = np.array([2, 15, 10], dtype=float)

# Resolver el sistema de ecuaciones lineales utilizando el Método de Gauss
solucion = gauss_elimination(A, b)

# Imprimir resultado
print("Solución encontrada:", solucion)