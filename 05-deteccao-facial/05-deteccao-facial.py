# reconhecimento_deepface.py

import cv2
from mtcnn import MTCNN
from deepface import DeepFace
import os

# Configurações
CAMINHO_IMAGEM = 'foto_teste.jpg'
CAMINHO_REFERENCIAS = 'banco_referencias'

# 1. Carrega imagem
imagem = cv2.imread(CAMINHO_IMAGEM)

# 2. Detecta faces com MTCNN
detector = MTCNN()
faces = detector.detect_faces(imagem)

if not faces:
    print("Nenhuma face detectada.")
    exit()

for i, face in enumerate(faces):
    x, y, w, h = face['box']
    face_crop = imagem[y:y+h, x:x+w]

    # Salva temporariamente a face para reconhecimento
    nome_face = f'temp_face_{i+1}.jpg'
    cv2.imwrite(nome_face, face_crop)

    try:
        resultado = DeepFace.find(img_path=nome_face, db_path=CAMINHO_REFERENCIAS, enforce_detection=False)

        if resultado.empty:
            identidade = "Desconhecido"
        else:
            identidade = os.path.basename(resultado.iloc[0]['identity']).replace('.jpg', '')

        # Exibe resultado
        print(f"Face {i+1}: {identidade}")
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(imagem, identidade, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

    except Exception as e:
        print(f"Erro ao reconhecer face {i+1}: {e}")

# Exibe imagem com nomes
cv2.imshow('Reconhecimento Facial', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
