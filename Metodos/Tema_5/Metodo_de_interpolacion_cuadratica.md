# Interpolació cuadratica 

## Definición 

La interpolación cuadrática es una técnica matemática utilizada para estimar valores entre puntos de datos. Entra en juego cuando tienes tres puntos de datos y quieres entender cómo una curva suave podría conectar estos puntos. En este método, se supone que la relación subyacente entre los puntos de datos puede aproximarse mediante un polinomio de segundo grado, a menudo denominado polinomio cuadrático. Este supuesto significa que se espera que el comportamiento de la curva sea de forma parabólica.

Esta ecuación le permite estimar el comportamiento de la función entre los puntos de datos dados, incluso cuando se desconoce la función específica.

## Fórmula 
![Formula](https://almedinablog.files.wordpress.com/2016/03/interpolacion-cuadratica.png)

## Algoritmo
1. Definir tres puntos conocidos \((x_0, y_0)\), \((x_1, y_1)\), y \((x_2, y_2)\).
2. Determinar el polinomio cuadrático \( P(x) = ax^2 + bx + c \) que pasa por estos puntos.
3. Resolver el sistema de ecuaciones para encontrar los coeficientes \( a \), \( b \), y \( c \).
4. Utilizar el polinomio cuadrático para estimar valores en puntos intermedios.

## Metodología

### Código en Python para Interpolación Cuadrática
A continuación, se presenta un ejemplo de código en Python para aplicar la interpolación cuadrática.

```python
import numpy as np
import matplotlib.pyplot as plt

def interpolacion_cuadratica(x0, y0, x1, y1, x2, y2):
    """
    Función para realizar la interpolación cuadrática y encontrar los coeficientes del polinomio cuadrático.

    Parámetros:
    x0, y0 (float): Primer punto conocido.
    x1, y1 (float): Segundo punto conocido.
    x2, y2 (float): Tercer punto conocido.

    Devuelve:
    tuple: Coeficientes del polinomio cuadrático (a, b, c).
    """
    # Crear el sistema de ecuaciones
    A = np.array([
        [x0**2, x0, 1],
        [x1**2, x1, 1],
        [x2**2, x2, 1]
    ])
    b = np.array([y0, y1, y2])

    # Resolver el sistema para encontrar los coeficientes
    a, b, c = np.linalg.solve(A, b)
    return a, b, c

# Definir los puntos conocidos
x0, y0 = 0, 1
x1, y1 = 1, 3
x2, y2 = 2, 2

# Encontrar los coeficientes del polinomio cuadrático
a, b, c = interpolacion_cuadratica(x0, y0, x1, y1, x2, y2)

# Definir la función del polinomio cuadrático
def P(x):
    return a*x**2 + b*x + c

# Definir los puntos donde se desea estimar los valores
x_nuevo = np.linspace(0, 2, 100)
y_nuevo = P(x_nuevo)

# Graficar los puntos conocidos y el polinomio cuadrático de interpolación
plt.plot([x0, x1, x2], [y0, y1, y2], 'o', label='Puntos conocidos')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación Cuadrática')
plt.show()
```
### Ejercicio 2
Dado los puntos conocidos \((1, 3)\), \((2, 8)\), y \((3, 15)\), encuentra el polinomio cuadrático que pasa por estos puntos y grafica la interpolación cuadrática resultante.

```python
import numpy as np
import matplotlib.pyplot as plt

# Definir los puntos conocidos
x0, y0 = 1, 3
x1, y1 = 2, 8
x2, y2 = 3, 15

# Encontrar los coeficientes del polinomio cuadrático
a, b, c = interpolacion_cuadratica(x0, y0, x1, y1, x2, y2)

# Definir la función del polinomio cuadrático
def P(x):
    return a*x**2 + b*x + c

# Definir los puntos donde se desea estimar los valores
x_nuevo = np.linspace(1, 3, 100)
y_nuevo = P(x_nuevo)

# Graficar los puntos conocidos y el polinomio cuadrático de interpolación
plt.plot([x0, x1, x2], [y0, y1, y2], 'o', label='Puntos conocidos')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación Cuadrática - Ejercicio 1')
plt.show()
```

### Ejercicio 3
Dado los puntos conocidos \((-1, 0)\), \((0, 1)\), y \((1, 0)\), encuentra el polinomio cuadrático que pasa por estos puntos y grafica la interpolación cuadrática resultante.

```python
# Definir los puntos conocidos
x0, y0 = -1, 0
x1, y1 = 0, 1
x2, y2 = 1, 0

# Encontrar los coeficientes del polinomio cuadrático
a, b, c = interpolacion_cuadratica(x0, y0, x1, y1, x2, y2)

# Definir la función del polinomio cuadrático
def P(x):
    return a*x**2 + b*x + c

# Definir los puntos donde se desea estimar los valores
x_nuevo = np.linspace(-1, 1, 100)
y_nuevo = P(x_nuevo)

# Graficar los puntos conocidos y el polinomio cuadrático de interpolación
plt.plot([x0, x1, x2], [y0, y1, y2], 'o', label='Puntos conocidos')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación Cuadrática - Ejercicio 2')
plt.show()
```

### Ejercicio 4
Dado los puntos conocidos \((-2, 1)\), \((0, -1)\), y \((2, 5)\), encuentra el polinomio cuadrático que pasa por estos puntos y grafica la interpolación cuadrática resultante.

```python
# Definir los puntos conocidos
x0, y0 = -2, 1
x1, y1 = 0, -1
x2, y2 = 2, 5

# Encontrar los coeficientes del polinomio cuadrático
a, b, c = interpolacion_cuadratica(x0, y0, x1, y1, x2, y2)

# Definir la función del polinomio cuadrático
def P(x):
    return a*x**2 + b*x + c

# Definir los puntos donde se desea estimar los valores
x_nuevo = np.linspace(-2, 2, 100)
y_nuevo = P(x_nuevo)

# Graficar los puntos conocidos y el polinomio cuadrático de interpolación
plt.plot([x0, x1, x2], [y0, y1, y2], 'o', label='Puntos conocidos')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación Cuadrática - Ejercicio 3')
plt.show()
```

### Ejercicio 5
Dado los puntos conocidos \((-3, 1)\), \((0, 2)\), y \((3, 1)\), encuentra el polinomio cuadrático que pasa por estos puntos y grafica la interpolación cuadrática resultante.

```python
# Definir los puntos conocidos
x0, y0 = -3, 1
x1, y1 = 0, 2
x2, y2 = 3, 1

# Encontrar los coeficientes del polinomio cuadrático
a, b, c = interpolacion_cuadratica(x0, y0, x1, y1, x2, y2)

# Definir la función del polinomio cuadrático
def P(x):
    return a*x**2 + b*x + c

# Definir los puntos donde se desea estimar los valores
x_nuevo = np.linspace(-3, 3, 100)
y_nuevo = P(x_nuevo)

# Graficar los puntos conocidos y el polinomio cuadrático de interpolación
plt.plot([x0, x1, x2], [y0, y1, y2], 'o', label='Puntos conocidos')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación Cuadrática - Ejercicio 4')
plt.show()
```

### Resultados y Análisis
El código anterior aplica la interpolación cuadrática a tres puntos conocidos \((0, 1)\), \((1, 3)\), y \((2, 2)\). Se determina el polinomio cuadrático que pasa por estos puntos y se utiliza para estimar valores intermedios.
