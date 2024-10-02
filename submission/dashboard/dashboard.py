import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Aplikasi
st.title("Dashboard Penyewaan Sepeda")

# Mengimpor Data
@st.cache_data
def load_data():
    day_data = pd.read_csv('day.csv')  # Sesuaikan path jika perlu
    hour_data = pd.read_csv('hour.csv')  # Sesuaikan path jika perlu
    return day_data, hour_data

day_data, hour_data = load_data()

# Menentukan Pertanyaan Bisnis
st.header("Pertanyaan Bisnis")
st.markdown("1. Apa pola penggunaan sepeda di hari kerja dan akhir pekan?")
st.markdown("2. Kapan waktu paling sering sepeda digunakan dalam sehari?")

# EDA
st.header("Exploratory Data Analysis (EDA)")
# Pola penggunaan di hari kerja vs akhir pekan
day_data['day_of_week'] = pd.to_datetime(day_data['dteday']).dt.dayofweek
weekend_data = day_data[day_data['day_of_week'] >= 5]
weekday_data = day_data[day_data['day_of_week'] < 5]

# Visualisasi Pola Penggunaan
st.subheader("Pola Penggunaan di Hari Kerja vs Akhir Pekan")
plt.figure(figsize=(10, 6))
sns.barplot(x=['Hari Kerja', 'Akhir Pekan'], y=[weekday_data['cnt'].sum(), weekend_data['cnt'].sum()])
plt.title('Jumlah Penyewaan Sepeda')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(rotation=45)
st.pyplot(plt)

# Visualisasi Penyewaan Berdasarkan Jam
st.subheader("Penyewaan Berdasarkan Jam")
hour_data['hour'] = pd.to_datetime(hour_data['dteday']).dt.hour
hour_counts = hour_data.groupby('hour')['cnt'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=hour_counts, x='hour', y='cnt')
plt.title('Penyewaan Sepeda Berdasarkan Jam')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(rotation=45)
st.pyplot(plt)

# Kesimpulan
st.header("Kesimpulan")
st.markdown("**Pertanyaan 1:** Pola penggunaan sepeda di hari kerja dan akhir pekan menunjukkan bahwa jumlah penyewaan di akhir pekan jauh lebih tinggi. Ini mengindikasikan peluang untuk meningkatkan fasilitas penyewaan pada hari kerja.")
st.markdown("**Pertanyaan 2:** Penyewaan sepeda menunjukkan waktu puncak penggunaan pada jam 7-9 pagi dan 5-7 sore, yang mencerminkan kebiasaan berangkat dan pulang kerja.")

