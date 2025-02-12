import numpy as np
from scipy.stats import boxcox

def apply_boxcox(data, lmbda=None):
    """
    Применяет преобразование Бокса-Кокса к данным.

    :param data: array-like
        Набор данных, который необходимо преобразовать. Значения должны быть положительными.
    :param lmbda: float, optional
        Параметр λ для преобразования. Если None, оптимальный λ будет вычислен автоматически.
    :return: tuple (transformed_data, lmbda)
        Преобразованные данные и значение λ.
    """
    # Проверяем, что все значения положительные
    if np.any(data <= 0):
        raise ValueError("Все значения в данных должны быть положительными для применения Box-Cox.")

    # Применяем преобразование
    transformed_data, optimal_lmbda = boxcox(data, lmbda=lmbda)

    return transformed_data, optimal_lmbda