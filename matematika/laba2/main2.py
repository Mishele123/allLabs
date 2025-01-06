import numpy as np
from prettytable import PrettyTable
from main import lu_decomposition, householder_reflection



# 1 задание
print("Задание 1")
def solve_upper_triangular_system(order, B):
    A = np.random.randint(1, 10, size=(order, order)).astype(float)
    A = np.triu(A)

    def back_substitution(A, B):
        n = len(B)
        X = np.zeros(n)
        for i in range(n-1, -1, -1):
            X[i] = (B[i] - np.dot(A[i, i+1:], X[i+1:])) / A[i, i]
        return X

    X_back_substitution = back_substitution(A, B)

    X_np_solve = np.linalg.solve(A, B)

    print("Матрица A:\n", A)
    print("Вектор B:\n", B)
    print("Решение методом обратной подстановки:\n", X_back_substitution)
    print("Решение методом np.solve:\n", X_np_solve)


B = np.array([1, 2, 3, 4, 5], dtype=float)
solve_upper_triangular_system(5, B)

# 2 задание
print("Задание 2")
def solve_linear_system_lu(A, B):
    """
    методом LU-разложения.
    """
    L, U = lu_decomposition(A)
    
    y = np.linalg.solve(L, B)
    
    x = np.linalg.solve(U, y)
    
    return x
    

A = np.array([[4.4, -2.5, 19.2, -10.8],
              [5.5, -9.3, -14.2, 13.2],
              [7.1, -11.5, 5.3, -6.7],
              [14.2, 23.4, -8.8, 5.3]])
B = np.array([4.3, 6.8, -1.8, 7.2])

solution = solve_linear_system_lu(A, B)
print("Решение системы:")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])
print("x4 =", solution[3])

# 3 задание
print("Задание 3")
def qr_decomposition_householder(A):
    """
    QR-разложение метода Хаусхолдера
    """
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()
    
    for j in range(n):
        v = R[j:, j]
        H = householder_reflection(v)
        R[j:, j:] = np.dot(H, R[j:, j:])
        Q[:, j:] = np.dot(Q[:, j:], H.T)
    
    return Q, R


def solve_linear_system_qr(A, B):
    """
    Решение системы методом QR-разложения.
    
    """
    # QR-разложение
    Q, R = qr_decomposition_householder(A)
    
    # Решение системы Rx = Q.T@B
    x = np.linalg.solve(R, np.dot(Q.T, B))
    
    return x

# Решение системы
solution_qr = solve_linear_system_qr(A, B)
print("Решение системы (QR-разложение):")
print("x1 =", solution_qr[0])
print("x2 =", solution_qr[1])
print("x3 =", solution_qr[2])
print("x4 =", solution_qr[3])

# Проверка
print("\nПроверка решения:")
print("Ax =", np.dot(A, solution_qr))
print("B =", B)

# Решение С помощью np.linalg.solve()
solution_np = np.linalg.solve(A, B)
print("\nРешение системы (np.linalg.solve()):")
print("x1 =", solution_np[0])
print("x2 =", solution_np[1])
print("x3 =", solution_np[2])
print("x4 =", solution_np[3])


# 4 Задание
# Исходная система уравнений
A = np.array([[3.5, -1.7, 2.8], 
              [4.1, 5.8, -1.7],
              [-1.4, -2.5, 3]])
b = np.array([1.7, 0.8, 2.1])


# Проверка условия сходимости метода простых итераций
row_sums = np.abs(A).sum(axis=1)
if np.all(row_sums < 1):
    print("Условие сходимости выполняется.")
else:
    print("Условие сходимости не выполняется. Необходимо преобразовать систему.")

x0 = np.zeros_like(b)
tol = 1e-3
max_iter = 100
iteration = 0

table = PrettyTable()
table.field_names = ["Итерация", "x1", "x2", "x3"]

while True:
    x_new = np.copy(x0)
    for i in range(len(A)):
        x_new[i] = (b[i] - np.dot(A[i, :i], x0[:i]) - np.dot(A[i, i+1:], x0[i+1:])) / A[i, i]
    
    if np.max(np.abs(x_new - x0)) < tol:
        break
    
    x0 = x_new
    iteration += 1
        
    table.add_row([iteration, x0[0], x0[1], x0[2]])
    
    if iteration >= max_iter:
        print("Достигнуто максимальное число итераций.")
        break

print(table)


print("Полученное решение:")
print(x0)

print("Проверка решения:")
print(np.dot(A, x0))
print(b)



# 5 Задание
# Коэффициенты системы
A = np.array([
    [4.4, -2.5, 19.2, -10.8],
    [5.5, -9.3, -14.2, 13.2],
    [7.1, -11.5, 5.3, -6.7],
    [14.2, 23.4, -8.8, 5.3],
    [8.2, -3.2, 14.2, 14.8]
])

# Вектор правых частей
B = np.array([4.3, 6.8, -1.8, 7.2, -8.4])

# Вычисление псевдообратной матрицы
A_pseudo = np.linalg.inv(A.T.dot(A)).dot(A.T)

# Нахождение псевдорешения
x_pseudo = A_pseudo.dot(B)

print("Псевдорешение системы:")
print(x_pseudo)