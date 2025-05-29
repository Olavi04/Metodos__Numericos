# Interpolacion de Newton

## Definición
La interpolación de Newton es un método numérico utilizado para construir un polinomio de grado n que pase por un conjunto de n+1 puntos dados (x0, y0), (x1, y1), ..., (xn, yn). Este polinomio interpolante, denotado como P(x), se expresa en la forma de Newton:
P(x) = y0 + a1(x - x0) + a2(x - x0)(x - x1) + ... + an(x - x0)(x - x1)...(x - xn-1)
donde los coeficientes a1, a2, ..., an se conocen como diferencias divididas y se calculan a partir de los puntos dados.
Las diferencias divididas se definen recursivamente de la siguiente manera:

f[x0] = y0
f[x0, x1] = (y1 - y0) / (x1 - x0)
f[x0, x1, x2] = (f[x1, x2] - f[x0, x1]) / (x2 - x0)
...
f[x0, x1, ..., xn] = (f[x1, x2, ..., xn] - f[x0, x1, ..., xn-1]) / (xn - x0)

Así, las diferencias divididas representan las pendientes sucesivas de las secantes que unen los puntos dados.

## Algoritmo
1. Obtener los puntos (x0, y0), (x1, y1), ..., (xn, yn).
2. Construir una tabla de diferencias divididas de (n+1) filas y (n+1) columnas.
3. Inicializar la primera columna de la tabla con los valores y0, y1, ..., yn.
4. Calcular las diferencias divididas f[x0, x1], f[x0, x1, x2], ..., f[x0, x1, ..., xn] usando la definición recursiva y llenar la tabla de diferencias divididas.
3. Evaluar el polinomio interpolante P(x) en el punto deseado x utilizando la fórmula de Newton y las diferencias divididas calculadas.

## Metodologia
```python
def Verificador(x, y): # Verifica si los puntos x son únicos para no dar un resultado de divicion por cero y calcula los coeficientes del polinomio interpolante de Newton
    n = len(x) #se define una lista con los valores de x
    coeficiente = [0] * n #se pasa la lista 
    for i in range(n):
        coeficiente[i] = y[i]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            if x[i] == x[i-j]:
                raise ValueError(f"Los puntos x{i} y x{i-j} son idénticos, lo que causa una división por cero.")
            coeficiente[i] = (coeficiente[i] - coeficiente[i-1]) / (x[i] - x[i-j])
    return coeficiente #devuelve una lista de coeficientes del polinomio interpolante de Newton

def newton_polynomial(x_val, x, coeficiente): #Evalua el polinomio interpolante de newton en 
    n = len(x) #se define la lista con los valores de x
    result = coeficiente[0] #realiza de los coeficientes de x y y
    for i in range(1, n):
        termino = coeficiente[i]
        for j in range(i):
            termino *= (x_val - x[j])
        result += termino
    return round(result,2) #retorna la suma a dos cifras significativas


try:
    numP = int(input("Ingrese el número de puntos: ")) #se define el numero de puntos
    if numP <= 0: #verifica que la cantidad de puntos es mayor a cero
        raise ValueError("El número de puntos debe ser mayor que cero.") #retorna un error que acaba el programa

    xP = [] #se define la matris que contrendra los valores de x
    yP = [] #se define la matris que contrendra los valores de y

    for i in range(numP):
        x = float(input(f"Ingrese x{i}: ")) #se ingresa los valores de x
        y = float(input(f"Ingrese y{i}: ")) #se ingresa los valores de y
        xP.append(x) #se ingresa el valor de x en la matris x
        yP.append(y) #se ingresa el valor de y en la matris y

    coeficiente = Verificador(xP, yP)
    print("Coeficientes del polinomio interpolante de Newton:", coeficiente)

    x_value = float(input("Ingrese el valor de x para evaluar el polinomio: ")) #se pide el valor de x para calcular y
    result = newton_polynomial(x_value, xP, coeficiente)
    print(f"El valor del polinomio en x = {x_value} es: {result}")

except ValueError as e:
    print(f"Error: {e}")
```

------

## Ejemplos

------

Ejercicio 1 resuelto: se usaran los parametros
- numero de puntos: 4
- x0: 7
- y0: 8
- x1: 14
- y1: 16
- x2: 21
- y2: 25
- x3: 34
- y3: 45
- valor de x: 5

**Resultado**

![](https://github.com/Mexta46/Metodos_Numericos/blob/9e22efabf9c8dad6b9be0ecdd8d9af81d3d70575/Imagenes/Imagenes_tema5/IN1.png)

------

Ejercicio 2 resuelto: usando los parametros
- numero de puntos: 2
- x0: 24
- y0: 16
- x1: 15
- y1: 17
- valor de x: 25

**Resultado**

![](https://github.com/Mexta46/Metodos_Numericos/blob/9e22efabf9c8dad6b9be0ecdd8d9af81d3d70575/Imagenes/Imagenes_tema5/IN2.png)

-------

Ejercicio 3 resuelto: usando los valores
- numero de puntos: 5
- x0: 24
- y0: 66
- x1: 15
- y1: 23
- x2: 78
- y2: 8
- x3: 9
- y3: 12
- x4: 14
- y4: 20
- valor de x: 7

**Resultado**

![](https://github.com/Mexta46/Metodos_Numericos/blob/9e22efabf9c8dad6b9be0ecdd8d9af81d3d70575/Imagenes/Imagenes_tema5/IN3.png)

--------

Ejercicio 4 resuelto: usando los parametros
- numero de puntos: 2
- x0: 16
- y0: 8
- x1: 12
- y1: 13
- valor de x: 21

**Resultado**

![](https://github.com/Mexta46/Metodos_Numericos/blob/9e22efabf9c8dad6b9be0ecdd8d9af81d3d70575/Imagenes/Imagenes_tema5/IN4.png)

--------

Ejercicio 5 resuelto: usando los parametros
- numero de puntos: 3
- x0: 45
- y0: 78
- x1: 46
- y1: 79
- x2: 112
- y2: 80
- valor de x: 15

**Resultado**

![](https://github.com/Mexta46/Metodos_Numericos/blob/9e22efabf9c8dad6b9be0ecdd8d9af81d3d70575/Imagenes/Imagenes_tema5/IN5.png)