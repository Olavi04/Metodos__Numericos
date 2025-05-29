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
    return 2*y-x

# Especificar el punto inicial y el tamaño del paso
x0 = 0
y0 = 13
h = 6
n = 10

# Resolver la ecuación diferencial utilizando el método de Euler
solution = euler_method(f, x0, y0, h, n)
print("Solución aproximada utilizando el método de Euler:")
for point in solution:
    print("x =", point[0], ", y =", point[1])