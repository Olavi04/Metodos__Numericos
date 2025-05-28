# Metodo de Simpson 3/8

![](https://raw.githubusercontent.com/Olavi04/Metodos__Numericos/main/Imagenes/Imagenes_Tema4/sinso%206.png)

## Definicion

El método de Simpson 3/8 es un método numérico para aproximar la integral definida de una función en un intervalo dado. Este método es una extensión del método de Simpson 1/3, pero utiliza una fórmula más precisa para mejorar la aproximación.

La fórmula del método de Simpson 3/8 es la siguiente:

![](https://raw.githubusercontent.com/Olavi04/Metodos__Numericos/main/Imagenes/Imagenes_Tema4/sinso%207.png)

## Algoritmo

1. Empezar

2. Definir la función f(x)

3. Lea el límite inferior de integración, el límite superior de
   integración y número de subintervalo

4. Cálculos: tamaño del paso = (límite superior - límite inferior)/número de subintervalo

5. Establecer: valor de integración = f(límite inferior) + f(límite superior)

6. Establecer: i = 1

7. Si i > número de subintervalo, entonces vaya a

8. Calcular: k = límite inferior + i * h

9. Si mod 3 = 0 entonces
     Valor de integración = Valor de integración + 2* f(k)
   De lo contrario
     Valor de integración = Valor de integración + 3 * f(k)
   Terminara si

10. Incremente i en 1, es decir, i = i+1 y vaya al paso 7

11. Calcule: Valor de integración = Valor de integración * tamaño de paso*3/8

12. Mostrar el valor de integración como respuesta requerida

13. Detener

## Metodologia

```python
# Simpson 3/8 

# Definir función a integrar
def f(x):
    return 1/(1 + x**2)

# Implementando Simpson 3/8
def simpson38(x0,xn,n):
    # calcular el tamaño del paso
    h = (xn - x0) / n
    
    # encontrar suma 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%3 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 3 * f(k)
    
    # Encontrar el valor de integración final
    integration = integration * 3 * h / 8
    
    return integration
    
# Sección de entrada
lower_limit = float(input("Introduzca el límite inferior de integración: "))
upper_limit = float(input("Introduzca el límite superior de integración: "))
sub_interval = int(input("Introduzca el número de subintervalos: "))

# Llame al método trapezoidal() y obtenga el resultado
result = simpson38(lower_limit, upper_limit, sub_interval)
print("El resultado de la integración por el método 3/8 de Simpson es: %0.6f" % (result) )
```

# EJEMPLOS

## Ejemplo 1

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/Imagenes_Tema4/sinso%208.png)

## Ejemplo 2

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/Imagenes_Tema4/sinso%209.png)

## Ejemplo 3

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/Imagenes_Tema4/sinso%2010.png)

## Ejemplo 4

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/Imagenes_Tema4/sinso%2011.png)

## Ejemplo 5

![](https://raw.githubusercontent.com/Mexta46/Metodos_Numericos_Tema4/main/Imagenes/Imagenes_Tema4/sinso%2012.png)
