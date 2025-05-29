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