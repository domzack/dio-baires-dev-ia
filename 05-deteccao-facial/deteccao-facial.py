# reconhecimento_deepface.py

import cv2
from mtcnn import MTCNN
from deepface import DeepFace
import os

# Configurações
CAMINHO_IMAGENS = '.'  # Diretório atual
CAMINHO_REFERENCIAS = 'banco_referencias'

# Extensões de imagens válidas
extensoes_validas = [".jpg", ".jpeg", ".png"]

# Lista todas as imagens no diretório
imagens = [f for f in os.listdir(CAMINHO_IMAGENS) if os.path.splitext(f)[1].lower() in extensoes_validas]

if not imagens:
    print("Nenhuma imagem encontrada no diretório.")
    exit()

# Processa cada imagem
for imagem_nome in imagens:
    print(f"Processando: {imagem_nome}")
    CAMINHO_IMAGEM = os.path.join(CAMINHO_IMAGENS, imagem_nome)

    # 1. Carrega imagem
    imagem = cv2.imread(CAMINHO_IMAGEM)

    # 2. Detecta faces com MTCNN
    detector = MTCNN()
    faces = detector.detect_faces(imagem)

    if not faces:
        print(f"Nenhuma face detectada em {imagem_nome}.")
        continue

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
            print(f"Face {i+1} em {imagem_nome}: {identidade}")
            cv2.rectangle(imagem, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(imagem, identidade, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

        except Exception as e:
            print(f"Erro ao reconhecer face {i+1} em {imagem_nome}: {e}")

    # Exibe imagem com nomes
    cv2.imshow(f'Reconhecimento Facial - {imagem_nome}', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
