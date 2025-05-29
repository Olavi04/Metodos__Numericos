# Interpolación de Lagrange

## Definición

La interpolación de Lagrange es un método numérico utilizado para encontrar el polinomio único de grado n que pasa por un conjunto de n+1 puntos dados. Este polinomio interpolante se expresa como una combinación lineal de polinomios base llamados polinomios de Lagrange.

## Algoritmo

1. Obtener los puntos (x0, y0), (x1, y1), ..., (xn, yn).
2. Calcular los polinomios de Lagrange Li(x) para cada punto (xi, yi).
3. Construir el polinomio interpolante P(x) como la suma ponderada de los polinomios de Lagrange.
4. Evaluar el polinomio interpolante P(x) en el punto deseado x_eval.

## Metodología

```python
def lagrange_interpolation(xP, y_points, x_value):
    """
    Función para realizar la interpolación de Lagrange y evaluar el polinomio interpolante en un punto dado.

    Parámetros:
    xP (list): Lista de coordenadas x de los puntos.
    y_points (list): Lista de coordenadas y de los puntos.
    x_value (float): Valor de x donde se evaluará el polinomio interpolante.

    Devuelve:
    float: Valor del polinomio interpolante evaluado en x_value.
    
    Raises:
    ValueError: Si se encuentran puntos con coordenadas x idénticas, lo que causa una división por cero.
    """
    n = len(xP)
    for i in range(n):
        for j in range(i + 1, n):
            if xP[i] == xP[j]:
                raise ValueError(f"Los puntos x{i} y x{j} son idénticos, lo que causa una división por cero.")
    
    result = 0 
    for i in range(n):
        termino = y_points[i]
        for j in range(n):
            if j != i:
                termino *= (x_value - xP[j]) / (xP[i] - xP[j])
        result += termino

    return round(result, 2)

try:
    num_points = int(input("Ingrese el número de puntos: "))
    if num_points <= 0:
        raise ValueError("El número de puntos debe ser mayor que cero.")

    xVal = []
    yVal = []

    for i in range(num_points):
        xi = float(input(f"Ingrese x{i}: "))
        yi = float(input(f"Ingrese y{i}: "))
        xVal.append(xi)
        yVal.append(yi)

    x = float(input("Ingrese el valor de x para evaluar el polinomio: "))
    result = lagrange_interpolation(xVal, yVal, x)
    print(f"El valor del polinomio en x = {x} es: {result}")

except ValueError as e:
    print(f"Error: {e}")
```

## Análisis y Resultados

### Ejercicio 1

Para este ejercicio, se tienen los siguientes puntos:

- Número de puntos: 4
- Puntos: (4, 6), (19, 20), (34, 32), (42, 47)
- Valor de x: 60

Al evaluar el polinomio interpolante en x = 60, se obtiene un valor de 83.62.

![](https://github.com/Mexta46/Metodos_Numericos/blob/f65355814af07014b2fe6c2ae56c1e8ea78d13d6/Imagenes/Imagenes_tema5/LN1.png)

### Ejercicio 2

En este caso, se tienen los siguientes puntos:

- Número de puntos: 2
- Puntos: (34, 40), (50, 60)
- Valor de x: 77

Al evaluar el polinomio interpolante en x = 77, se obtiene un valor de 113.0.

![](https://github.com/Mexta46/Metodos_Numericos/blob/f65355814af07014b2fe6c2ae56c1e8ea78d13d6/Imagenes/Imagenes_tema5/LN2.png)

### Ejercicio 3

Para este ejercicio, los puntos dados son:

- Número de puntos: 5
- Puntos: (1, 6), (12, 17), (25, 30), (32, 38), (40, 47)
- Valor de x: 50

Al evaluar el polinomio interpolante en x = 50, se obtiene un valor de 45.47.

![](https://github.com/Mexta46/Metodos_Numericos/blob/f65355814af07014b2fe6c2ae56c1e8ea78d13d6/Imagenes/Imagenes_tema5/LN3.png)

### Ejercicio 4

Los puntos para este ejercicio son:

- Número de puntos: 2
- Puntos: (12, 24), (15, 30)
- Valor de x: 20

Al evaluar el polinomio interpolante en x = 20, se obtiene un valor de 26.4.

![](https://github.com/Mexta46/Metodos_Numericos/blob/f65355814af07014b2fe6c2ae56c1e8ea78d13d6/Imagenes/Imagenes_tema5/LN4.png)

### Ejercicio 5

Por último, para este ejercicio se tienen los puntos:

- Número de puntos: 3
- Puntos: (11, 22), (25, 30), (33, 45)
- Valor de x: 50

Al evaluar el polinomio interpolante en x = 50, se obtiene un valor de 46.38.

![](https://github.com/Mexta46/Metodos_Numericos/blob/f65355814af07014b2fe6c2ae56c1e8ea78d13d6/Imagenes/Imagenes_tema5/LN5.png)
