# Método de Gauss
## Definición
El Método de Gauss es un algoritmo utilizado para resolver sistemas de ecuaciones lineales mediante la eliminación de incógnitas.

![](https://github.com/TuUsuario/TuRepositorio/blob/main/Imagenes/gauss_method.png)

## Algoritmo
1. Convertir el sistema de ecuaciones lineales en una matriz aumentada.
2. Aplicar eliminación gaussiana para convertir la matriz en una forma escalonada.
3. Aplicar sustitución hacia atrás para obtener las soluciones del sistema.

## Metodología

### Código en Python para el Método de Gauss
A continuación, se presenta un ejemplo de código en Python para aplicar el Método de Gauss en un sistema de ecuaciones lineales.

```python
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
```

### Resultados y Análisis
El código anterior aplica el Método de Gauss para resolver el sistema de ecuaciones lineales \(Ax = b\), donde \(A\) es una matriz de coeficientes y \(b\) es un vector de términos independientes. Se obtiene un vector de soluciones que satisface el sistema dado.

