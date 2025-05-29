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