# Método de Simpson 1/3
## Definición
El método de Simpson es una técnica de integración numérica que utiliza polinomios de segundo grado para aproximar el área bajo una curva. Se basa en dividir el área en segmentos y calcular una suma ponderada de los valores de la función en los extremos y en el punto medio de cada segmento.

![Simpson 1](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_Tema4/simpson1.png)

## Algoritmo
1. f(x) que se desea integrar.
2. Especificar el intervalo de integración,[a,b].
3. Dividir el intervalo [a,b] en n subintervalos de igual tamaño, donde n es un número par.
4. Calcular el ancho de cada subintervalo, h=(b−a)/2.
5. Calcular los valores de la función f(x) en los extremos de los subintervalos: f(a),f(a+h),f(a+2h),…,f(b).
6. Calcular los valores de la función f(x) en los puntos medios de los subintervalos: f(a+((h)/2)), f(a+((3h)/2)), ... , f(b+((h)/2)).
7. Aplicar la fórmula de Simpson para calcular la aproximación de la integral:
![Simpson 2](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_Tema4/simpson2.png)
8. Devolver el valor calculado como la aproximación de la integral.

## Metodología 

```python
import math

# Definir la función a integrar
def f(x):
    return math.sin(x)  # Función trigonométrica: sin(x)

# Método de Simpson para aproximar la integral
def simpson(a, b, n):
    # Calcular el ancho de cada subintervalo
    h = (b - a) / n
    # Sumar el valor de la función en los extremos
    sum = f(a) + f(b)
    
    # Calcular la suma de los valores de la función en los puntos medios
    for i in range(1, n):
        # Calcular el valor de x en el punto medio del subintervalo
        x = a + i * h
        # Aplicar la regla de Simpson (ponderar por 2 o 4 según el índice)
        if i % 2 == 0:
            sum += 2 * f(x)
        else:
            sum += 4 * f(x)
    
    # Devolver el resultado de la aproximación de la integral
    return h * sum / 3

# Intervalo de integración y número de subintervalos
a = 0   # Límite inferior del intervalo
b = math.pi   # Límite superior del intervalo (pi)
n = 10  # Número de subintervalos (par)

# Calcular la aproximación de la integral
result = simpson(a, b, n)
````


# Resultados y Análisis
print("La aproximación de la integral definida es:", result)
print("La integral definida es el área bajo la curva de la función f(x) = sin(x) en el intervalo [0, pi]. El Método de Simpson 1/3 se utiliza para calcular esta área numéricamente. El valor aproximado obtenido es una estimación de la integral definida.")

# Ejemplos

## Ejemplo 1
![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/simpson3.png)
## Ejemplo 2
![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/simpson4.png)
## Ejemplo 3
![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/simpson5.png)
## Ejemplo 4 
![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/simpson6.png)
## Ejemplo 5
![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_Tema4/simpson7.png)
