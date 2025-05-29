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