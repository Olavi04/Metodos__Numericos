# Método de Runge-Kutta
## Definición
El método de Runge-Kutta es un método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDOs) con condiciones iniciales conocidas. A diferencia del método de Euler, el método de Runge-Kutta utiliza una aproximación más precisa para calcular los valores de la función en los puntos sucesivos.

## Algoritmo
1. Definir la ecuación diferencial de primer orden que se desea resolver: dy/dx = f(x, y).
2. Especificar el punto inicial (x0, y0).
3. Especificar el tamaño del paso h.
4. Calcular los valores de y en los puntos sucesivos utilizando la fórmula de Runge-Kutta de cuarto orden.
5. Repetir el paso 4 hasta alcanzar el punto final deseado.

## Metodología
El método de Runge-Kutta es un método de integración numérica más preciso que el método de Euler, ya que utiliza una aproximación de cuarto orden para calcular los valores de la función en los puntos sucesivos. Esto resulta en una solución más precisa, especialmente para ecuaciones diferenciales que tienen soluciones que cambian rápidamente o son sensibles a pequeños errores de aproximación.

## Implementación en Python

```python
def runge_kutta_method(f, x0, y0, h, n):
    """
    Implementación del método de Runge-Kutta de cuarto orden para resolver una EDO de primer orden.

    Args:
    - f: Función que define la ecuación diferencial dy/dx = f(x, y).
    - x0: Punto inicial x.
    - y0: Valor inicial y en x0.
    - h: Tamaño del paso.
    - n: Número de pasos.

    Returns:
    - Lista de tuplas (x, y) con los valores aproximados de la solución.
    """
    results = [(x0, y0)]
    xn = x0
    yn = y0
    for _ in range(1, n + 1):
        k1 = h * f(xn, yn)
        k2 = h * f(xn + h/2, yn + k1/2)
        k3 = h * f(xn + h/2, yn + k2/2)
        k4 = h * f(xn + h, yn + k3)
        yn += (k1 + 2*k2 + 2*k3 + k4) / 6
        xn += h
        results.append((xn, yn))
    return results

# Ejemplo de uso:
# Definir la ecuación diferencial dy/dx = f(x, y)
def f(x, y):
    return x + y

# Especificar el punto inicial y el tamaño del paso
x0 = 0
y0 = 1
h = 0.1
n = 10

# Resolver la ecuación diferencial utilizando el método de Runge-Kutta
solution = runge_kutta_method(f, x0, y0, h, n)
print("Solución aproximada utilizando el método de Runge-Kutta:")
for point in solution:
    print("x =", point[0], ", y =", point[1])
```

### Datos de salida:


![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema6/R1.jpeg)


### Ejercicio 2:
Resuelve la ecuación diferencial \( \frac{{dy}}{{dx}} = x^2 - y \) con condiciones iniciales \( y(0) = 1 \) en el intervalo \( 0 \leq x \leq 1 \) utilizando el método de Runge-Kutta con un tamaño de paso \( h = 0.1 \).

```python
def runge_kutta_method(f, x0, y0, h, n):
    results = [(x0, y0)]
    xn = x0
    yn = y0
    for _ in range(n):
        k1 = h * f(xn, yn)
        k2 = h * f(xn + h/2, yn + k1/2)
        k3 = h * f(xn + h/2, yn + k2/2)
        k4 = h * f(xn + h, yn + k3)
        yn += (k1 + 2*k2 + 2*k3 + k4) / 6
        xn += h
        results.append((xn, yn))
    return results

def f(x, y):
    return x**2 - y

x0 = 0
y0 = 1
h = 0.1
n = 10

solution = runge_kutta_method(f, x0, y0, h, n)
print("Solución aproximada utilizando el método de Runge-Kutta (Ejercicio 2):")
for point in solution:
    print("x =", point[0], ", y =", point[1])
```

### Datos de salida:


![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema6/R2.jpeg)

### Ejercicio 3:
Resuelve la ecuación diferencial \( \frac{{dy}}{{dx}} = -2xy \) con condiciones iniciales \( y(0) = 0.5 \) en el intervalo \( 0 \leq x \leq 1 \) utilizando el método de Runge-Kutta con un tamaño de paso \( h = 0.05 \).

```python
def runge_kutta_method(f, x0, y0, h, n):
    results = [(x0, y0)]
    xn = x0
    yn = y0
    for _ in range(n):
        k1 = h * f(xn, yn)
        k2 = h * f(xn + h/2, yn + k1/2)
        k3 = h * f(xn + h/2, yn + k2/2)
        k4 = h * f(xn + h, yn + k3)
        yn += (k1 + 2*k2 + 2*k3 + k4) / 6
        xn += h
        results.append((xn, yn))
    return results

def f(x, y):
    return -2 * x * y

x0 = 0
y0 = 0.5
h = 0.05
n = 20

solution = runge_kutta_method(f, x0, y0, h, n)
print("Solución aproximada utilizando el método de Runge-Kutta (Ejercicio 3):")
for point in solution:
    print("x =", point[0], ", y =", point[1])
```

### Datos de salida:


![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema6/R3.jpeg)

### Ejercicio 4:
Resuelve la ecuación diferencial \( \frac{{dy}}{{dx}} = x^2 + y^2 \) con condiciones iniciales \( y(0) = 0 \) en el intervalo \( 0 \leq x \leq 1 \) utilizando el método de Runge-Kutta con un tamaño de paso \( h = 0.1 \).

```python
def runge_kutta_method(f, x0, y0, h, n):
    results = [(x0, y0)]
    xn = x0
    yn = y0
    for _ in range(n):
        k1 = h * f(xn, yn)
        k2 = h * f(xn + h/2, yn + k1/2)
        k3 = h * f(xn + h/2, yn + k2/2)
        k4 = h * f(xn + h, yn + k3)
        yn += (k1 + 2*k2 + 2*k3 + k4) / 6
        xn += h
        results.append((xn, yn))
    return results

def f(x, y):
    return x**2 + y**2

x0 = 0
y0 = 0
h = 0.1
n = 10

solution = runge_kutta_method(f, x0, y0, h, n)
print("Solución aproximada utilizando el método de Runge-Kutta (Ejercicio 4):")
for point in solution:
    print("x =", point[0], ", y =", point[1])
```

### Datos de salida:


![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema6/R4.jpeg)

### Ejercicio 5:
Resuelve la ecuación diferencial \( \frac{{dy}}{{dx}} = y - x \) con condiciones iniciales \( y(0) = 2 \) en el intervalo \( 0 \leq x \leq 1 \) utilizando el método de Runge-Kutta con un tamaño de paso \( h = 0.2 \).

```python
def runge_kutta_method(f, x0, y0, h, n):
    results = [(x0, y0)]
    xn = x0
    yn = y0
    for _ in range(n):
        k1 = h * f(xn, yn)
        k2 = h * f(xn + h/2, yn + k1/2)
        k3 = h * f(xn + h/2, yn + k2/2)
        k4 = h * f(xn + h, yn + k3)
        yn += (k1 + 2*k2 + 2*k3 + k4) / 6
        xn += h
        results.append((xn, yn))
    return results

def f(x, y):
    return y - x

x0 = 0
y0 = 2
h = 0.2
n = 5

solution = runge_kutta_method(f, x0, y0, h, n)
print("Solución aproximada utilizando el método de Runge-Kutta (Ejercicio 5):")
for point in solution:
    print("x =", point[0], ", y =", point[1])
```

### Datos de salida:


![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema6/R5.jpeg)


## Análisis y Resultados
El método de Runge-Kutta de cuarto orden proporciona una solución más precisa a la ecuación diferencial especificada en comparación con el método de Euler. Al utilizar una aproximación de cuarto orden, el método de Runge-Kutta es capaz de capturar de manera más efectiva los cambios en la función y proporcionar una solución más precisa en cada paso.

Al observar los resultados obtenidos con el ejemplo proporcionado, podemos notar que la solución aproximada utilizando el método de Runge-Kutta se acerca más a la solución exacta en comparación con el método de Euler. Esto demuestra la mayor precisión del método de Runge-Kutta, especialmente cuando se trabaja con ecuaciones diferenciales que tienen soluciones que cambian rápidamente o son sensibles a pequeños errores de aproximación.

