# Error de Redondeo
## Definición
El error de redondeo es la diferencia entre el valor numérico exacto y su aproximación debido a la limitación en la representación de números en sistemas de cómputo. Este tipo de error ocurre cuando se redondean números a un número fijo de dígitos significativos o decimales. Los errores de redondeo pueden acumularse en cálculos repetidos y afectar la precisión de los resultados.

![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema_1/error.png).

## Algoritmo
1. Definir la función f(x) cuya evaluación puede introducir errores de redondeo.
2. Especificar el intervalo de evaluación [a, b].
3. Dividir el intervalo [a, b] en n subintervalos de igual tamaño.
4. Calcular el valor exacto de f(x) en puntos específicos del intervalo.
5. Calcular el valor aproximado de f(x) usando una precisión limitada en puntos específicos del intervalo.
6. Comparar los valores exactos y aproximados para determinar el error de redondeo.
7. Analizar cómo varía el error de redondeo a lo largo del intervalo.
8. Devolver los valores calculados como análisis del error de redondeo.

![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema_1/errorf.png).

## Metodología

### Código en Python para Evaluar el Error de Redondeo
A continuación, se presenta un ejemplo de código en Python para evaluar el error de redondeo en la función \( f(x) = e^x \) en el intervalo [0, 1].

```python
import numpy as np

def calcular_error_redondeo(f, a, b, n, precision):
    """
    Función para calcular el error de redondeo en la evaluación de una función f(x) en el intervalo [a, b].

    Parámetros:
    f (función): Función a evaluar.
    a (float): Límite inferior del intervalo.
    b (float): Límite superior del intervalo.
    n (int): Número de subintervalos.
    precision (int): Número de decimales para la aproximación.

    Devuelve:
    list: Lista de errores de redondeo en los puntos del intervalo.
    """
    h = (b - a) / n  # tamaño del subintervalo
    valores_exactos = []
    valores_aproximados = []
    errores = []

    for i in range(n + 1):
        x = a + i * h
        valor_exacto = f(x)
        valor_aproximado = round(f(x), precision)  # Redondear a la precisión especificada
        valores_exactos.append(valor_exacto)
        valores_aproximados.append(valor_aproximado)
        error = abs(valor_exacto - valor_aproximado)
        errores.append(error)

    return errores, valores_exactos, valores_aproximados

# Definición de la función a evaluar
def f(x):
    return np.exp(x)

# Parámetros del intervalo y precisión
a = 0
b = 1
n = 10  # número de subintervalos
precision = 5  # número de decimales para la aproximación

# Calcular errores de redondeo
errores, valores_exactos, valores_aproximados = calcular_error_redondeo(f, a, b, n, precision)

# Imprimir resultados
print("x\tValor Exacto\tValor Aproximado\tError de Redondeo")
for i in range(n + 1):
    x = a + i * h
    print(f"{x:.2f}\t{valores_exactos[i]:.5f}\t{valores_aproximados[i]:.5f}\t{errores[i]:.5f}")
```
