from django.db import models

class LinguisticData(models.Model):
    version_id = models.CharField(max_length=10)
    word_count = models.IntegerField()
    char_count = models.IntegerField()
    avg_word_length = models.FloatField()
    language = models.CharField(max_length=50)  # save language name
    original_text = models.TextField()

    def __str__(self):
        return f"Linguistic Data {self.id} - {self.language}"