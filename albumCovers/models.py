from django.db import models
from django.conf import settings


class AlbumCover(models.Model):
   Artist = models.CharField(max_length=100)
   albumName = models.CharField(max_length=100)
   cover_url = models.URLField()
   posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   album_cover = models.ForeignKey('albumCovers.AlbumCover', related_name='votes', on_delete=models.CASCADE)

