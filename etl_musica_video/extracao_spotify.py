import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticação
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="b5378e3b030a47908ca495535af59478",
    client_secret="5ad53c1acc8f4995b9b7f0a65c4be670"
))

# Playlist "Top Brasil"
playlist_id = "7xwSv337EetpUTnQLgxFbW"  # Top Músicas da playlist Thi is Souto MC
result = sp.playlist_items(playlist_id, limit=20)

musicas = []
for item in result['items']:
    track = item['track']
    musicas.append({
        "nome": track['name'],
        "artista": track['artists'][0]['name'],
        "popularidade": track['popularity']
    })

df = pd.DataFrame(musicas)
df.to_csv("spotify_data.csv", index=False)
print("Dados do Spotify salvos com sucesso!")
