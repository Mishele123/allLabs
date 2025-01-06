import math
import sympy
from sympy import *


def task1() -> None:
    x, y = symbols("x y")
    expr = -(4*x*y)/3*(x-y)+(2*x + 3*y)**2
    print("expression:", expr)
    expr2 = sympy.expand(expr)
    print("simplified expression:", expr2)
    subs_dict = {x: 1.038, y: math.sqrt(7)}
    expr3 = expr2.subs(subs_dict)
    print("substitution result:", expr3)


def task2() -> None:
    x, y = symbols("x y")
    expr = -(4*x*y)/3*(x-y)+(2*x + 3*y)**2
    expr1 = sympy.expand(expr)
    der_x = diff(expr1, x)
    der_y = diff(expr1, y)
    print("derivative of x:", der_x)
    print("derivative of y:", der_y)


def task3() -> None:
    x, y = symbols("x y")
    expr = -(4*x*y)/3*(x-y)+(2*x + 3*y)**2
    integ = Integral(expr, x)
    res = integ.doit()
    print("calculated integral:", res)


def task4() -> None:
    x, y = symbols("x y")
    expr = -(4*x*y)/3*(x-y)+(2*x + 3*y)**2
    expr1 = expr.subs(x, 2)
    equat = Eq(expr1, 3)
    res = nonlinsolve([equat], (y,))
    print("result non lin equat:", res)


def task5() -> None:
    x1, x2, x3 = symbols("x1 x2 x3")
    res = linsolve([Eq(x1-x3, 1), Eq(-x1-x2+3*x3, -3), Eq(x1-2*x2-4*x3, 5)], (x1,x2,x3))
    print("result lin equat:", res)


def task6() -> None:
    x = symbols("x")
    expr = sympy.sqrt(x)+x**(2/3)
    res = integrate(expr, (x, 0, 1))
    print("calculated integral:", res)


def task7() -> None:
    x, y = symbols("x y")
    integral = (x - y) * exp(y)
    inner_integral = integrate(integral, (x, 2*y, y), (y, -1, 1))
    print(f"calculated integral: {simplify(inner_integral)}")


if __name__ == "__main__":
    print("Результат task1 = ")
    task1()
    print("Результат task2 = ")
    task2()
    print("Результат task3 = ")
    task3()
    print("Результат task4 = ")
    task4()
    print("Результат task5 = ")
    task5()
    print("Результат task6 = ")
    task6()
    print("Результат task7 = ")
    task7()