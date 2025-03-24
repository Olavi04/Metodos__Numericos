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
