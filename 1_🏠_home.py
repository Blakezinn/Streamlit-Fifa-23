import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Copiado por [Max Paulo](https://github.com/blakezinn)")



btn = st.button("Acesso os dados no Kaggle")
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    '''
O Conjunto de Dados dos Jogadores de Futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais. O conjunto de dados contém uma ampla gama de atributos, incluindo demografia dos jogadores, características físicas, estatísticas de jogo, detalhes de contrato e afiliações a clubes.

Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois permite o estudo de atributos dos jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento de jogadores ao longo do tempo.
'''
)