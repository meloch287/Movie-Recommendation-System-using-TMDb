import pandas as pd
import numpy as np
import pickle
import os

# Создаем папку "model", если ее нет
if not os.path.exists('model'):
    os.makedirs('model')

# 1. Создаем данные для movie_list.pkl
# Пример: небольшой список фильмов
movies_data = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Avatar']
}
movies_df = pd.DataFrame(movies_data)

# Сохраняем DataFrame в файл movie_list.pkl
with open('model/movie_list.pkl', 'wb') as f:
    pickle.dump(movies_df, f)

# 2. Создаем матрицу схожести для similarity.pkl
# Пример: матрица 5x5 (для 5 фильмов), где значения от 0 до 1
similarity_matrix = np.array([
    [1.0, 0.8, 0.6, 0.7, 0.3],
    [0.8, 1.0, 0.7, 0.9, 0.4],
    [0.6, 0.7, 1.0, 0.5, 0.6],
    [0.7, 0.9, 0.5, 1.0, 0.2],
    [0.3, 0.4, 0.6, 0.2, 1.0]
])

# Сохраняем матрицу в файл similarity.pkl
with open('model/similarity.pkl', 'wb') as f:
    pickle.dump(similarity_matrix, f)

print("Файлы 'movie_list.pkl' и 'similarity.pkl' успешно созданы в папке 'model'.")