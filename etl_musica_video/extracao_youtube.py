import pandas as pd
from googleapiclient.discovery import build


youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode="BR",
    maxResults=20
)
response = request.execute()

videos = []
for item in response['items']:
    videos.append({
        "titulo": item['snippet']['title'],
        "canal": item['snippet']['channelTitle'],
        "visualizacoes": int(item['statistics'].get('viewCount', 0)),
        "likes": int(item['statistics'].get('likeCount', 0))
    })

df = pd.DataFrame(videos)
df.to_csv("youtube_data.csv", index=False)
print("Dados do YouTube salvos com sucesso!")
