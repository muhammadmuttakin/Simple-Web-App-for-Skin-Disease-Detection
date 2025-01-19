# 🚀 Deteksi Penyakit Kulit Menggunakan Deep Learning yang Diintegrasikan ke Aplikasi Web Sederhana 🌐
<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white&style=for-the-badge)
![Keras](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=white&style=for-the-badge)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white&style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-black?logo=flask&logoColor=white&style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white&style=for-the-badge)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn&logoColor=white&style=for-the-badge)

</div>
## 📝 Tentang Proyek
Saya senang membagikan proyek terbaru ini, di mana saya mengembangkan model **deep learning** untuk mendeteksi penyakit kulit dan mengintegrasikannya ke dalam aplikasi web sederhana. Proyek ini memanfaatkan teknologi mutakhir untuk meningkatkan aksesibilitas dan akurasi dalam diagnosis kondisi kulit.

---

## 🔍 Sorotan Proyek

### 🔧 Alat & Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python
- **Framework Deep Learning**: TensorFlow, Keras
- **Pendukung Analisis**: Scikit-learn
- **Back-end Web**: Flask

### 📸 Model Deep Learning
- Menggunakan **Pretrained MobileNetV2**, yang telah diadaptasi untuk klasifikasi penyakit kulit.

### 📊 Hasil
- Model ini mencapai akurasi **93%** dalam mendeteksi penyakit kulit.

### 📂 Dataset
Dataset yang digunakan sebagian besar terdiri dari foto close-up kondisi kulit. Untuk hasil yang lebih optimal, pengembangan dataset dengan gambar yang lebih beragam dan realistis sangat diperlukan.

---

## 💡 Langkah Pengembangan

1. **Preprocessing Dataset**: 
   - Augmentasi gambar untuk meningkatkan variasi data.
   - Normalisasi data untuk mempercepat proses pelatihan.

2. **Training Model**:
   - Fine-tuning pretrained MobileNetV2 untuk tugas klasifikasi multi-kelas.
   - Evaluasi menggunakan metrik akurasi dan confusion matrix.

3. **Integrasi ke Aplikasi Web**:
   - Membuat API prediksi menggunakan Flask.
   - Desain antarmuka web sederhana dengan HTML dan CSS untuk mengunggah gambar dan melihat hasil prediksi.

4. **Testing**:
   - Uji coba pada dataset baru untuk mengukur performa dalam skenario dunia nyata.

---

## 📦 Instalasi dan Penggunaan

### 1. Clone Repository
```bash
$ git clone https://github.com/username/skin-disease-detector.git
$ cd skin-disease-detector
```

### 2. Instalasi Dependencies
```bash
$ pip install -r requirements.txt
```

### 3. Jalankan Aplikasi Web
```bash
$ python app.py
```
Buka browser Anda dan akses: `http://localhost:5000`

---

## 📸 Screenshot
![Screenshot Aplikasi](https://via.placeholder.com/800x400.png?text=Screenshot+Aplikasi+Deteksi+Penyakit+Kulit)

---

## 🌟 Rencana Pengembangan

- **Peningkatan Dataset**: Menambahkan data dengan latar belakang yang lebih realistis dan gambar dari berbagai kondisi pencahayaan.
- **Optimasi Model**: Mengeksplorasi model yang lebih ringan untuk aplikasi mobile.
- **Pengembangan Front-end**: Membuat antarmuka pengguna yang lebih interaktif dan estetis menggunakan React atau Vue.js.

---

## 🤝 Kontribusi
Kontribusi sangat diterima! Jika Anda memiliki ide, saran, atau ingin berkontribusi pada proyek ini, silakan buka _issue_ atau kirimkan _pull request_.

---

## 📄 Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---


---

> **Catatan**: Proyek ini adalah untuk keperluan edukasi dan pengembangan. Jangan gunakan untuk diagnosis medis tanpa konsultasi dokter profesional.
