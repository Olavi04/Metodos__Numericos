# Overflow
## Definición
El overflow (desbordamiento) ocurre cuando un cálculo produce un resultado que es mayor que el valor máximo que puede ser representado con el tipo de datos numérico utilizado en el sistema de cómputo. Esto puede llevar a resultados incorrectos o a la pérdida de información.

![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema_1/overflow.png).

## Algoritmo
1. Definir la función f(x) cuyo cálculo puede llevar al overflow.
2. Especificar el intervalo de evaluación [a, b].
3. Dividir el intervalo [a, b] en n subintervalos de igual tamaño.
4. Calcular el valor de f(x) en puntos específicos del intervalo.
5. Detectar si ocurre overflow y manejarlo adecuadamente.
6. Analizar cómo y dónde ocurre el overflow a lo largo del intervalo.
7. Devolver los valores calculados y las instancias de overflow detectadas.

![](https://github.com/Olavi04/Metodos__Numericos/blob/main/Imagenes/Imagenes_tema_1/overflowf.png).

## Metodología

### Código en Python para Evaluar el Overflow
A continuación, se presenta un ejemplo de código en Python para evaluar el problema de overflow en la función \( f(x) = e^x \) en el intervalo [0, 50].

```python
import numpy as np

# Valor base y exponente
base = 10
exponente = 308

try:
    resultado = np.power(base, exponente)
    print(f"Resultado de {base}^{exponente}: {resultado}")
except OverflowError as e:
    print(f"Error de desbordamiento: {e}")
```

### Ejercicio 3: Desbordamiento en un bucle factorial
Calcular el factorial de un número grande y observar el desbordamiento.

```python
import math

# Número grande para calcular el factorial
numero = 170

try:
    resultado = math.factorial(numero)
    print(f"Factorial de {numero}: {resultado}")
except OverflowError as e:
    print(f"Error de desbordamiento: {e}")
```

### Ejercicio 4: Desbordamiento en una serie geométrica
Investigar el desbordamiento al sumar una serie geométrica con una razón mayor que 1.

```python
# Parámetros de la serie geométrica
a = 1  # Primer término
r = 1.1  # Razón
n = 100  # Número de términos

try:
    suma = sum(a * r**i for i in range(n))
    print(f"Suma de la serie geométrica: {suma}")
except OverflowError as e:
    print(f"Error de desbordamiento: {e}")
```

### Ejercicio 5: Desbordamiento en una multiplicación iterativa
Calcular el producto de una serie de números grandes y observar el desbordamiento.

```python
# Lista de números grandes
numeros = [1e154, 2e154, 3e154, 4e154]

try:
    producto = 1
    for numero in numeros:
        producto *= numero
    print(f"Producto de los números: {producto}")
except OverflowError as e:
    print(f"Error de desbordamiento: {e}")
```



### Resultados y Análisis
El código anterior genera una tabla que muestra el valor de la función y si ocurrió overflow en varios puntos del intervalo [0, 50]. Analizando estos resultados, se puede observar cómo y dónde ocurre el overflow, lo que ayuda a entender mejor las limitaciones de representación numérica y el comportamiento de la función en estos casos.

