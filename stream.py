import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import HeatMap

df_covid_brasil = pd.read_csv('brazil_cities_coordinates.csv')

df_heat_map = df_covid_brasil[['lat', 'long']]
df_heat_map = df_heat_map.replace(to_replace=r',', value='.', regex=True)

st.title('Mapa de calor Covid Brasil')


zoonMap = st.sidebar.slider(label='Zoom do mapa', max_value=10, min_value=5)

latitude = st.sidebar.number_input(label='Insira a latitude desejada')
longitude = st.sidebar.number_input(label='Insira a longitude desejada')

crime_map = folium.Map(location=[-2.5100598, -44.2511041],
                       zoom_start=zoonMap)

data_heatmap = df_heat_map[['lat', 'long']]
data_heatmap = df_heat_map.dropna(axis=0, subset=['lat', 'long'])
data_heatmap = [[row['lat'], row['long']]
                for index, row in data_heatmap.iterrows()]
HeatMap(data_heatmap, radius=15).add_to(crime_map)

crime_map

folium_static(crime_map)

df_covid_saoluis_cases = pd.read_csv('covid19_ma.csv')

optionState = st.sidebar.selectbox(
    'Selecione o estado que seja ver na tabela', options=['MA'])

st.dataframe(
    df_covid_saoluis_cases[df_covid_saoluis_cases['city'] == 'São Luís'])
