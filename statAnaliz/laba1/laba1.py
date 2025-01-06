import scipy.stats as sts
import numpy as np
import math
import matplotlib.pyplot as plt


def normal_distribution(a = -1, sigma = 1, n_points = 100):
    """Модулирует выборку из N независ наблюдений по нормальному закону распределения
    a - среднее значение
    sigma - стандартное отклонение
    """
    distribution = sts.norm.rvs(loc = a, scale = sigma, size = n_points)
    return distribution


def create_frequency_table(data, sigma = 1, n_points = 100):
    """Создание интервального ряда абсолютных и относительных частот и их графики"""
    interval_num = math.ceil(3.5 * sigma / (n_points**(1/3)))
    freq, bins = np.histogram(data, bins=interval_num)
    print(f"Интервалы: {bins}")
    print(f"Частоты по интервалам: {freq}")
    freq_sum = np.sum(freq)
    print(f"Сумма абсолютных частот: {freq_sum}")
    relative_freq = freq / freq_sum
    print(f"Относительные частоты: {relative_freq}")
    relative_freq_sum = sum(relative_freq)
    print(f"Сумма относительных частот: {relative_freq_sum}")
    # Диаграмма абсолютных частот
    plt.hist(data, bins = bins, edgecolor = "black", alpha = 0.7)
    plt.title(f"Диаграмма аблолютных частот с {interval_num} интервалом")
    plt.xlabel("Интервалы")
    plt.ylabel("Абсолютная частота")
    plt.xticks(bins, np.round(bins, 1))
    plt.show()

    # диаграмма относительных частот
    center_bins = (bins[:-1] + bins[1:]) / 2 # Находим центр каждого интервала
    plt.bar(center_bins, relative_freq, width = np.diff(bins), edgecolor = "black", alpha = 0.7)
    plt.title(f"Диаграмма относительных частот с {interval_num} интервалом")
    plt.xlabel("Интервалы")
    plt.ylabel("Относительная частота")
    plt.xticks(bins, np.round(bins, 1))
    plt.show()


create_frequency_table(normal_distribution())