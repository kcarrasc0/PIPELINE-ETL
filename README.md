# Projeto ETL – Análise de Tendências Musicais e Audiovisuais (Spotify + YouTube)

Este projeto coleta dados de músicas populares no Spotify e vídeos populares no YouTube, organiza esses dados em tabelas e visualiza os resultados em um painel interativo criado com Streamlit.

## 👨‍💻 Equipe
- Erick Carrasco (Kcarrasco)
- Lucas Vicente (Luquinhasaf)
- Dandara Gouveia (Dara8)

## 📦 Estrutura

etl_musica_video/ ├── extracao_spotify.py → coleta dados do Spotify ├── extracao_youtube.py → coleta dados do YouTube ├── spotify_data.csv → dados extraídos do Spotify ├── youtube_data.csv → dados extraídos do YouTube ├── painel.py → painel visual interativo com Streamlit ├── README.md → explicação do projeto └── requirements.txt → bibliotecas necessárias


## 🚀 Como executar

1. Clone o repositório ou extraia os arquivos zipados.
2. Instale as bibliotecas:
   ```bash
   pip install -r requirements.txt
   
python extracao_spotify.py
python extracao_youtube.py

streamlit run painel.py

🔑 Pré-requisitos

Chave de API do Spotify (https://developer.spotify.com/dashboard)
Chave de API do YouTube (https://console.cloud.google.com)


✅ Resultado Esperado

Tabelas com músicas e vídeos populares
Gráfico com a popularidade das músicas no painel Streamlit
Visualização fácil de comparar os conteúdos das duas plataformas


📚 Tecnologias

Python
Spotipy
Google API Client
Pandas
Streamlit


---

## 📄 `requirements.txt`

```txt
spotipy
google-api-python-client
pandas
streamlit
