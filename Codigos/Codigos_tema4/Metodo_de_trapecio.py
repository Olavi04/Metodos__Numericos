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