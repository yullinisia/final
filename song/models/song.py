from django.db import models
<<<<<<< HEAD
from song.models.singer import Singer
from song.models.album import Album

class Song(models.Model):
    title = models.CharField(max_length=200)
    singer = models.ForeignKey(Singer, on_delete=models.SET_NULL, null=True)
    album = models.ManyToManyField(Album)
=======

class Song(models.Model):
    title = models.CharField(max_length=200)
    singer = models.ForeignKey('Singer', on_delete=models.SET_NULL, null=True)
    album = models.ManyToManyField('Album')
>>>>>>> bdeff8bd9231a1870ad2c31e6ae8da47a0f24064
    date_published = models.DateField(null=True, blank=True)

class Meta:
    app_label = 'song'

def __str__(self):
       return f'{self.title}'

