
# #1.2
# # В другом Python скрипте или интерактивной сессии
# import my_module  # Выведет "Модуль my_module загружается"
# import my_module  # Не выводит ничего при повторном импорте

# #1.3
# from some_module import GLOBAL_VAR
# GLOBAL_VAR = 42
#
#
# import some_module
# some_module.GLOBAL_VAR = 42

#1.4
# from your_module import *
#
# print(var1)
# function1()
#
# print(var2)
# function2()

#2.1

# import numpy as np
# import matplotlib.pyplot as plt
#
# def generate_random_sprite():
#     sprite = np.zeros((5, 5))
#
#     for i in range(3):
#         for j in range(5):
#             sprite[i][j] = np.random.randint(0, 2)
#
#     for i in range(3):
#         for j in range(5):
#             sprite[4 - i][j] = sprite[i][j]
#
#     return sprite
#
# sprite = generate_random_sprite()
#
# rotated_sprite = np.rot90(sprite)
#
# plt.imshow(rotated_sprite, cmap='gray', interpolation='nearest')
# plt.axis('off')
# plt.show()

#2.7
from PIL import Image

def get_rgb_values(image_filename):
    # Открываем изображение
    with Image.open(image_filename) as img:
        # Загружаем данные о пикселях
        pixels = img.load()

        # Инициализируем список для хранения RGB значений
        rgb_values = []

        # Проходим по каждому пикселю изображения
        for i in range(img.height):
            row = []
            for j in range(img.width):
                row.append(pixels[j, i])
            rgb_values.append(row)

        return rgb_values

# Пример вызова функции (для проверки)
image_path = "ph1.jpg"
rgb_matrix = get_rgb_values(image_path)
print(rgb_matrix)






#3.11
#3.12
#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Загрузка данных
# file_path = '/Users/po_scripty/Documents/pythonprac/GAMES.csv'
# games_df_full = pd.read_csv(file_path, header=None, names=['Name', 'Genre', 'URL', 'Year'], sep=';')
#
# # Очистка данных
# # Удаление строк, где год не указан или не является числом
# games_df_full = games_df_full[games_df_full['Year'].str.isnumeric()]
# games_df_full['Year'] = games_df_full['Year'].astype(int)
#
# # Анализ данных
# # Подсчет количества игр по годам
# yearly_counts_full = games_df_full['Year'].value_counts().sort_index()
#
# # Группировка данных по годам и жанрам
# genre_yearly_full = games_df_full.groupby(['Year', 'Genre']).size().unstack(fill_value=0)
#
# # Визуализация данных
# # График количества игр по годам
# plt.figure(figsize=(10, 6))
# yearly_counts_full.plot(kind='bar', color='skyblue')
# plt.title('Количество игр, выпущенных по годам')
# plt.xlabel('Год')
# plt.ylabel('Количество игр')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()
#
# # Стековый график популярности жанров по годам
# plt.figure(figsize=(12, 8))
# genre_yearly_full.plot(kind='bar', stacked=True, colormap='viridis')
# plt.title('Популярность жанров игр по годам')
# plt.xlabel('Год')
# plt.ylabel('Количество игр')
# plt.legend(title='Жанр')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()
