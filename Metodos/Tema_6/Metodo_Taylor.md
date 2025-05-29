# Método de Taylor
## Definición
El método de Taylor es un método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDOs) con condiciones iniciales conocidas. Este método se basa en la aproximación de la solución de la ecuación diferencial mediante una serie de Taylor, lo que permite obtener una solución más precisa que el método de Euler.

## Algoritmo
1. Definir la ecuación diferencial de primer orden que se desea resolver: dy/dx = f(x, y).
2. Especificar el punto inicial (x0, y0).
3. Calcular las derivadas de la función f(x, y) con respecto a y en el punto inicial.
4. Utilizar la serie de Taylor para aproximar la solución de la ecuación diferencial en los puntos sucesivos.
5. Repetir el paso 4 hasta alcanzar el punto final deseado.

## Metodología
El método de Taylor es un método de integración numérica que proporciona una solución más precisa que el método de Euler al utilizar una aproximación de alta precisión basada en la serie de Taylor. Esto permite obtener soluciones más precisas, especialmente para ecuaciones diferenciales que tienen soluciones que cambian rápidamente o son sensibles a pequeños errores de aproximación.

## Implementación en Python

```python
def taylor_method(f, df_dx, df_dy, x0, y0, h, n):
    """
    Implementación del método de Taylor para resolver una EDO de primer orden.

    Args:
    - f: Función que define la ecuación diferencial dy/dx = f(x, y).
    - df_dx: Derivada parcial de f respecto a x.
    - df_dy: Derivada parcial de f respecto a y.
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
        xn += h
        yn += h * f(xn - h/2, yn) + (h**2 / 2) * (df_dx(xn - h/2, yn) + df_dy(xn - h/2, yn) * f(xn - h/2, yn))
        results.append((xn, yn))
    return results

# Ejemplo de uso:
# Definir la ecuación diferencial dy/dx = f(x, y)
def f(x, y):
    return x + y

# Derivadas parciales de f respecto a x e y
def df_dx(x, y):
    return 1

def df_dy(x, y):
    return 1

# Especificar el punto inicial y el tamaño del paso
x0 = 0
y0 = 1
h = 0.1
n = 10

# Resolver la ecuación diferencial utilizando el método de Taylor
solution = taylor_method(f, df_dx, df_dy, x0, y0, h, n)
print("Solución aproximada utilizando el método de Taylor:")
for point in solution:
    print("x =", point[0], ", y =", point[1])
```

### Ejercicio 1:
Resuelve la ecuación diferencial \( dy/dx = x^4 - y^2 \) con condiciones iniciales \( x(0)=0, y(0) = 1 \) en el intervalo \( 0 < x < 1 \) utilizando el método de Taylor con un tamaño de paso \( h = 0.1 \).

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Imagenes_tema6/IT1.png)

### Ejercicio 2:
Resuelve la ecuación diferencial \( dy/dx = -2xy \) con condiciones iniciales \( x(0)=0, y(0) = 0.5 \) en el intervalo \( 0 < x < 1 \) utilizando el método de Taylor con un tamaño de paso \( h = 0.05 \).

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Imagenes_tema6/IT2.png)

### Ejercicio 3:
Resuelve la ecuación diferencial \( dy/dx = x^2 + y^2 \) con condiciones iniciales \( x(0)=0, y(0) = 0 \) en el intervalo \( 0 < x < 1 \) utilizando el método de Taylor con un tamaño de paso \( h = 0.1 \).

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Imagenes_tema6/IT3.png)

### Ejercicio 4:
Resuelve la ecuación diferencial \( dy/dx = y - x \) con condiciones iniciales \( x(0)=0, y(0) = 2 \) en el intervalo \( 0 < x < 1 \) utilizando el método de Taylor con un tamaño de paso \( h = 0.2 \).

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Imagenes_tema6/IT4.png)

### Ejercicio 5:
Resuelve la ecuación diferencial \( dy/dx = 2y-x \) con condiciones iniciales \( x(0)=0, y(0) = 13 \) en el intervalo \( 0 < x < 1 \) utilizando el método de Taylor con un tamaño de paso \( h = 6 \).

![](https://github.com/Mexta46/Metodos_Numericos/blob/main/Imagenes/Imagenes_tema6/IT5.png)


## Análisis y Resultados
El método de Taylor proporciona una solución más precisa a la ecuación diferencial especificada en comparación con el método de Euler, ya que utiliza una aproximación de alta precisión basada en la serie de Taylor. Al calcular las derivadas parciales de la función \( f(x, y) \) y utilizar la serie de Taylor para aproximar la solución en los puntos sucesivos, el método de Taylor es capaz de capturar de manera más efectiva los cambios en la función y proporcionar una solución más precisa en cada paso.

Al observar los resultados obtenidos con el ejemplo proporcionado, podemos notar que la solución aproximada utilizando el método de Taylor se acerca más a la solución exacta en comparación con el método de Euler. Esto demuestra la mayor precisión del método de Taylor, especialmente cuando se trabaja con ecuaciones diferenciales que tienen soluciones que cambian rápidamente o son sensibles a pequeños errores de aproximación.
