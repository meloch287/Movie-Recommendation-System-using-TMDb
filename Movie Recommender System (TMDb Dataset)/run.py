import pickle
import streamlit as st
import requests
from requests.exceptions import RequestException

# Константы для TMDB API
TMDB_API_KEY = "86ad30107fe22e81f7759f97e59d46a4"
TMDB_LANGUAGE = "en-US"
TMDB_POSTER_URL = "https://image.tmdb.org/t/p/w500/"

def fetch_movie_details(movie_identifier):
    """
    Получает данные о фильме из TMDB API, включая URL постера и рейтинг.

    :param movie_identifier: Уникальный идентификатор фильма
    :return: Словарь с 'poster_url' и 'rating'
    """
    api_url = f"https://api.themoviedb.org/3/movie/{movie_identifier}?api_key={TMDB_API_KEY}&language={TMDB_LANGUAGE}"
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        movie_data = response.json()
        # Формируем URL постера, если он есть
        poster_url = TMDB_POSTER_URL + movie_data['poster_path'] if 'poster_path' in movie_data and movie_data['poster_path'] else None
        # Проверяем наличие рейтинга
        if movie_data.get('vote_count', 0) > 0:
            rating = str(round(movie_data['vote_average'], 1))
        else:
            rating = 'Нет рейтинга'
        return {'poster_url': poster_url, 'rating': rating}
    except RequestException as e:
        print(f"Ошибка при получении данных для фильма с ID {movie_identifier}: {e}")
        return {'poster_url': None, 'rating': 'N/A'}

def generate_movie_suggestions(chosen_movie_name):
    """
    Генерирует список рекомендованных фильмов с их названиями, URL постеров и рейтингами.

    :param chosen_movie_name: Название выбранного пользователем фильма
    :return: Список словарей с данными о фильмах
    """
    movie_position = movie_collection[movie_collection['title'] == chosen_movie_name].index[0]
    similarity_ranking = sorted(list(enumerate(similarity_matrix[movie_position])), reverse=True, key=lambda x: x[1])
    suggested_movies = []
    for rank in similarity_ranking[1:6]:  # Топ-5 похожих фильмов
        movie_idx = rank[0]
        title = movie_collection.iloc[movie_idx].title
        movie_id = movie_collection.iloc[movie_idx].movie_id
        details = fetch_movie_details(movie_id)
        suggested_movies.append({
            'title': title,
            'poster_url': details['poster_url'],
            'rating': details['rating']
        })
    return suggested_movies

st.header('Система рекомендаций фильмов')

movie_collection = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity_matrix = pickle.load(open('model/similarity.pkl', 'rb'))

available_movie_titles = movie_collection['title'].values


chosen_movie_name = st.selectbox(
    "Введите или выберите фильм из списка",
    available_movie_titles
)

# Обработка нажатия кнопки
if st.button('Показать рекомендации'):
    suggested_movies = generate_movie_suggestions(chosen_movie_name)
    display_columns = st.columns(5)
    for column, movie in zip(display_columns, suggested_movies):
        with column:
            # Отображаем название с рейтингом в скобках
            title_with_rating = f"{movie['title']} ({movie['rating']})"
            st.text(title_with_rating)
            # Показываем постер, если он доступен
            if movie['poster_url']:
                st.image(movie['poster_url'])
