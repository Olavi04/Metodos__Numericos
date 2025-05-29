# Método de Euler
## Definición
El método de Euler es una técnica numérica para aproximar soluciones de ecuaciones diferenciales ordinarias (EDOs) con condiciones iniciales conocidas. Este método se basa en la aproximación de la derivada de una función mediante una diferencia finita.

## Algoritmo
1. Definir la ecuación diferencial de primer orden que se desea resolver: dy/dx = f(x, y).
2. Especificar el punto inicial (x0, y0).
3. Especificar el tamaño del paso h.
4. Calcular los valores de y en los puntos sucesivos utilizando la fórmula de Euler:
   - \( y(n+1) = yn + h * f(xn, yn) \)
5. Repetir el paso 4 hasta alcanzar el punto final deseado.

## Metodología
El método de Euler es un método de integración numérica utilizado para resolver ecuaciones diferenciales ordinarias de primer orden. Aunque es un método simple, puede proporcionar resultados útiles para problemas que no son muy sensibles a pequeños errores de aproximación.

## Implementación en Python

```python
def euler_method(f, x0, y0, h, n):
    """
    Implementación del método de Euler para resolver una EDO de primer orden.

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
        xn += h
        yn += h * f(xn - h, yn)  # Aplicando la fórmula de Euler
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

# Resolver la ecuación diferencial utilizando el método de Euler
solution = euler_method(f, x0, y0, h, n)
print("Solución aproximada utilizando el método de Euler:")
for point in solution:
    print("x =", point[0], ", y =", point[1])
```


### Ejercicio 1:
Resuelve la ecuación diferencial \( dy/dx = x^2 - y \) con condiciones iniciales (x(0)=0, y(0) = 1 ) en el intervalo \( 0 < x < 1 \) utilizando el método de Euler con un tamaño de paso \( h = 0.1 \).

![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema6/IE1.png)

### Ejercicio 2:
Resuelve la ecuación diferencial \( dy/dx = -2xy \) con condiciones iniciales (x(0)=0, y(0) = 0.5 \) en el intervalo \( 0 < x < 1 \) utilizando el método de Euler con un tamaño de paso \( h = 0.05 \).

![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema6/IE2.png)

### Ejercicio 3:
Resuelve la ecuación diferencial \( dy/dx = x^2 + y^2 \) con condiciones iniciales (x(0)=0, y(0) = 0 ) en el intervalo \( 0 < x < 1 \) utilizando el método de Euler con un tamaño de paso \( h = 0.1 \).

![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema6/IE3.png)

### Ejercicio 4:
Resuelve la ecuación diferencial \( dy/dx = y - x \) con condiciones iniciales (x(0)=0, y(0) = 2 ) en el intervalo \( 0 < x < 1 \) utilizando el método de Euler con un tamaño de paso \( h = 0.2 \).

![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema6/IE4.png)

### Ejercicio 5:
Resuelve la ecuación diferencial \( dy/dx = 2y - x \) con condiciones iniciales (x(0)=0, y(0) = 13 ) en el intervalo \( 0 < x < 1 \) utilizando el método de Euler con un tamaño de paso \( h = 6 \).

![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema6/IE5.png)

## Análisis y Resultados
El método de Euler proporciona una solución aproximada a la ecuación diferencial especificada mediante la iteración a través de pequeños pasos desde el punto inicial hasta el punto final deseado. La precisión de la solución depende del tamaño del paso \( h \), donde valores más pequeños de \( h \) generalmente proporcionan resultados más precisos a expensas de una mayor carga computacional.

Al observar los resultados obtenidos con el ejemplo proporcionado, podemos notar que la solución aproximada se acerca a la solución exacta a medida que aumentamos el número de pasos \( n \) o disminuimos el tamaño del paso \( h \). Sin embargo, es importante tener en cuenta que el método de Euler puede no ser adecuado para todas las ecuaciones diferenciales, especialmente aquellas con soluciones que cambian rápidamente o son sensibles a pequeños errores de aproximación.

