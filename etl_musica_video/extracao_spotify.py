import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticação
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="02a8e2e4f3714d97ba1ade9f3af1d539",
    client_secret="75609231399b472fa745205adf602319"
))

# Playlist 
playlist_id = "31VkXgAcOZSmt5wIL1TkkR"  # Top Músicas da playlist 年2000 
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
