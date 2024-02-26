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

def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='Tanggal').agg({
        'Total_Sewa': 'sum'
    }).reset_index()
    return daily_rent_df

def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='Tanggal').agg({'Non-member': 'sum'}).reset_index()
    return daily_casual_rent_df

def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='Tanggal').agg({
        'Member': 'sum'
    }).reset_index()
    return daily_registered_rent_df
    
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='Musim')[['Member', 'Non-member']].sum().reset_index()
    return season_rent_df

def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='Bulan').agg({'Total_Sewa': 'sum'})
    order_bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 
                'September', 'Oktober', 'November', 'Desember'
    ]
    monthly_rent_df = monthly_rent_df.reindex(order_bulan, fill_value=0)
    return monthly_rent_df

def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='Hari').agg({
        'Total_Sewa': 'sum'
    }).reset_index()
    return weekday_rent_df
    
def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='Cuaca').agg({
        'Total_Sewa': 'sum'
    })
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
daily_rent_df = create_daily_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)


# Membuat Dashboard secara lengkap

# Membuat judul
st.header('Final Project Data Analytics - Bike Sharing Dataset')

# Membuat jumlah penyewaan bulanan
st.subheader('Monthly Rentals')
fig, ax = plt.subplots(figsize=(24, 8))
ax.plot(
    monthly_rent_df.index,
    monthly_rent_df['Total_Sewa'],
    marker='o', 
    linewidth=2,
    color='tab:blue'
)

for index, row in enumerate(monthly_rent_df['Total_Sewa']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

# Membuah jumlah penyewaan berdasarkan kondisi cuaca
st.subheader('Weatherly Rentals')
order_cuaca = ['Salju Ringan/Hujan', 'Berkabut/Berawan', 'Cerah/Sebagian Berawan']
df['Cuaca'] = pd.Categorical(df['Cuaca'], categories=order_cuaca, ordered=True)
df = df.sort_values('Cuaca')
order_cuaca = df.groupby('Cuaca')[['Member', 'Non-member']].sum().reset_index()
fig, ax = plt.subplots(figsize=(16, 8))

colors=["tab:blue", "tab:orange", "tab:green"]

sns.barplot(
    x=weather_rent_df.index,
    y=weather_rent_df['Total_Sewa'],
    palette=colors,
    ax=ax
)

for index, row in enumerate(weather_rent_df['Total_Sewa']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

# Membuat jumlah penyewaan berdasarkan musim
st.subheader('Seasonly Rentals')
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
