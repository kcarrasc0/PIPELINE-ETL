import pandas as pd
import streamlit as st
from PIL import Image

# Título
st.title("Top Músicas da playlist 年2000 no spotify")

# Carregar dados
df_spotify = pd.read_csv("spotify_data.csv")
df_youtube = pd.read_csv("youtube_data.csv")


# Mostrar tabela Spotify
st.dataframe(df_spotify)

# YouTube
st.header("Vídeos populares no YouTube")
st.dataframe(df_youtube)

# Gráfico (exemplo)
st.subheader("🎵 Popularidade das músicas")
st.bar_chart(df_spotify.set_index("nome")["popularidade"])
