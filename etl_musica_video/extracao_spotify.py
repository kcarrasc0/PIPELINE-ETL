import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticação
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="0771db6a29d0452eb9ac0504e73ba551",
    client_secret="7c133c4acb584fc1b9b065927a283daf"
))


playlist_id = "4oEOPYBlYOOGKzhQgDxLKy"  
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
