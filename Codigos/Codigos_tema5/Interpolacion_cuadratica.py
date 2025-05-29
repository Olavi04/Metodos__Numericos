import numpy as np
import matplotlib.pyplot as plt

def interpolacion_cuadratica(x0, y0, x1, y1, x2, y2):
    """
    Función para realizar la interpolación cuadrática y encontrar los coeficientes del polinomio cuadrático.

    Parámetros:
    x0, y0 (float): Primer punto conocido.
    x1, y1 (float): Segundo punto conocido.
    x2, y2 (float): Tercer punto conocido.

    Devuelve:
    tuple: Coeficientes del polinomio cuadrático (a, b, c).
    """
    # Crear el sistema de ecuaciones
    A = np.array([
        [x0**2, x0, 1],
        [x1**2, x1, 1],
        [x2**2, x2, 1]
    ])
    b = np.array([y0, y1, y2])

    # Resolver el sistema para encontrar los coeficientes
    a, b, c = np.linalg.solve(A, b)
    return a, b, c

# Definir los puntos conocidos
x0, y0 = 0, 1
x1, y1 = 1, 3
x2, y2 = 2, 2

# Encontrar los coeficientes del polinomio cuadrático
a, b, c = interpolacion_cuadratica(x0, y0, x1, y1, x2, y2)

# Definir la función del polinomio cuadrático
def P(x):
    return a*x**2 + b*x + c

# Definir los puntos donde se desea estimar los valores
x_nuevo = np.linspace(0, 2, 100)
y_nuevo = P(x_nuevo)

# Graficar los puntos conocidos y el polinomio cuadrático de interpolación
plt.plot([x0, x1, x2], [y0, y1, y2], 'o', label='Puntos conocidos')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación Cuadrática')
plt.show()