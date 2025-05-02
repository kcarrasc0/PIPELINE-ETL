import pandas as pd
import streamlit as st

# Título
st.title("🎶 Análise de Tendências: Spotify & YouTube")

# Carregar dados
df_spotify = pd.read_csv("spotify_data.csv")
df_youtube = pd.read_csv("youtube_data.csv")

# Spotify
st.header("Top músicas da Playlist THIS IS SOUTO MC no Spotify")
st.dataframe(df_spotify)

# YouTube
st.header("Vídeos populares no YouTube")
st.dataframe(df_youtube)

# Gráfico (exemplo)
st.subheader("🎵 Popularidade das músicas")
st.bar_chart(df_spotify.set_index("nome")["popularidade"])
