# Método de Cuadratura
## Definición
El Método de Cuadratura, también conocido como regla de cuadratura, es un método numérico utilizado para aproximar el valor de una integral definida mediante la evaluación de la función en puntos seleccionados dentro del intervalo de integración.

![imagen1](https://github.com/Olavi04/Metodos__Numericos/assets/160789479/8145aed4-2e4a-45d9-a5d2-e20dc9f3f3f8)

## Algoritmo
1. Seleccionar los puntos de cuadratura y los pesos correspondientes dentro del intervalo de integración.
2. Evaluar la función en los puntos de cuadratura y ponderar los resultados por los pesos correspondientes.
3. Sumar los productos obtenidos para obtener la aproximación de la integral.

![imagen2](https://github.com/Olavi04/Metodos__Numericos/assets/160789479/7ef3e576-5664-4405-9e82-80bf49f6384b)

## Metodología

### Código en Python para el Método de Cuadratura
A continuación, se presenta un ejemplo de código en Python para aplicar el Método de Cuadratura en la aproximación de una integral definida.

```python
def cuadratura(f, a, b, puntos, pesos):
    """
    Función para aproximar una integral definida utilizando el Método de Cuadratura.

    Parámetros:
    f (function): Función a integrar.
    a (float): Límite inferior del intervalo de integración.
    b (float): Límite superior del intervalo de integración.
    puntos (list): Lista de puntos de cuadratura dentro del intervalo de integración.
    pesos (list): Lista de pesos correspondientes a los puntos de cuadratura.

    Devuelve:
    float: Aproximación de la integral definida.
    """
    integral = 0
    for i in range(len(puntos)):
        integral += pesos[i] * f((b - a) / 2 * puntos[i] + (a + b) / 2)
    integral *= (b - a) / 2
    return integral

# Ejemplo de aproximación de una integral definida
import numpy as np

f = np.sin  # Función a integrar
a = 0       # Límite inferior del intervalo de integración
b = np.pi   # Límite superior del intervalo de integración

# Puntos y pesos para la regla de cuadratura de Gauss-Legendre con 3 puntos
puntos = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
pesos = [5/9, 8/9, 5/9]

# Aproximación de la integral definida utilizando el Método de Cuadratura
aproximacion = cuadratura(f, a, b, puntos, pesos)

# Imprimir resultado
print("Aproximación de la integral definida:", aproximacion)
```


### Datos de salida:


![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/R1.jpeg)

### Ejercicio 2:
Aproxima la integral \( \int_0^1 x^2 \, dx \) utilizando el método de cuadratura con la regla del trapecio y un tamaño de paso \( h = 0.1 \).

```python
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

def f(x):
    return x**2

a = 0
b = 1
n = 10

result = trapezoidal_rule(f, a, b, n)
print("Aproximación de la integral utilizando el método de cuadratura (Ejercicio 2):", result)
```

### Datos de salida:


![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/R2.jpeg)

### Ejercicio 3:
Aproxima la integral \( \int_0^1 \sin(x) \, dx \) utilizando el método de cuadratura con la regla del trapecio y un tamaño de paso \( h = 0.1 \).

```python
import math

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

def f(x):
    return math.sin(x)

a = 0
b = 1
n = 10

result = trapezoidal_rule(f, a, b, n)
print("Aproximación de la integral utilizando el método de cuadratura (Ejercicio 3):", result)
```
### Datos de salida:


![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/R3.jpeg)

### Ejercicio 4:
Aproxima la integral \( \int_0^1 e^x \, dx \) utilizando el método de cuadratura con la regla del trapecio y un tamaño de paso \( h = 0.1 \).

```python
import math

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

def f(x):
    return math.exp(x)

a = 0
b = 1
n = 10

result = trapezoidal_rule(f, a, b, n)
print("Aproximación de la integral utilizando el método de cuadratura (Ejercicio 4):", result)
```

### Datos de salida:


![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/R4.jpeg)


### Ejercicio 5:
Aproxima la integral \( \int_0^2 \cos(x) \, dx \) utilizando el método de cuadratura con la regla del trapecio y un tamaño de paso \( h = 0.2 \).

```python
import math

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

def f(x):
    return math.cos(x)

a = 0
b = 2
n = 10

result = trapezoidal_rule(f, a, b, n)
print("Aproximación de la integral utilizando el método de cuadratura (Ejercicio 5):", result)
```

### Datos de salida:


![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/R5.jpeg)



### Resultados y Análisis
El código anterior aproxima la integral definida de la función seno en el intervalo \([0, \pi]\) utilizando el Método de Cuadratura con la regla de cuadratura de Gauss-Legendre con 3 puntos. Se obtiene una aproximación numérica de la integral definida.
