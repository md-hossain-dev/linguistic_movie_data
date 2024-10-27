from django.urls import path
from .views import MovieSearchView, MovieDetailView,MovieDetailSaveDataView

urlpatterns = [
    path('search/', MovieSearchView.as_view(), name='movie_search'),
    path('movie/<int:movie_id>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:movie_id>/', MovieDetailSaveDataView.as_view(), name='movie_details'),
]