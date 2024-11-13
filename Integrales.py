from sympy import symbols, integrate, sympify

x = symbols('x')
funcion_str = input("Ingrese la función f(x): ")
funcion = sympify(funcion_str)

es_definida = input("¿Desea una integral definida? (si/no): ")

if es_definida == 'si':
    a = float(input("Ingrese el límite inferior: "))
    b = float(input("Ingrese el límite superior: "))
    resultado = integrate(funcion, (x, a, b))
    print(f"La integral definida de {funcion} de {a} a {b} es: {resultado}")
else:
    resultado = integrate(funcion, x)
    print(f"La integral indefinida de {funcion} es: {resultado}")