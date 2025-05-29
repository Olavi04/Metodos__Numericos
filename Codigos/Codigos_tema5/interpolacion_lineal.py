def interpolacion_lineal(x0, y0, x1, y1, x):
    m = (y1 - y0) / (x1 - x0)
    y = (m * (x - x0)) + y0
    return y

def main():
    x0 = 1.0
    y0 = 75.0
    x1 = 3.0
    y1 = 100.0
    
    x = 6
    
    y = interpolacion_lineal(x0, y0, x1, y1, x)
    
    print(f"El valor de y para x = {x} es: {y}")

if __name__ == "__main__":
    main()