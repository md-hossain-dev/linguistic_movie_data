from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tmdb_api import search_movies, get_movie_details,TMDB_API_KEY,TMDB_BASE_URL
from .models import Movie
import requests

class MovieSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('query', '')
        if not query:
            return Response({"error": "Query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        # search move tmdb api
        try:
            movies = search_movies(query)
            movie_suggestions = [{'id': movie['id'], 'title': movie['title']} for movie in movies]
            return Response(movie_suggestions, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





def get_movie_details_save_data(movie_id):
    # TMDB API URL

    url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}&append_to_response=credits"
    

    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Movie not found or TMDB API error")
    
    movie_data = response.json()
    

    title = movie_data.get("title")
    overview = movie_data.get("overview")
    release_date = movie_data.get("release_date")
    rating = movie_data.get("vote_average")
    actors = ', '.join([actor['name'] for actor in movie_data.get("credits", {}).get("cast", [])[:5]]) 


    movie, created = Movie.objects.update_or_create(
        tmdb_id=movie_id,
        defaults={
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'rating': rating,
            'actors': actors
        }
    )
    
    return {
        "id": movie.id,
        "title": movie.title,
        "overview": movie.overview,
        "release_date": movie.release_date,
        "rating": movie.rating,
        "actors": movie.actors,
    }





class MovieDetailSaveDataView(APIView):
    def get(self, request, movie_id):
        try:
            movie_details = get_movie_details_save_data(movie_id)
            return Response(movie_details, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MovieDetailView(APIView):
    def get(self, request, movie_id):
        try:
            movie_details = get_movie_details(movie_id)
            return Response(movie_details, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)