import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi tema
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide", page_icon="🚲")

# Load data
df = pd.read_csv('day.csv')
df['weather_desc'] = df['weathersit'].map({1: 'Cerah', 2: 'Berkabut', 3: 'Hujan Ringan', 4: 'Hujan Berat'})
df['is_weekend'] = df['weekday'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')

# Sidebar untuk filter
st.sidebar.title("Filter Data")
weather_filter = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca", 
    options=df['weather_desc'].unique(), 
    default=df['weather_desc'].unique()
)
day_filter = st.sidebar.multiselect(
    "Pilih Tipe Hari", 
    options=['Weekday', 'Weekend'], 
    default=['Weekday', 'Weekend']
)

# Filter dataset berdasarkan pilihan
filtered_df = df[df['weather_desc'].isin(weather_filter) & df['is_weekend'].isin(day_filter)]

# Judul utama
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Analisis Penyewaan Sepeda Berdasarkan Cuaca dan Hari")

# Metrik cepat
col1, col2, col3 = st.columns(3)
col1.metric("Total Penyewaan", f"{int(filtered_df['cnt'].sum()):,}")
col2.metric("Rata-rata Harian", f"{int(filtered_df['cnt'].mean()):,}")
col3.metric("Hari Tercatat", f"{len(filtered_df)}")

# Visualisasi 1: Pengaruh Cuaca
st.subheader("📊 Pengaruh Cuaca terhadap Penyewaan")
weather_group = filtered_df.groupby('weather_desc')['cnt'].mean().reset_index()
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x='weather_desc', y='cnt', data=weather_group, palette='viridis', ax=ax1)
ax1.set_title('Rata-rata Penyewaan Berdasarkan Cuaca', fontsize=14, pad=10)
ax1.set_xlabel('Kondisi Cuaca', fontsize=12)
ax1.set_ylabel('Jumlah Penyewaan (Rata-rata)', fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Visualisasi 2: Weekday vs Weekend
st.subheader("📊 Penyewaan: Weekday vs Weekend")
day_group = filtered_df.groupby('is_weekend')['cnt'].mean().reset_index()
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x='is_weekend', y='cnt', data=day_group, palette='magma', ax=ax2)
ax2.set_title('Rata-rata Penyewaan: Weekday vs Weekend', fontsize=14, pad=10)
ax2.set_xlabel('Tipe Hari', fontsize=12)
ax2.set_ylabel('Jumlah Penyewaan (Rata-rata)', fontsize=12)
st.pyplot(fig2)

# Tabel ringkasan (opsional)
st.subheader("📋 Ringkasan Data")
st.dataframe(weather_group.style.format({"cnt": "{:,.0f}"}))

# Footer
st.markdown("---")
st.markdown("Dibuat dengan ❤️ menggunakan Streamlit | Data: Bike Sharing Dataset")
