import requests

TMDB_API_KEY = ''
TMDB_BASE_URL = 'https://api.themoviedb.org/3'

def search_movies(query):
    url = f"{TMDB_BASE_URL}/search/movie?api_key={TMDB_API_KEY}&query={query}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['results']

def get_movie_details(movie_id):
    url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
