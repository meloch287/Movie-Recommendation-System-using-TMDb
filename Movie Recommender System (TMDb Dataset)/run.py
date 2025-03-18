import pickle
import streamlit as st
import requests

# Константы
TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
TMDB_LANGUAGE = "en-US"
TMDB_POSTER_URL = "https://image.tmdb.org/t/p/w500/"

def retrieve_poster(movie_identifier):
    """
    Извлекает URL постера фильма по его идентификатору через API TMDB.
    
    :param movie_identifier: Уникальный идентификатор фильма
    :return: Полный URL постера фильма
    """
    
    api_url = f"https://api.themoviedb.org/3/movie/{movie_identifier}?api_key={TMDB_API_KEY}&language={TMDB_LANGUAGE}"
    response = requests.get(api_url)
    movie_data = response.json()
    poster_relative_path = movie_data['poster_path']
    poster_full_url = TMDB_POSTER_URL + poster_relative_path
    return poster_full_url

def generate_movie_suggestions(chosen_movie_name):
    """
    Генерирует список рекомендованных фильмов на основе косинусного сходства.
    
    :param chosen_movie_name: Название выбранного пользователем фильма
    :return: Кортеж из списков: названия рекомендованных фильмов и URL их постеров
    """
    movie_position = movie_collection[movie_collection['title'] == chosen_movie_name].index[0]
    similarity_ranking = sorted(list(enumerate(similarity_matrix[movie_position])), reverse=True, key=lambda x: x[1])
    suggested_movie_titles = []
    suggested_movie_posters = []
    for rank in similarity_ranking[1:6]:  # Берем 5 ближайших, исключая сам фильм
        suggested_movie_id = movie_collection.iloc[rank[0]].movie_id
        suggested_movie_posters.append(retrieve_poster(suggested_movie_id))
        suggested_movie_titles.append(movie_collection.iloc[rank[0]].title)
    return suggested_movie_titles, suggested_movie_posters

# Заголовок приложения
st.header('Система рекомендаций фильмов')

# Загрузка данных
movie_collection = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity_matrix = pickle.load(open('model/similarity.pkl', 'rb'))

# Список названий фильмов для выбора
available_movie_titles = movie_collection['title'].values

# Интерфейс выбора фильма
chosen_movie_name = st.selectbox(
    "Введите или выберите фильм из списка",
    available_movie_titles
)

# Обработка нажатия кнопки
if st.button('Показать рекомендации'):
    suggested_titles, suggested_posters = generate_movie_suggestions(chosen_movie_name)
    # Создание колонок для вывода результатов
    display_columns = st.columns(5)
    for column, title, poster in zip(display_columns, suggested_titles, suggested_posters):
        with column:
            st.text(title)
            st.image(poster)