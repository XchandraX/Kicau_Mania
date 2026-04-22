# 🐱 Kicau Mania Split Screen

Proyek interaktif menggunakan Python yang mendeteksi gerakan tangan ke mulut menggunakan **MediaPipe** untuk memicu video "Kicau Mania" dan suara latar secara otomatis. Program ini menggunakan sistem *split screen* yang menampilkan kamera pengguna di satu sisi dan video kucing di sisi lainnya.

## ✨ Fitur
- **Deteksi Landmark Wajah & Tangan**: Menggunakan MediaPipe Holistic untuk akurasi tinggi.
- **Interaksi Real-time**: Video dan audio otomatis bermain saat tangan mendekati mulut.
- **Split Screen View**: Tampilan berdampingan antara kamera lokal dan video target.
- **Visual Debug**: Menampilkan indikator jarak antara tangan dan mulut pada layar.

## 🛠️ Persyaratan Sistem
Pastikan kamu sudah menginstal Python di komputermu. Library utama yang digunakan adalah:
- `opencv-python` (untuk pengolahan video)
- `mediapipe` (untuk AI tracking)
- `pygame` (untuk memutar audio)
- `numpy` (untuk manipulasi array layar)

## 🚀 Cara Menjalankan

### 1. Persiapan File
Pastikan semua file berikut berada dalam satu folder yang sama:
- `kicau_mania.py` (Kode utama)
- `kicau.mp3` (File audio)
- `kucing_kicau.mp4` (File video)
- `install.py` (Script installer library)

### 2. Instalasi Library
Jalankan script installer untuk mengunduh semua kebutuhan:
```bash
python install.py
```
Atau jika kamu ingin menggunakan requirements.txt:
```bash
pip install -r requirements.txt
```
### 3. Menjalankan Program
Jalankan script utama dengan perintah:
```bash
python kicau_mania.py
```

🎮 Cara Pakai
telah membuka kamera, kamu akan melihat tampilan kamera di kiri dan layar hitam di kanan.
1. Dekatkan telapak tangan (ujung jari telunjuk) ke arah mulutmu.
2. Jika jarak cukup dekat (di bawah threshold), video kucing akan muncul di layar kanan dan suara "Kicau Mania" akan mulai berputar.
3. Jauhkan tangan untuk menghentikan video dan suara.
4. Tekan tombol 'q' pada keyboard untuk keluar dari program.

📂 Struktur File
dengan penjelasan singkat:
| File | Fungsi |
|---|---|
kicau_mania.py | Logika deteksi AI dan pengaturan tampilan split screen.
install.py | Script otomatis untuk instalasi dependensi.
requirements.txt | Daftar library yang dibutuhkan.
.gitignore | Daftar file yang diabaikan oleh Git (cache, venv, dll).
note: Pastikan pencahayaan ruangan cukup agar MediaPipe dapat mendeteksi titik wajah dan tangan dengan optimal.