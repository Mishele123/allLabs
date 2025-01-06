import numpy as np
import scipy as sp
import math
import matplotlib.pyplot as plt


def zadanie1() -> None:
    print("1 задание")
    matrix = np.random.randint(0, 10, (5, 5))
    print(f"Обычная матрица = \n{matrix}")
    print("_______________")
    matrix1 = matrix.transpose()
    print(f"Транспонированная матрица = \n{matrix1}")
    print(f"Определитель матрицы = {np.linalg.det(matrix)}")


def zadanie2() -> None:
    print("2 задание")
    vector = np.array([[1], [2], [3], [4], [5]]) # 5x1
    matrix = np.random.randint(1, 3, (1, 5), int) # 1x5
    print(f"Умножение матриц = \n{np.dot(vector, matrix)}") # 5x5


def zadanie3() -> None:
    print("3 задание")
    matrix = np.array([[1, 0, -1], [-1, -1, 3], [1, -2, -4]], int)
    vec = np.array([1, -3, 5], int)
    print(f"Решение системы уравнений = \n{np.linalg.solve(matrix, vec)}")


def zadanie4() -> None:
    print("Задание 4")
    solve = sp.integrate.quad(lambda x: (math.sqrt(x) + math.pow(x, 2/3)), 0, 1)
    print(f"Значение интегралла = {solve}")


def zadanie5() -> None:
    print("Задание 5")
    def f(x, y) -> float:
        return (x - y) * math.exp(y)
    def upper(x) -> float:
        return x
    def lower(x) -> float:
        return 2 * x

    solve, err = sp.integrate.dblquad(f, -1, 1, lower, upper)
    print(f"Решение двойного логарифма = {solve}")


def zadanie6() -> None:
    print("Задание 6")

    plt.figure(figsize=(8, 5), dpi=80)
    ax = plt.subplot(111)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    X = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
    C, L = 3 * np.sin(X), np.sqrt(X + 5)
    plt.xlabel("X", fontsize = 14)
    plt.ylabel("Y", fontsize = 14)
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="sin Function")
    plt.plot(X, L, color="red", linewidth=2.5, linestyle="-", label="grad Function")
    plt.xticks([-2*np.pi, -3*np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3*np.pi / 2, 2*np.pi ],
           [r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$', r'$+3 \pi/2$', r'$+ 2\pi$' ])
    plt.ylim(C.min() * 1.1, C.max() * 1.1)
    plt.yticks([-2, -1, +1, +2],
            [r'$-2$', r'$-1$', r'$+1$', r'$+2$'])
    intersection_x = []
    intersection_y = []
    for x in X:
        if np.isclose(3 * np.sin(x), np.sqrt(x + 5), atol=0.0595):
            intersection_x.append(x)
            intersection_y.append(3 * np.sin(x))
    if intersection_x:
        plt.scatter(intersection_x, intersection_y, color='green', zorder=5, label='Intersection Points')
    plt.legend(loc='lower left', frameon=False)
    plt.grid()
    ax.annotate('', xy=(2 * np.pi + 0.5, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=1.2))
    ax.annotate('', xy=(0, 2), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=1))
    ax.set_xlabel("Axis X", fontsize=15, labelpad=130)
    ax.set_ylabel("Axis Y", fontsize=15, labelpad=200)
    plt.show()


def main():
    zadanie1()
    zadanie2()
    zadanie3()
    zadanie4()
    zadanie5()
    zadanie6()


if __name__ == "__main__":
    main()