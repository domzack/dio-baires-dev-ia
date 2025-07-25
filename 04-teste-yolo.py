from ultralytics import YOLO
import os

modelo = YOLO("yolov8n.pt")  # Modelo leve, rápido e já treinado com COCO

# Procurar todas as imagens no diretório atual
extensoes_validas = [".jpg", ".jpeg", ".png"]
imagens = [f for f in os.listdir('.') if os.path.splitext(f)[1].lower() in extensoes_validas]

for caminho_imagem in imagens:
    print(f"Processando: {caminho_imagem}")
    resultados = modelo(caminho_imagem)
    resultados[0].show()  # Exibir imagem com rotulação

    for r in resultados:
        for caixa in r.boxes:
            classe = modelo.names[int(caixa.cls[0])]
            confianca = caixa.conf[0]
            print(f"Classe: {classe}, Confiança: {confianca:.2f}")
