<<<<<<< HEAD
### Analisis Efisiensi Pembelajaran Hibrida

Aplikasi analitik berbasis Streamlit untuk memodelkan hubungan antara jam pembelajaran tatap muka dan daring terhadap nilai akhir mahasiswa menggunakan Regresi Linier dan Aljabar Linier.

---

#### Struktur Repositori

```text
project/
├── app.py                      # Halaman utama aplikasi
├── pages/                      # Antarmuka multi halaman
│   ├── 1_eksplorasi_data.py
│   ├── 2_model_regresi.py
│   ├── 3_aljabar_linier.py
│   └── 4_prediksi.py
├── src/                        # Lapisan logika dan matematika
│   ├── data_processing.py
│   ├── linear_algebra.py
│   ├── modeling.py
│   └── visualization.py
├── tests/                      # Unit testing
│   ├── test_data_processing.py
│   └── test_linear_algebra.py
├── data/                       # Tempat penyimpanan dataset sampel
├── .devcontainer/              # Konfigurasi container development
├── .streamlit/                 # Konfigurasi tema antarmuka
├── requirements.txt            # Dependensi utama aplikasi
└── requirements-dev.txt        # Dependensi khusus untuk pengujian

```

---

#### Cara Menjalankan Aplikasi

Pastikan perangkat Anda menggunakan Python 3.11 atau yang lebih baru.

```bash
# Clone dan navigate
git clone <url>
cd project

# Setup environment
python -m venv venv
source venv/bin/activate

# Menginstal semua dependensi
pip install -r requirements.txt

# Menjalankan server aplikasi
streamlit run app.py

```

Aplikasi dapat diakses melalui peramban web pada alamat `http://192.168.0.3:8501`.

---

#### Menjalankan Pengujian

Untuk memverifikasi keakuratan perhitungan aljabar linier dan logika validasi data, jalankan rangkaian unit tests:

```bash
# Menginstal pustaka untuk pengujian
pip install -r requirements-dev.txt

# Mengeksekusi pengujian
pytest
```
=======
# Analytic Student Data
>>>>>>> upstream/main
