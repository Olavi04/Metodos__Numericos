# Método de Gauss-Jordan
## Definición
El método de Gauss-Jordan es una técnica numérica utilizada para resolver sistemas de ecuaciones lineales de la forma \( Ax = b \). Se basa en la eliminación de Gauss con una serie de pasos adicionales para convertir la matriz de coeficientes en una matriz identidad, simplificando la obtención de la solución.

## Algoritmo
1. Definir la matriz de coeficientes \( A \) y el vector de términos independientes \( b \).
2. Construir la matriz aumentada \([A | b]\).
3. Aplicar las operaciones de fila para transformar la matriz aumentada en la forma \([I | x]\), donde \( I \) es la matriz identidad.
4. El vector resultante en la columna de términos independientes es la solución \( x \).

## Metodología

### Código en Python para el Método de Gauss-Jordan
A continuación, se presenta un ejemplo de código en Python para aplicar el método de Gauss-Jordan para resolver un sistema de ecuaciones lineales.

```python
import numpy as np

def gauss_jordan(a, b, tol=1.0e-12):
    """
    Función para resolver el sistema de ecuaciones lineales Ax = b utilizando el método de Gauss-Jordan.

    Parámetros:
    a (ndarray): Matriz de coeficientes del sistema (n x n).
    b (ndarray): Vector de términos independientes (n).
    tol (float): Tolerancia para detectar singularidad.

    Devuelve:
    ndarray: Solución del sistema.
    """
    n = len(b)
    # Crear la matriz aumentada
    aug_matrix = np.hstack((a, b.reshape(-1, 1)))

    # Aplicar eliminación Gauss-Jordan
    for i in range(n):
        # Buscar el máximo elemento en la columna i
        max_row = np.argmax(np.abs(aug_matrix[i:n, i])) + i
        aug_matrix[[i, max_row]] = aug_matrix[[max_row, i]]

        # Verificar si la matriz es singular
        if np.abs(aug_matrix[i, i]) < tol:
            raise ValueError("La matriz es singular y no puede resolverse")

        # Hacer que el elemento diagonal sea 1
        aug_matrix[i] = aug_matrix[i] / aug_matrix[i, i]

        # Eliminar los demás elementos de la columna
        for j in range(n):
            if j != i:
                aug_matrix[j] -= aug_matrix[j, i] * aug_matrix[i]

    # La solución está en la última columna de la matriz aumentada
    x = aug_matrix[:, -1]
    return x

# Ejemplo de uso
# Definición de la matriz de coeficientes y el vector de términos independientes
a = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

# Aplicar el método de Gauss-Jordan
solucion = gauss_jordan(a, b)

# Imprimir la solución
print("Solución del sistema:")
print(solucion)
```

### Ejercicio 2: Resolver el sistema de ecuaciones
\[ \begin{cases} 
x + y + z = 6 \\
2y + 5z = -4 \\
2x + 5y - z = 27 
\end{cases} \]
utilizando el método de Gauss-Jordan.

```python
# Definición de la matriz de coeficientes y el vector de términos independientes
a = np.array([[1, 1, 1],
              [0, 2, 5],
              [2, 5, -1]], dtype=float)
b = np.array([6, -4, 27], dtype=float)

# Aplicar el método de Gauss-Jordan
solucion = gauss_jordan(a, b)

# Imprimir la solución
print("Solución del sistema:")
print(solucion)
```

### Ejercicio 3: Resolver el sistema de ecuaciones
\[ \begin{cases} 
3x - 0.1y - 0.2z = 7.85 \\
0.1x + 7y - 0.3z = -19.3 \\
0.3x - 0.2y + 10z = 71.4 
\end{cases} \]
utilizando el método de Gauss-Jordan.

```python
# Definición de la matriz de coeficientes y el vector de términos independientes
a = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]], dtype=float)
b = np.array([7.85, -19.3, 71.4], dtype=float)

# Aplicar el método de Gauss-Jordan
solucion = gauss_jordan(a, b)

# Imprimir la solución
print("Solución del sistema:")
print(solucion)
```

### Ejercicio 4: Resolver el sistema de ecuaciones
\[ \begin{cases} 
x + 2y + 3z = 9 \\
2x + 3y + 5z = 23 \\
4x + 5y + 7z = 34 
\end{cases} \]
utilizando el método de Gauss-Jordan.

```python
# Definición de la matriz de coeficientes y el vector de términos independientes
a = np.array([[1, 2, 3],
              [2, 3, 5],
              [4, 5, 7]], dtype=float)
b = np.array([9, 23, 34], dtype=float)

# Aplicar el método de Gauss-Jordan
solucion = gauss_jordan(a, b)

# Imprimir la solución
print("Solución del sistema:")
print(solucion)
```

### Ejercicio 5: Resolver el sistema de ecuaciones
\[ \begin{cases} 
2x + y + z = 4 \\
x + 3y + 2z = 5 \\
z = 1 
\end{cases} \]
utilizando el método de Gauss-Jordan.

```python
# Definición de la matriz de coeficientes y el vector de términos independientes
a = np.array([[2, 1, 1],
              [1, 3, 2],
              [0, 0, 1]], dtype=float)
b = np.array([4, 5, 1], dtype=float)

# Aplicar el método de Gauss-Jordan
solucion = gauss_jordan(a, b)

# Imprimir la solución
print("Solución del sistema:")
print(solucion)
```

### Resultados y Análisis
El código anterior aplica el método de Gauss-Jordan para resolver diferentes sistemas de ecuaciones lineales. Los resultados muestran la solución de cada sistema, asegurando que se cumplan las ecuaciones dadas.
