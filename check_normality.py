"""Функция для проверки нормальности выборки по Колмогорову-Смирнову и Шапиро-Уилку"""

import numpy as np
from scipy import stats

def check_normality(data, sample_num):
    # Тест Колмогорова-Смирнова
    ks_statistic, ks_p_value = stats.kstest(data, 'norm', args=(np.mean(data), np.std(data)))

    # Тест Шапиро-Уилка
    shapiro_statistic, shapiro_p_value = stats.shapiro(data)

    # Вывод результатов
    print(f"\nРезультаты для выборки {sample_num}:")
    print(f"Тест Колмогорова-Смирнова: Статистика = {ks_statistic}, p-значение = {ks_p_value}")
    print(f"Тест Шапиро-Уилка: Статистика = {shapiro_statistic}, p-значение = {shapiro_p_value}")

    # Интерпретация результатов
    alpha = 0.05
    if ks_p_value > alpha:
        print(f"По результатам теста Колмогорова-Смирнова для выборки {sample_num} выборка может быть нормальной (не отвергаем H0).")
    else:
        print(f"По результатам теста Колмогорова-Смирнова для выборки {sample_num} выборка не является нормальной (отвергаем H0).")

    if shapiro_p_value > alpha:
        print(f"По результатам теста Шапиро-Уилка для выборки {sample_num} выборка может быть нормальной (не отвергаем H0).")
    else:
        print(f"По результатам теста Шапиро-Уилка для выборки {sample_num} выборка не является нормальной (отвергаем H0).")