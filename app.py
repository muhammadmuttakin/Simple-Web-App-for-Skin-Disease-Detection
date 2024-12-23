import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

# Definisikan kelas DepthwiseConv2D kustom
from tensorflow.keras.layers import DepthwiseConv2D

class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, groups=1, **kwargs):
        # Hapus 'groups' dari kwargs jika ada
        if 'groups' in kwargs:
            del kwargs['groups']
        super().__init__(**kwargs)

# Inisialisasi Flask
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')  # Gunakan environment variable jika memungkinkan

# Konfigurasi folder upload dan ekstensi file yang diizinkan
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Path model dan target size
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'model_default.h5')
TARGET_SIZE = (224, 224)  # Sesuaikan dengan ukuran input model Anda

print(f"TensorFlow version: {tf.__version__}")

# Memuat model dengan custom_objects
try:
    model = load_model(MODEL_PATH, custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D})
    print("Model berhasil dimuat.")
except Exception as e:
    print(f"Error saat memuat model: {e}")
    exit(1)  # Hentikan aplikasi jika model gagal dimuat

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
        img_array = img_to_array(img)
        img_array = img_array / 255.0  # Normalisasi
        img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch
        return img_array
    except Exception as e:
        print(f"Error saat memproses gambar: {e}")
        return None

# Route utama untuk upload dan prediksi
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Periksa apakah ada file dalam request
        if 'file' not in request.files:
            print("Tidak ada file dalam request.")
            return redirect(request.url)
        file = request.files['file']
        # Jika tidak memilih file
        if file.filename == '':
            print("Tidak ada file yang dipilih.")
            return redirect(request.url)
        # Jika file valid
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                file.save(filepath)
                print(f"File disimpan di: {filepath}")
            except Exception as e:
                print(f"Error saat menyimpan file: {e}")
                return redirect(request.url)

            # Siapkan gambar dan lakukan prediksi
            img = load_and_preprocess_image(filepath, TARGET_SIZE)
            if img is not None:
                try:
                    prediction = model.predict(img)
                    predicted_class = np.argmax(prediction, axis=1)[0]
                    confidence = np.max(prediction, axis=1)[0] * 100
                    predicted_label = labels.get(predicted_class, 'Unknown')

                    print(f"Prediksi: {predicted_label} dengan confidence: {confidence}%")

                    return render_template('result.html', filename=filename, prediction=predicted_label, confidence=confidence)
                except Exception as e:
                    print(f"Error saat melakukan prediksi: {e}")
                    return redirect(request.url)
            else:
                print("Gagal memproses gambar.")
                return redirect(request.url)
    return render_template('index.html')

# Route untuk menampilkan gambar hasil upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

# Jalankan aplikasi
if __name__ == '__main__':
    # Pastikan folder uploads ada
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        print(f"Folder {UPLOAD_FOLDER} dibuat.")
    app.run(debug=True)
