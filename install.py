import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

packages = ["opencv-python", "mediapipe", "pygame", "numpy"]

print("Sedang menginstal library yang dibutuhkan...")
for p in packages:
    try:
        install(p)
        print(f"Berhasil menginstal {p}")
    except Exception as e:
        print(f"Gagal menginstal {p}: {e}")

print("\nSemua beres! Sekarang kamu bisa jalankan kode Kicau Mania-nya.")
