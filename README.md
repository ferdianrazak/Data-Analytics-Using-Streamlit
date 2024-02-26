# Final Project Data Analytics - Bike Sharing Dataset

## Analisis Data dan Hasil dengan Jupyter Notebook

Ini merupakan proyek final yang saya kerjakan untuk kursus "Belajar Analisis Data dengan Python" di Dicoding, di mana saya bertugas untuk menganalisis dan memvisualisasikan data dari dataset bike sharing. Saya telah mendokumentasikan proses analisis saya, mulai dari Data Wrangling hingga Visualisasi Data, dalam sebuah notebook. Saya juga telah mengembangkan sebuah dashboard menggunakan Streamlit, yang dapat Anda akses melalui tautan di sidebar kanan atau melalui link yang disediakan di sini.

Untuk detail tambahan seperti konteks dataset, detail karakteristik, struktur file, dan informasi lainnya, silakan rujuk ke file Readme. Saya tidak akan membahasnya secara detail di sini.

### Pertanyaan Bisnis
1. Bagaimana tren jumlah penggunaan sepeda pada tahun 2011 dan 2012?
2. Bagaimana kondisi cuaca mempengaruhi frekuensi penggunaan sepeda?
3. Musim apa yang memiliki jumlah penggunaan sepeda sepeda tertinggi?

### Hasil Analisis
1. Dari analisis visualisasi data pada tahun 2011 dan 2012, terlihat adanya perbedaan signifikan dalam puncak dan dasar penggunaan sepeda pada kedua tahun, dimana puncak penggunaan pada tahun 2011 terjadi di bulan Juni dan terendah di Januari, sementara pada tahun 2012, puncaknya bergeser ke bulan September dengan dasar yang tetap di bulan Januari. Jumlah total penyewaan sepeda pada tahun 2012 secara keseluruhan menunjukkan peningkatan dibandingkan dengan tahun 2011, mengikuti tren dan musiman yang sama di mana jumlah penyewaan meningkat di pertengahan tahun dan menurun di awal dan akhir tahun, terlepas dari kategori pelanggan, baik anggota maupun bukan anggota.

2. Analisis hubungan antara suhu dan jumlah pengguna terdaftar penyewaan sepeda menunjukkan bahwa cuaca berpengaruh signifikan terhadap minat bersepeda, dengan peningkatan suhu yang cenderung meningkatkan jumlah pengguna. Kesimpulan dari analisis ini mengungkapkan bahwa ada korelasi positif antara kondisi cuaca yang cerah atau sedikit mendung dengan jumlah penyewaan sepeda yang tinggi, di mana kuartil ketiga (Q3) lebih dari 6000 dan kuartil pertama (Q1) kurang dari 4000, serta median hampir 5000. Cuaca berkabut atau mendung menempati posisi kedua dengan Q3 di atas 5000, Q1 di bawah 3000, dan median lebih dari 4000. Sementara itu, kondisi cuaca seperti sedikit bersalju atau hujan kurang disukai dengan Q3 di atas 2000, Q1 di bawah 1000, dan median lebih dari 1000. Tidak ada data untuk kondisi cuaca ekstrem seperti badai besar karena tidak memungkinkan untuk bersepeda dalam kondisi tersebut. Selanjutnya, dikonfirmasi bahwa cuaca cerah sangat berhubungan dengan rata-rata penyewaan sepeda yang lebih tinggi, menegaskan bahwa kondisi cuaca yang mendukung aktivitas luar ruangan seperti bersepeda sangat dipengaruhi oleh kecerahan dan keadaan cuaca yang baik, yang meningkatkan minat dan motivasi pengguna untuk menyewa sepeda dan menikmati kegiatan di luar rumah di bawah sinar matahari. Ini menunjukkan bahwa faktor cuaca memainkan peran penting dalam keputusan penyewaan sepeda, dengan preferensi yang jelas terhadap cuaca cerah dan kondisi yang lebih nyaman untuk bersepeda.

3. Dalam analisis visualisasi terakhir, terungkap sebuah kejutan bahwa musim semi, bukan musim dingin, menempati posisi terendah dalam hal jumlah penyewaan sepeda. Faktor-faktor seperti kondisi cuaca, suhu udara, hari kerja versus hari libur dapat mempengaruhi dinamika ini. Sebaliknya, musim gugur muncul sebagai musim dengan jumlah penyewaan sepeda tertinggi, mencapai lebih dari 800.000 penyewaan. Meskipun analisis sebelumnya menunjukkan musim panas sebagai periode dengan aktivitas penyewaan sepeda yang paling tinggi, diikuti oleh penurunan selama musim dingin, data terbaru ini menawarkan perspektif yang berbeda, menekankan bahwa musim semi—bukan musim dingin—adalah waktu dengan minat penyewaan sepeda yang paling rendah, sementara musim gugur mendominasi sebagai periode dengan aktivitas penyewaan sepeda yang paling tinggi. Ini menyoroti pentingnya mempertimbangkan berbagai faktor lingkungan dan sosial dalam menganalisis pola penyewaan sepeda.

### Struktur file
submission
├── dashboard
│   ├── dashboard.py
│   └── day.csv
├── data
│   ├── Readme.txt
│   ├── day.csv
|   └── hour.csv
├── screenshots
|   ├── Screenshots (91).png
|   ├── Screenshots (92).png
|   ├── Screenshots (93).png
|   └── Screenshots (94).png
├── README.md
├── notebook.ipynb
└── requirements.txt

## Streamlit Dashboard
Lihat dashboard di streamlit di link: https://capital-bikeshare-alfikri.streamlit.app/ 
