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