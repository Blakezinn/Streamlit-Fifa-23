from tarfile import data_filter

import pandas as pd
import streamlit as st
from pandas.conftest import all_numeric_reductions
from pandas.io.sas.sas_constants import col_count_p1_multiplier
from rich.jupyter import display
import time
st.set_page_config(
    layout='wide',
    page_title="spotify songs"
)

@st.cache_data
def load_data():
    df = pd.read_csv('01 Spotify.csv')
    time.sleep(5)
    return df
df = load_data()
st.session_state["df_spotify"] = df


df.set_index('Track', inplace= True)

artists = df['Artist'].value_counts().index
artist = st.sidebar.selectbox('Artista', artists)
df_filter = df[df['Artist'] == artist]

album_lista = df_filter['Album'].value_counts().index
album = st.selectbox('Album', album_lista)

df_filter2 = df[df['Album'] == album]

#display = st.checkbox("Display!")
#if display:

col1, col2 = st.columns([0.7, 0.3])

col1.bar_chart(df_filter2['Stream'])
col2.line_chart(df_filter2['Danceability'])


st.write(artist)
st.sidebar.button('teste')






