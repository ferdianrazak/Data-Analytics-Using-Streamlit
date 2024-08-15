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

# Custom CSS to improve the look and feel of the dashboard
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    font-weight: bold !important;
}
.metric-box {
    padding: 10px;
    border-radius: 5px;
    border: 2px solid #eee;
    margin: 10px;
}
</style>
""", unsafe_allow_html=True)

# Metric Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Accounts Receivable", "$6,621,280", "1.8%")
col2.metric("Total Accounts Payable", "$1,630,270", "-0.9%")
col3.metric("Equity Ratio", "75.38%", "0.5%")
col4.metric("Debt Equity", "1.10%", "-0.1%")

# Data Analysis Sections
with st.expander("Financial Ratios Analysis"):
    st.markdown('<p class="big-font">Financial Ratios</p>', unsafe_allow_html=True)
    # Add plots and analysis

with st.expander("Revenue and Profit Summary"):
    st.markdown('<p class="big-font">Monthly Revenue and Profit</p>', unsafe_allow_html=True)
    # Plot for revenue and profits
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df, x='Month', y='Revenue', ax=ax, label='Revenue')
    sns.lineplot(data=df, x='Month', y='Profit', ax=ax, label='Profit')
    st.pyplot(fig)

# Interactive Plots with Plotly
st.subheader('Interactive Analysis of Data')
fig = px.bar(df, x='Month', y='Profit', color='Year', title='Profit by Month and Year')
st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown('<p class="big-font">Dashboard by Ferdian Razak</p>', unsafe_allow_html=True)
