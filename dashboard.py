import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Load data with caching to improve performance
@st.cache
def load_data(url):
    data = pd.read_csv(url)
    data['Tanggal'] = pd.to_datetime(data['Tanggal'])
    return data

df = load_data("https://raw.githubusercontent.com/ferdianrazak/dashboard/main/dashboard/main_data.csv")

# Sidebar details
st.sidebar.title("Peneliti:")
st.sidebar.markdown("**• Nama: Ferdian Razak**")
st.sidebar.markdown("**• Email: [ferdianrazak77@gmail.com](mailto:ferdianrazak77@gmail.com)**")
st.sidebar.markdown("**• Dicoding: [Profile](https://www.dicoding.com/users/ferdianrazak/)**")

# Define functions to process data
def season_data(df):
    order_season = ['Semi', 'Dingin', 'Panas', 'Gugur']
    df['Musim'] = pd.Categorical(df['Musim'], categories=order_season, ordered=True)
    return df.groupby('Musim')[['Member', 'Non-member']].sum().reset_index()

def monthly_data(df, year):
    df_year = df[df['Tahun'] == year]
    order_month = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
                   'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    monthly_df = df_year.groupby('Bulan').agg({'Total_Sewa': 'sum'})
    return monthly_df.reindex(order_month, fill_value=0)

def weather_data(df):
    order_weather = ['Salju Ringan/Hujan', 'Berkabut/Berawan', 'Cerah/Sebagian Berawan']
    df['Cuaca'] = pd.Categorical(df['Cuaca'], categories=order_weather, ordered=True)
    return df.groupby('Cuaca')[['Member', 'Non-member']].sum().reset_index()

# User inputs for the date range
min_date = df['Tanggal'].min().date()
max_date = df['Tanggal'].max().date()
start_date, end_date = st.date_input("Waktu Data", [min_date, max_date], min_value=min_date, max_value=max_date)

filtered_df = df[(df['Tanggal'].dt.date >= start_date) & (df['Tanggal'].dt.date <= end_date)]

# Dataframes for different analyses
season_df = season_data(filtered_df)
weather_df = weather_data(filtered_df)
monthly_2011_df = monthly_data(df, 2011)
monthly_2012_df = monthly_data(df, 2012)

# Plotting
st.header('Final Project Data Analytics - Bike Sharing Dataset')

# Monthly trends by year
st.subheader('Tren jumlah pengguna per bulan pada 2011 dan 2012')
fig = px.line(x=monthly_2011_df.index, y=monthly_2011_df['Total_Sewa'], labels={'x': 'Month', 'y': 'Total Rentals'},
              title='Monthly Trends for 2011')
fig.add_scatter(x=monthly_2012_df.index, y=monthly_2012_df['Total_Sewa'], name='2012')
st.plotly_chart(fig)

# Rentals by weather condition
st.subheader('Jumlah sewa berkaitan dengan cuaca')
fig = px.bar(weather_df, x='Cuaca', y=['Member', 'Non-member'],
             title='Rentals by Weather Condition', barmode='group')
st.plotly_chart(fig)

# Rentals by season
st.subheader('Jumlah sewa berkaitan dengan musim')
fig = px.bar(season_df, x='Musim', y=['Member', 'Non-member'],
             title='Rentals by Season', barmode='group')
st.plotly_chart(fig)

# Copyright notice
st.caption('Copyright (c) Ferdian Razak 2024')
