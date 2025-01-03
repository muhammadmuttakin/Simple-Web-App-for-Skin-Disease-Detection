import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

# Inisialisasi Flask
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# Konfigurasi folder upload dan ekstensi file yang diizinkan
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Batas maksimal upload file: 16MB

# Path model dan target size
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'model_default.h5')
TARGET_SIZE = (224, 224)

# Label kelas
labels = {
    0: 'chickenpox',
    1: 'cowpox',
    2: 'healthy',
    3: 'measles',
    4: 'monkeypox',
    5: 'smallpox'
}

# Fungsi untuk memeriksa ekstensi file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Fungsi untuk memuat dan memproses gambar
def load_and_preprocess_image(image_path, target_size):
    try:
        img = load_img(image_path, target_size=target_size)
        img_array = img_to_array(img) / 255.0  # Normalisasi
        img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch
        return img_array
    except Exception as e:
        print(f"Error saat memproses gambar: {e}")
        return None

# Muat model TensorFlow sekali saat aplikasi dimulai
try:
    model = load_model(MODEL_PATH)
    print("Model berhasil dimuat.")
except Exception as e:
    print(f"Error saat memuat model: {e}")
    model = None

# Route utama untuk upload, prediksi, dan menampilkan hasil
@app.route('/', methods=['GET', 'POST'])
def deteksi():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("Tidak ada file dalam request.")
            return render_template('index.html', error="Tidak ada file yang diunggah.")

        file = request.files['file']
        if file.filename == '':
            print("Tidak ada file yang dipilih.")
            return render_template('deteksi.html', error="Tidak ada file yang dipilih.")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                file.save(filepath)
                print(f"File disimpan di: {filepath}")
            except Exception as e:
                print(f"Error saat menyimpan file: {e}")
                return render_template('deteksi.html', error="Gagal menyimpan file.")

            img = load_and_preprocess_image(filepath, TARGET_SIZE)
            if img is not None:
                try:
                    prediction = model.predict(img)
                    predicted_class = np.argmax(prediction, axis=1)[0]
                    confidence = np.max(prediction, axis=1)[0] * 100
                    predicted_label = labels.get(predicted_class, 'Unknown')

                    print(f"Prediksi: {predicted_label} dengan confidence: {confidence}%")

                    return render_template('deteksi.html', 
                                           filename=filename, 
                                           prediction=predicted_label, 
                                           confidence=confidence)
                except Exception as e:
                    print(f"Error saat melakukan prediksi: {e}")
                    return render_template('deteksi.html', error="Gagal melakukan prediksi.")
            else:
                return render_template('deteksi.html', error="Gagal memproses gambar.")
    return render_template('deteksi.html')

# Route untuk menampilkan gambar hasil upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

# Jalankan aplikasi
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
