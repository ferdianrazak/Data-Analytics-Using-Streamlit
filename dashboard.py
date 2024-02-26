import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("dashboard/main_data.csv")
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Ferdian Razak**")
st.sidebar.markdown(
    "**• Email: [ferdianrazak77@gmail.com](ferdianrazak77@gmail.com)**")
st.sidebar.markdown(
    "**• Dicoding: [ferdianrazak](https://www.dicoding.com/users/ferdianrazak/)**")

def create_season_rent_df(df):
    season_rent_df = df.groupby(by='Musim')[['Member', 'Non-member']].sum().reset_index()

    return season_rent_df

def create_monthly_rent_df(df, year):
    df_year = df[df['Tahun'] == year]
    monthly_rent_df = df_year.groupby(by='Bulan').agg({'Total_Sewa': 'sum'})
    order_bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 
                'September', 'Oktober', 'November', 'Desember'
    ]
    monthly_rent_df = monthly_rent_df.reindex(order_bulan, fill_value=0)
    return monthly_rent_df
    
def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='Cuaca')[['Member', 'Non-member']].sum().reset_index()
    return weather_rent_df
   
# Membuat komponen filter
min_date = pd.to_datetime(df ['Tanggal']).dt.date.min()
max_date = pd.to_datetime(df ['Tanggal']).dt.date.max()

start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

main_df = df [(df['Tanggal'] >= str(start_date)) & (df['Tanggal'] <= str(end_date))]

# Menyiapkan berbagai dataframe
season_rent_df = create_season_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)
monthly_rent_df_2011 = create_monthly_rent_df(df, 2011)
monthly_rent_df_2012 = create_monthly_rent_df(df, 2012)

# Membuat Dashboard secara lengkap
st.header('Final Project Data Analytics - Bike Sharing Dataset')
st.subheader('Tren jumlah pengguna per bulan pada 2011 dan 2012')
fig, ax = plt.subplots(figsize=(24, 8))
ax.plot(
    monthly_rent_df_2011.index,
    monthly_rent_df_2011['Total_Sewa'],
    marker='o',
    linewidth=2,
    color='tab:blue',
    label='2011'  # Label for the legend
)

ax.plot(
    monthly_rent_df_2012.index,
    monthly_rent_df_2012['Total_Sewa'],
    marker='o',
    linewidth=2,
    color='tab:orange',
    label='2012'  # Label for the legend
)

for index, value in enumerate(monthly_rent_df_2011['Total_Sewa']):
    ax.text(index, value, str(value), ha='center', va='bottom', fontsize=12)
    ax.text(index, value, str(value), ha='center', va='bottom', fontsize=12)
ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
ax.legend()
st.pyplot(fig)

# Membuah jumlah penyewaan berdasarkan kondisi cuaca
st.subheader('Jumlah sewa berkaitan dengan cuaca')
fig, ax = plt.subplots(figsize=(16, 8))

sns.barplot(
    x='Cuaca',
    y='Member',
    data=weather_rent_df,
    label='Member',
    ax=ax
)

sns.barplot(
    x='Cuaca',
    y='Non-member',
    data=weather_rent_df,
    label='Non-member',
    ax=ax
)

for index, row in weather_rent_df.iterrows():
    ax.text(index, row['Member'], str(row['Member']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['Non-member'], str(row['Non-member']), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20, rotation=0)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)

# Membuat jumlah penyewaan berdasarkan musim
st.subheader('Jumlah sewa berkaitan dengan musim')
fig, ax = plt.subplots(figsize=(16, 8))

sns.barplot(
    x='Musim',
    y='Member',
    data=season_rent_df,
    label='Member',
    ax=ax
)

sns.barplot(
    x='Musim',
    y='Non-member',
    data=season_rent_df,
    label='Non-member',
    ax=ax
)

for index, row in season_rent_df.iterrows():
    ax.text(index, row['Member'], str(row['Member']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['Non-member'], str(row['Non-member']), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20, rotation=0)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)

st.caption('Copyright (c) Ferdian Razak 2024')
