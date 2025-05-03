import pandas as pd
import streamlit as st
from PIL import Image

# Título
st.title("🎶 Análise de Tendências: Spotify & YouTube")

# Carregar dados
df_spotify = pd.read_csv("spotify_data.csv")
df_youtube = pd.read_csv("youtube_data.csv")

# Carregar imagem
img = Image.open("ALBUM SOUTO MC.png")

# Layout com colunas: imagem ao lado do título
col1, col2 = st.columns([1, 4])
with col1:
    st.image(img, width=100)
with col2:
    st.header("Top músicas da Playlist THIS IS SOUTO MC no Spotify")

# Mostrar tabela Spotify
st.dataframe(df_spotify)

# YouTube
st.header("Vídeos populares no YouTube")
st.dataframe(df_youtube)

# Gráfico (exemplo)
st.subheader("🎵 Popularidade das músicas")
st.bar_chart(df_spotify.set_index("nome")["popularidade"])
