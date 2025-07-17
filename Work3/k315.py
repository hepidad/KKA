import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

st.title("📊 Analisis Penjualan Mobil Listrik - Klasterisasi Hari")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data_penjualan_mobil_listrik.csv")

df = load_data()

# Tampilkan data awal
st.subheader("📁 Dataset Penjualan")
st.dataframe(df.head(20))

# Pivot data
pivot_df = df.pivot_table(index='Tanggal', columns='Model', values='Jumlah_Terjual', aggfunc='sum').fillna(0).reset_index()

# Pilih jumlah klaster
n_clusters = st.slider("Pilih jumlah klaster", min_value=2, max_value=5, value=3)

# Fitur
features = pivot_df[['Model A', 'Model B', 'Model C', 'Model D']]

# Standarisasi
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# KMeans
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
pivot_df['Cluster'] = kmeans.fit_predict(scaled_features)

# Visualisasi PCA
pca = PCA(n_components=2)
components = pca.fit_transform(scaled_features)

fig, ax = plt.subplots()
scatter = ax.scatter(components[:, 0], components[:, 1], c=pivot_df['Cluster'], cmap='tab10')
ax.set_xlabel("PCA Komponen 1")
ax.set_ylabel("PCA Komponen 2")
ax.set_title("Visualisasi Klaster Hari Berdasarkan Penjualan")
ax.grid(True)

st.pyplot(fig)

# Tampilkan data hasil klaster
st.subheader("📌 Data Setelah Klasterisasi")
st.dataframe(pivot_df[['Tanggal', 'Model A', 'Model B', 'Model C', 'Model D', 'Cluster']])

