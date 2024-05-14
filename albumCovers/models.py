from django.db import models
from django.conf import settings


class AlbumCover(models.Model):
   Artist = models.CharField(max_length=100)
   album_name = models.CharField(max_length=100)
   cover_url = models.URLField()
   created_at = models.DateTimeField(auto_now_add=True)
   
   class Meta:
      ordering = ['-created_at']
posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Vote(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   album_cover = models.ForeignKey(AlbumCover, related_name='votes', on_delete=models.CASCADE)

