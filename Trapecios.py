import sympy as sp

def metodo_trapecio(funcion, a, b, n):
    x = sp.symbols('x')
    h = (b - a) / n
    puntos = [a + i * h for i in range(n + 1)]
    area = 0
    for i in range(n):
        f_xi = funcion.subs(x, puntos[i])
        f_xi1 = funcion.subs(x, puntos[i + 1])
        area += (f_xi + f_xi1) * h / 2
    return area

x = sp.symbols('x')
expr_str = input("Ingresa la función en términos de x: ")
funcion = sp.sympify(expr_str)
a = float(input("Ingresa el límite inferior: "))
b = float(input("Ingresa el límite superior: "))
n = int(input("Número de trapecios para la aproximación: "))

area_aproximada = metodo_trapecio(funcion, a, b, n)
print("Área aproximada bajo la curva:", area_aproximada)