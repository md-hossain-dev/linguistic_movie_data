from django.db import models

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)  # TMDB ID
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    actors = models.TextField()  # Actors list as a string

    def __str__(self):
        return self.title