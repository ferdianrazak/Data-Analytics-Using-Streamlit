import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("../dashboard/main_data.csv")

st.sidebar.title("Peneliti:")
st.sidebar.markdown("**• Nama: Ferdian Razak**")
st.sidebar.markdown(
    "**• Email: [ferdianrazak77@gmail.com](ferdianrazak77@gmail.com)**")
st.sidebar.markdown(
    "**• Dicoding: [ferdianrazak](https://www.dicoding.com/users/ferdianrazak/)**")

def def_musim_df(df):
    order_musim = ['Semi', 'Dingin', 'Panas', 'Gugur']
    df['Musim'] = pd.Categorical(df['Musim'], categories=order_musim, ordered=True)
    musim_df = df.groupby(by='Musim')[['Member', 'Non-member']].sum().reset_index()
    return musim_df
def def_bulan_df(df, year):
    df_year = df[df['Tahun'] == year]
    bulan_df = df_year.groupby(by='Bulan').agg({'Total_Sewa': 'sum'})
    order_bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 
                'September', 'Oktober', 'November', 'Desember']
    bulan_df = bulan_df.reindex(order_bulan, fill_value=0)
    return bulan_df
def def_cuaca_df(df):
    order_cuaca = ['Salju Ringan/Hujan', 'Berkabut/Berawan', 'Cerah/Sebagian Berawan']
    df['Cuaca'] = pd.Categorical(df['Cuaca'], categories=order_cuaca, ordered=True)
    cuaca_df = df.groupby(by='Cuaca')[['Member', 'Non-member']].sum().reset_index()
    return cuaca_df
   
min_date = pd.to_datetime(df ['Tanggal']).dt.date.min()
max_date = pd.to_datetime(df ['Tanggal']).dt.date.max()
start_date, end_date = st.date_input(label='Waktu Data', min_value= min_date,
                                     max_value= max_date, value=[min_date, max_date])
main_df = df [(df['Tanggal'] >= str(start_date)) & (df['Tanggal'] <= str(end_date))]

musim_df = def_musim_df(main_df)
cuaca_df = def_cuaca_df(main_df)
bulan_2011_df = def_bulan_df(df, 2011)
bulan_2012_df = def_bulan_df(df, 2012)

st.header('Final Project Data Analytics - Bike Sharing Dataset')
st.subheader('Tren jumlah pengguna per bulan pada 2011 dan 2012')
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(bulan_2011_df.index, bulan_2011_df['Total_Sewa'],
        marker='o', linewidth=4, color='tab:red', label='2011')
ax.plot(bulan_2012_df.index, bulan_2012_df['Total_Sewa'],
        marker='o', linewidth=4, color='tab:green', label='2012')
for index, value in enumerate(bulan_2011_df['Total_Sewa']):
    ax.text(index, value, str(value), ha='center', va='bottom', fontsize=12)
for index, value in enumerate(bulan_2012_df['Total_Sewa']):
    ax.text(index, value, str(value), ha='center', va='bottom', fontsize=12)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)

st.subheader('Jumlah sewa berkaitan dengan cuaca')
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x='Cuaca', y='Member', data=cuaca_df,
            label='Member', ax=ax)
sns.barplot(x='Cuaca', y='Non-member', data=cuaca_df,
            label='Non-member', ax=ax)
for index, row in cuaca_df.iterrows():
    ax.text(index, row['Member'], str(row['Member']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['Non-member'], str(row['Non-member']), ha='center', va='bottom', fontsize=12)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)

st.subheader('Jumlah sewa berkaitan dengan musim')
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x='Musim', y='Member', data=musim_df,
            label='Member', ax=ax)
sns.barplot(x='Musim', y='Non-member', data=musim_df,
            label='Non-member', ax=ax)
for index, row in musim_df.iterrows():
    ax.text(index, row['Member'], str(row['Member']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['Non-member'], str(row['Non-member']), ha='center', va='bottom', fontsize=12)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)

st.caption('Copyright (c) Ferdian Razak 2024')
