from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='music/')

    def __str__(self):
        return self.title
