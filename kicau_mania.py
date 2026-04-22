import os
import cv2
import mediapipe as mp
import math
import pygame
import numpy as np
import warnings

# 1. Setup Awal
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")
pygame.mixer.init()

try:
    suara_kicau = pygame.mixer.Sound("kicau.mp3")
except:
    suara_kicau = None

mp_holistic = mp.solutions.holistic
cap = cv2.VideoCapture(0)
cat_video = cv2.VideoCapture('kucing_kicau.mp4')

suara_sedang_main = False
threshold_jarak = 0.1 

print("Program Berjalan... Tekan 'q' untuk keluar.")

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(rgb_frame)
        
        tangan_di_mulut = False
        jarak_terdekat = 1.0 # Logic dari kode sebelumnya

        if results.face_landmarks:
            # Titik mulut
            m_x, m_y = results.face_landmarks.landmark[13].x, results.face_landmarks.landmark[13].y
            
            # Cek tangan kanan & kiri (Logic dari kode sebelumnya)
            daftar_tangan = []
            if results.right_hand_landmarks: daftar_tangan.append(results.right_hand_landmarks)
            if results.left_hand_landmarks: daftar_tangan.append(results.left_hand_landmarks)

            for tgn in daftar_tangan:
                j_x, j_y = tgn.landmark[8].x, tgn.landmark[8].y
                jarak = math.hypot(m_x - j_x, m_y - j_y)
                
                if jarak < jarak_terdekat:
                    jarak_terdekat = jarak
                if jarak < threshold_jarak:
                    tangan_di_mulut = True

            # Info jarak di layar kamera (Debug visual)
            warna_teks = (0, 255, 0) if tangan_di_mulut else (255, 255, 255)
            cv2.putText(frame, f"Jarak: {round(jarak_terdekat, 2)}", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, warna_teks, 2)

        # 2. LOGIKA SPLIT SCREEN
        if tangan_di_mulut:
            if suara_kicau and not suara_sedang_main:
                suara_kicau.play(-1)
                suara_sedang_main = True
            
            ret_cat, cat_frame = cat_video.read()
            if not ret_cat:
                cat_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret_cat, cat_frame = cat_video.read()
            
            if ret_cat:
                cat_frame = cv2.resize(cat_frame, (int(w * 0.8), h)) 
                tampilan_akhir = np.hstack((frame, cat_frame))
                cv2.putText(tampilan_akhir, "KICAU MANIAAA!", (w + 20, 50), 
                            cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
            else:
                tampilan_akhir = frame # Fallback jika video gagal
        else:
            if suara_sedang_main:
                if suara_kicau: suara_kicau.stop()
                suara_sedang_main = False
            
            # Layar stand-by di samping
            layar_hitam = np.zeros((h, int(w * 0.8), 3), dtype=np.uint8)
            tampilan_akhir = np.hstack((frame, layar_hitam))
            cv2.putText(tampilan_akhir, "Siap Kicau?", (w + 20, h//2), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('Kicau Mania Split Screen', tampilan_akhir)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cat_video.release()
pygame.mixer.quit()
cv2.destroyAllWindows()
