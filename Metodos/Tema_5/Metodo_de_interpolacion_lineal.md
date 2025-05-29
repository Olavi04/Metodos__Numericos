# Interpolación Lineal

## Definición

La interpolación lineal es un método numérico utilizado para encontrar el valor de una función entre dos puntos dados. Este método asume que la función varía de manera lineal entre los puntos conocidos.

## Algoritmo

1. Obtener dos puntos conocidos (x0, y0) y (x1, y1).
2. Calcular la pendiente m de la recta que pasa por los dos puntos: m = (y1 - y0) / (x1 - x0).
3. Usar la ecuación de la recta para calcular el valor interpolado y en el punto x deseado: y = y0 + m * (x - x0).

## Metodología

```python
def linear_interpolation(x0, y0, x1, y1, x):
    """
    Función para realizar la interpolación lineal y calcular el valor y en un punto x dado.

    Parámetros:
    x0 (float): Coordenada x del primer punto conocido.
    y0 (float): Coordenada y del primer punto conocido.
    x1 (float): Coordenada x del segundo punto conocido.
    y1 (float): Coordenada y del segundo punto conocido.
    x (float): Valor de x donde se desea calcular el valor interpolado.

    Devuelve:
    float: Valor interpolado y en el punto x.
    """
    m = (y1 - y0) / (x1 - x0)
    return y0 + m * (x - x0)

try:
    x0 = float(input("Ingrese la coordenada x del primer punto: "))
    y0 = float(input("Ingrese la coordenada y del primer punto: "))
    x1 = float(input("Ingrese la coordenada x del segundo punto: "))
    y1 = float(input("Ingrese la coordenada y del segundo punto: "))
    x = float(input("Ingrese el valor de x para calcular la interpolación: "))
    
    result = linear_interpolation(x0, y0, x1, y1, x)
    print(f"El valor interpolado de y en x = {x} es: {result}")

except ValueError as e:
    print(f"Error: {e}")
```

## Análisis y Resultados

### Ejemplo

Para este ejemplo, se tienen los siguientes puntos conocidos:

- Primer punto: (1, 2)
- Segundo punto: (5, 7)
- Valor de x: 3

Al aplicar la interpolación lineal, se obtiene un valor interpolado de y en x = 3 de 4.25. Este resultado significa que se estima que la función pasa por el punto (3, 4.25), asumiendo una variación lineal entre los puntos conocidos (1, 2) y (5, 7).
