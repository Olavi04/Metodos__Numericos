def lagrange_interpolation(x, y, x_val): #evalua la interpolacion y previene que este tenga que dividir entre cero
    n = len(x) #crea una lista con los valores de x
    for i in range(n): #recorre los valores para rectificar que estos no sean los mismo para dividir entre cero
        for j in range(i + 1, n):
            if x[i] == x[j]:
                raise ValueError(f"Los puntos x{i} y x{j} son idénticos, lo que causa una división por cero.") 
    resultado = 0
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x_val - x[j]) / (x[i] - x[j])
        resultado += y[i] * L_i

    return round(resultado,2) #retorna el resultado a dos cifras significativas

try:
    num_points = int(input("Ingrese el número de puntos: ")) #se ingresa la cantidad de puntos a tratar
    if num_points <= 0: #verifica que el numero de puntos a tratar no sea menor a cero
        raise ValueError("El número de puntos debe ser mayor que cero.")

    xP = [] #define una matriz de valores x
    yP = [] #define una matriz de valores x

    for i in range(num_points):
        x = float(input(f"Ingrese x{i}: ")) #se ingresan los valores de x
        y = float(input(f"Ingrese y{i}: ")) #se ingresan los valores de y
        xP.append(x) #agrega los valores de x en la matriz de valores de x
        yP.append(y) #agrega los valores de y en la matriz de valores de y

    x_value = float(input("Ingrese el valor de x para evaluar el polinomio: ")) #pide el valor de x para calcular y
    result = lagrange_interpolation(xP, yP, x_value ) 
    print(f"El valor del polinomio en x = {x_value} es: {result}") #muestra el resultado

except ValueError as e:
    print(f"Error: {e}")
