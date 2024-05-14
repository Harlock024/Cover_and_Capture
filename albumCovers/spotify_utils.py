from  .spotify_auth import sp

def obtener_portada_album(artist_name, album_name):
    try:
      
        results = sp.search(q=f'artist:{artist_name} album:{album_name}', type='album', limit=1)
        items = results['albums']['items']
        if items:
           
            cover_url = items[0]['images'][0]['url']
            return cover_url
        else:
            print("No se encontró el álbum.")
            return None
    except Exception as e:
        print("Error al buscar el álbum:", e)
        return None
    

