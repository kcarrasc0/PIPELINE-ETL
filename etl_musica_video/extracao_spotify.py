import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticação
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(

result = sp.playlist_items(playlist_id, limit=20)

musicas = []

for item in result['items']:
    track = item['track']

    nome_musica = track.get('name', 'Desconhecido')
    nome_artista = track.get('artists', [{}])[0].get('name', 'Desconhecido')
    popularidade = track.get('popularity', 0)

    musicas.append({
        "nome": nome_musica,
        "artista": nome_artista,
        "popularidade": popularidade
    })


df = pd.DataFrame(musicas)
df.to_csv("spotify_data.csv", index=False)
print("Dados do Spotify salvos com sucesso!")
