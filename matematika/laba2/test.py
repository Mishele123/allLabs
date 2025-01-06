import numpy as np

def householder_reflection(vector):
    # Создаем желаемый вектор, обнуляя элементы с 4 по 10
    desired_vector = np.copy(vector)
    desired_vector[3:] = 0  # Обнуляем элементы с 4 по 10 (индексы 3 и далее)
    print(desired_vector)
    # Находим вектор для отражения
    v = vector - desired_vector
    v_norm = np.linalg.norm(v)

    # Если вектор v равен нулю, отражение не нужно
    if v_norm == 0:
        return np.eye(vector.shape[0])  # Возвращаем единичную матрицу

    # Нормируем вектор v
    v = v / v_norm

    # Формируем матрицу отражения
    H = np.eye(vector.shape[0]) - 2 * np.outer(v, v)

    return H

# Пример использования
def main():
    # Исходный вектор
    vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Исходный вектор: {vector}")

    # Находим матрицу отражения Хаусхолдера
    H = householder_reflection(vector)
    
    # Применяем отражение
    transformed_vector = np.dot(H, vector)
    
    print(f"Матрица отражения H:\n{H}")
    print(f"Преобразованный вектор: {transformed_vector}")

main()