from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audios/')
    duration = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.title