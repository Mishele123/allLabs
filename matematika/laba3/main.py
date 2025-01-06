import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

from prettytable import PrettyTable



def f(x) -> float:
    return -1.38 * x**3 - 5.42 * x**2 + 2.57 * x + 10.95


def df(x):
    return -4.14 * x**2 - 10.84 * x + 2.57


def draw_graphic():
    x = np.linspace(-5, 3, 1000)
    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x))
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции')
    plt.show()


def pol_del(a, b, tol):
    """
    Метод половинного деления
    """
    if f(a) * f(b) >= 0:
        print('Корень не найден на данном интервале')
        return None
    table = PrettyTable()
    table.field_names = ["Итерация", "a", "b", "c", "f(c)"]
    
    c = a
    iterations = 0
    while abs(b - a) >= tol:
        c = (a + b) / 2
        table.add_row([iterations, f"{a:.6f}", f"{b:.6f}", f"{c:.6f}", f"{f(c):.6f}"])
        iterations += 1
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    print("Метод половинного деления:")
    print(table)
    return c, iterations


def metod_hord(x0, x1, tol):
    """
    Метод хорд
    """
    f_x0 = f(x0)
    f_x1 = f(x1)
    x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
    
    table = PrettyTable()
    table.field_names = ["Итерация", "x0", "x1", "x2", "f(x2)"]
    table.add_row([0, f"{x0:.6f}", f"{x1:.6f}", f"{x2:.6f}", f"{f(x2):.6f}"])
    iterations =  1
    while abs(x2 - x1) >= tol:
        x0 = x1
        x1 = x2
        f_x0 = f_x1
        f_x1 = f(x1)
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        table.add_row([iterations, f"{x0:.6f}", f"{x1:.6f}", f"{x2:.6f}", f"{f(x2):.6f}"])
        iterations += 1

    print("Метод хорд:")
    print(table)
    return x2, iterations


def newton_method(x0, tol = 0.001):
    table = PrettyTable()
    table.field_names = ["Итерация", "x", "f(x)", "f'(x)", "x - f(x)/f'(x)"]

    x = x0
    iterations = 0
    while abs(f(x)) > tol:
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Производная равна нулю, метод Ньютона не применим")
            return None, None
        x_next = x - fx / dfx
        table.add_row([iterations, f"{x:.6f}", f"{fx:.6f}", f"{dfx:.6f}", f"{x_next:.6f}"])
        x = x_next
        iterations += 1

    print("Метод Ньютона")
    print(table)
    return x, iterations


def fixed_point(x0, tol=0.001):
    table = PrettyTable()
    table.field_names = ["Итерация", "x", "f(x)", "x - f(x)/f'(x)"]

    x = x0
    iterations = 0
    while abs(f(x)) >= tol:
        x_next = x - f(x) / df(x)
        table.add_row([iterations, f"{x:.6f}", f"{f(x):.6f}", f"{abs(x - x_next):.6f}"])
        x = x_next
        iterations += 1

    print("Метод последовательных приближений:")
    print(table)
    return x, iterations


#draw_graphic()
print('Метод половинного деления: сходится')
print('Метод хорд: сходится')
print('Метод Ньютона: сходится')
print('Метод последовательных приближений: сходится')

# метод половинного деления
print(pol_del(-5, -2, 0.001))
print(pol_del(-2, 0, 0.001))
print(pol_del(0, 3, 0.001))

# метод хорд
print(metod_hord(-5, -3, 0.001))
print(metod_hord(-2, 0, 0.001))
print(metod_hord(0, 3, 0.001))

# метод Ньютона
print(newton_method(-5, 0.001))
print(newton_method(-2, 0.001))
print(newton_method(1, 0.001))

# метод последовательных приближений
print(fixed_point(-5, 0.001))
print(fixed_point(-2, 0.001))
print(fixed_point(1, 0.001))


# Проверка решений
x = sp.symbols('x')
function = -1.38 * x**3 - 5.42 * x**2 + 2.57 * x + 10.95

solutions = sp.solve(function, x)
print(solutions)