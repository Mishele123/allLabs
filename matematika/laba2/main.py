import numpy as np
import math




def task1() -> None:
    matrix = np.random.randint(-3, 4, (10, 10))
    minor = matrix[1:5, 6:10]
    print(f"Минор 4-го порядка: {minor}")
    determ = np.linalg.det(minor)
    print(f"Определитель минора: {determ}")

def task2() -> None:
    rows_1 , cols_1 = 3, 4
    rows_2, cols_2 = cols_1, 5
    matrix_1 = np.random.uniform(2, 3, (rows_1, cols_1))
    matrix_2 = np.random.uniform(2, 3, (rows_2, cols_2))
    print(f"Матрица 1: {matrix_1}")
    print(f"Матрица 2: {matrix_2}")

    # Векторный алгоритм
    Res_matrix = np.zeros((rows_1, cols_2))
    for i in range(rows_1):
        for j in range(cols_2):
            Res_matrix[i, j] = np.sum(matrix_1[i, :] * matrix_2[:, j])
    print(f"Результат векторного алгоритма: {Res_matrix}")

    Res_dot = np.dot(matrix_1, matrix_2)
    print(f"Результат dot: {Res_dot}")

    #матричный алгоритм
    Res_matrix = np.zeros((rows_1, cols_2))
    for j in range(cols_2):
        Res_matrix[:, j] = np.dot(matrix_1, matrix_2[:, j])
    print(f"Результат матричного алгоритма: {Res_matrix}")


def task3() -> None:
    vector = np.random.randint(0, 100, (1, 10))


    def calculate_vector_norm(vector):
        sum_of_squares = 0
        for x in vector[0]:
            sum_of_squares += x**2
        norm = math.sqrt(sum_of_squares)        
        return norm
    

    norma = calculate_vector_norm(vector)
    norm_check = np.linalg.norm(vector[0])
    print(f"Вектор: {vector}")
    print(f"Норма: {norma}")
    print(f"Норма(linalg.norm): {norm_check}")

    # задание 5
    np.set_printoptions(precision=4, suppress=True)
    H = householder_reflection(vector)
    transformed_vector = np.dot(H, vector)
    print(f"H: {H}")
    print(f"Преобразованный вектор: {transformed_vector}")


def householder_reflection(vector):
    desired_vector = np.copy(vector)
    desired_vector[3:] = 0
    v = vector - desired_vector
    v_norm = np.linalg.norm(v)
    if v_norm == 0:
        return np.eye(vector.shape[0])
    v = v / v_norm
    H = np.eye(vector.shape[0]) - 2 * np.outer(v, v)
    return H


def task4() -> None:
    eigenvalues = lambda matrix: np.linalg.eigvals(matrix)
    spectral_norm = lambda matrix: np.max(np.abs(eigenvalues(matrix)))
    matrix = np.random.randint(-10, 10, (4, 4))
    calcule_norm = spectral_norm(matrix)
    norm_check = np.linalg.norm(matrix, ord="fro")
    print(f"Случайная матрица: {matrix}")
    print(f"Спектральная норма(вычисленная): {calcule_norm}")
    print(f"Спектральная норма(np.linalg.norm): {norm_check}")

    # Задание 6
    # LU-разложение
    L, U = lu_decomposition(matrix)
    print(f"Матрица L: \n{L}")
    print(f"Матрица U: \n{U}")

    # Проверка результата
    LU = np.dot(L, U)
    print(f"Проверка (L * U): \n{LU}")

    # Задание 7
    Q, R = gram_schmidt(matrix)
    print(f"Матрица Q: \n{Q}")
    print(f"Матрица R: \n{R}")

    QR = np.dot(Q, R)
    print(f"Проверка (Q * R): \n{QR}")

    Q_np, R_np = np.linalg.qr(matrix)
    print(f"Матрица Q (np.linalg.qr): \n{Q_np}")
    print(f"Матрица R (np.linalg.qr): \n{R_np}")

    QR_np = np.dot(Q_np, R_np)
    print(f"Проверка (Q_np * R_np): \n{QR_np}")

def lu_decomposition(matrix):
    """Функция для LU-разложения матрицы"""
    n = matrix.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            U[i, j] = matrix[i, j] - np.sum(L[i, :i] * U[:i, j])

        for j in range(i, n):
            if i == j:
                L[i, j] = 1
            else:
                L[j, i] = (matrix[j, i] - np.sum(L[j, :i] * U[:i, i])) / U[i, i]
    return L, U


def gram_schmidt(matrix):
    """QR-разложение с использованием метода Грама-Шмидта"""
    m, n = matrix.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = matrix[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], matrix[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j] if R[j, j] != 0 else v
    return Q, R


# task1()
# task2()   
# task3()
# task4()