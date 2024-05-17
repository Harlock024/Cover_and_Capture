# views.py
from django.http import JsonResponse
from .models import Album
from spotify_utils import obtener_portada_album

def guardar_album(request):
    if request.method == 'POST':
        artist_name = request.POST.get('artist_name')
        albumName = request.POST.get('albumName')

        cover_url = obtener_portada_album(artist_name, albumName)

        if cover_url:
           
            album = Album(artist_name=artist_name, album_name=albumName, cover_url=cover_url)
            album.save()
            return JsonResponse({'success': True, 'message': 'Álbum guardado correctamente'})
        else:
            return JsonResponse({'success': False, 'message': 'No se pudo encontrar la portada del álbum'})

    return JsonResponse({'success': False, 'message': 'Método no permitido'})

