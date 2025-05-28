# Regla del trapecio
## Definición
La regla del trapecio es un método de aproximación numérica utilizado para estimar el valor de una integral definida. Consiste en aproximar el área bajo una curva mediante el área de trapecios formados por segmentos rectos. La regla del trapecio se basa en dividir el intervalo de integración en pequeños segmentos y aproximar el área bajo la curva en cada segmento con un trapecio cuya base superior coincide con el valor de la función en un extremo del segmento y cuya base inferior coincide con el valor de la función en el otro extremo. La suma de las áreas de estos trapecios proporciona una aproximación al valor de la integral.
## Algoritmo
1. Definir el intervalo de integración [a, b] y el número de subintervalos n en los que se dividirá el intervalo.
2. Calcular el ancho de cada subintervalo: h = (b - a) / n
3. Evaluar la función en los puntos extremos del intervalo (a y b) y en los puntos intermedios (xi = a + i*h, donde i = 1, 2, ..., n-1).
4. Calcular la aproximación de la integral definida utilizando la fórmula del trapecio: Integral aproximada = (h/2) * (f(a) + 2*[f(x1) + f(x2) + ... + f(xn-1)] + f(b)) Donde f(a), f(b) y f(xi) son los valores de la función evaluada en los puntos correspondientes.
5. Cuantos más subintervalos se tomen (es decir, mayor sea n), más precisa será la aproximación de la integral.
## Metodología
```python
fun = "" #Es una variable global que contendra la exprecion de la funcion a usar 
def f(x): #Es el metodo que evalua la expresion y cambia algunos terminos para hacerlo mas complencible
    try: 
        expresion = fun.replace("x", f"{x}") #rempleaza la variable x con la constante que se va a evaluar
        expresion2 = expresion.replace("^", "**") #remplaza el simbolo que nosotros conocemos para potenciar por una que python entiende como potenciador
        expresion3 = expresion2.replace("e", "2.71828") #remplaza las constantes e que estan en la expresion por su valor
        resultado = eval(expresion3) #evalua la expresion convirtiendola de algebraico a aritmetico y retorna su valor final
        return resultado # retorna el resultado de la expresion evaluada
    except Exception as e: #Captura el error que puede ocacionar si no se coloca bien la exprecion
        print("La expresion esta mal, tienes que usar la variable x dentro de la expresion y cada vez que tienes que mutiplicar un numero con una variable tienes que usar *, por ejemplo 3*x^2")
        return None #retorna valor nulo
def trapecio(a, b, n):# Es el metodo que realiza los calculos basado en la formula de la regla del trapecio
    h = (b - a) / n # se calcula la altura de cada trapecio
    if f(a) == None: # corta el metodo si hay un error en la expresion
        return None # retorna un valor nulo
    suma = f(a) + f(b) # se realiza la sumatoria de la funcion de a y b
    for i in range(1, n): # se declara un ciclo for con un rango de 1 hasta n numero de veces
        x = a + i * h # se calcula el trapecio que esta en medio de los limites 
        suma += 2 * f(x) # se calcula la funcion de ese trapecio
    integral = (h / 2) * suma # al final se suma todo y se multiplica por la hlatura sobre dos
    return round(integral, 2) # retorna el resultado en 2 cifras significativas
fun = input("Ingresa la expresion algebraica con la variable x y usando el signo de multiplicacion para cada variable x que se multiplica con un numero:") #se ingresa y asigna la expresion de la funsion en la variable global
try:
    a = float(input("Ingresa el limite inferior:"))# se registra el limite inferior en la variable a
    b = float(input("Ingresa el limite superior:"))# se registra el limite superior en la variable b
    n = int(input("Ingresa la cantidad de subintervalos a usar:"))# se registra la cantidad de subintervalos
    resultado = None #iniciamos la variable donde se captura el resultado y lo iniciamos con un valor nulo
    if(b<a): # evaluamos que el limite inferior no sea mayor que el superior
        print("El limite inferior no puede ser mayor al limite superior")
    elif(n<=0): # evaluamos que la cantidad de subintervalos sea mayor que cero
        print("El numero de intervalos debe ser mayor que cero")
    else:
        resultado = trapecio(a, b, n) # llamamos al metodo que calculara la integral por el metodo de trapecio
    if(resultado!=None): # si la expresion esta mal el metodo retornara un valor nulo aqui nos aseguramos de que resultados no tenga ese valor
        print(f"La aproximación de la integral definida en el intervalo [{a}, {b}] con {n} subintervalos es: {resultado}")
    else:# si de lo contrario el metodo retorna ese valor solo se mostrara un mensaje que los datos ingresados esta mal
        print("Los datos que ingresaste son incorrectos")
except Exception as e: # captura los errores al ingresar los datos equivocados, como poner letras al ingresar los limites o la cantidad de subintervalos
    print("Los datos que ingresaste son incorrectos")
```

## Ejemplos

------------

1- Resolver la integral con la funcion 3x con los limites [1,2] y con 5 subintervalos

Solución:

![](https://github.com/Mexta46/Metodos_Numericos/blob/3abb8cf12a2b67d8b0bcf6d2d3f39078d6474753/Imagenes/Imagenes_Tema4/Ejemplo1Trap.png)

------------

2- Resolver la integral con la funcion x^2 con los limites [1,3] y con 5 subintervalos

Solución:

![](https://github.com/Mexta46/Metodos_Numericos/blob/3abb8cf12a2b67d8b0bcf6d2d3f39078d6474753/Imagenes/Imagenes_Tema4/Ejemplo2Trap.png)

------------

3- Resolver la integral con la funcion x^3-6x^2+11x-6 con los limites [1.3,1.8] y con 1 subintervalo

Solución:

![](https://github.com/Mexta46/Metodos_Numericos/blob/3abb8cf12a2b67d8b0bcf6d2d3f39078d6474753/Imagenes/Imagenes_Tema4/Ejemplo3Trap.png)

------------

4- Resolver la integral con la funcion e^x^2 con los limites [2,4] y con 5 subintervalos

Solución:

![](https://github.com/Mexta46/Metodos_Numericos/blob/3abb8cf12a2b67d8b0bcf6d2d3f39078d6474753/Imagenes/Imagenes_Tema4/Ejemplo4Trap.png)

------------

5- Resolver la integral con la funcion 5x^5 con los limites [1,3] y con 10 subintervalos

Solución:

![](https://github.com/Mexta46/Metodos_Numericos/blob/3abb8cf12a2b67d8b0bcf6d2d3f39078d6474753/Imagenes/Imagenes_Tema4/Ejemplo5Trapecio.png)
