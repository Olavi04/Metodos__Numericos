# Método de Gauss-Seidel
## Definición
El método de Gauss-Seidel es un algoritmo iterativo utilizado para resolver sistemas de ecuaciones lineales. Este método es una variante del método de Jacobi que aprovecha las soluciones ya calculadas en las iteraciones actuales para mejorar la convergencia.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/gauss_seidel.png)

## Algoritmo
1. Inicializar las soluciones \(x_0^{(0)}, x_1^{(0)}, ..., x_n^{(0)}\) de manera arbitraria o utilizando valores aproximados.
2. Para cada ecuación \(i\) en el sistema, calcular \(x_i^{(k+1)}\) utilizando las soluciones calculadas en la iteración \(k\).
3. Repetir el paso 2 hasta que se satisfaga un criterio de convergencia (por ejemplo, la diferencia entre dos iteraciones consecutivas sea menor que una tolerancia predefinida).

## Metodología

### Código en Python para el Método de Gauss-Seidel
A continuación, se presenta un ejemplo de código en Python para aplicar el método de Gauss-Seidel en un sistema de ecuaciones lineales.

```python
import numpy as np

def gauss_seidel(A, b, x0, tol, Nmax):
    """
    Función para resolver un sistema de ecuaciones lineales utilizando el método de Gauss-Seidel.

    Parámetros:
    A (numpy.ndarray): Matriz de coeficientes del sistema.
    b (numpy.ndarray): Vector de términos independientes.
    x0 (numpy.ndarray): Vector de soluciones inicial.
    tol (float): Tolerancia para la convergencia.
    Nmax (int): Número máximo de iteraciones.

    Devuelve:
    numpy.ndarray: Vector de soluciones aproximado.
    int: Número de iteraciones realizadas.
    bool: Indicador de convergencia.
    """
    n = len(b)
    x = x0.copy()
    convergencia = False

    for k in range(Nmax):
        x_ant = x.copy()
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += A[i, j] * x[j]
            x[i] = (b[i] - suma) / A[i, i]
        
        # Criterio de convergencia
        if np.linalg.norm(x - x_ant) < tol:
            convergencia = True
            break
    
    return x, k+1, convergencia

# Ejemplo de sistema de ecuaciones lineales
A = np.array([[4, 1, 1],
              [2, 7, 2],
              [1, 2, 4]], dtype=float)
b = np.array([2, 5, 3], dtype=float)
x0 = np.zeros_like(b)
tol = 1e-6
Nmax = 100

# Aplicar el método de Gauss-Seidel
solucion, iteraciones, convergencia = gauss_seidel(A, b, x0, tol, Nmax)

# Imprimir resultados
if convergencia:
    print(f"Solución encontrada: {solucion} en {iteraciones} iteraciones")
else:
    print(f"No se alcanzó la convergencia en {iteraciones} iteraciones")
```

### Resultados y Análisis
El código anterior aplica el método de Gauss-Seidel para resolver el sistema de ecuaciones lineales \(Ax = b\), donde \(A\) es una matriz de coeficientes, \(b\) es un vector de términos independientes, \(x\) es el vector de soluciones y \(x_0\) es el vector de soluciones inicial. El resultado muestra si el método ha convergido a una solución dentro de un número máximo de iteraciones y una tolerancia especificada.
