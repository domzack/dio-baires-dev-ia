import os
import urllib.request
import zipfile
import shutil
import subprocess
import requests
from pycocotools.coco import COCO

# Função para download e extração de arquivos
def download_and_extract(url, output_path, extract_to):
    # Exibir tamanho do arquivo
    response = requests.head(url)
    file_size = int(response.headers.get('Content-Length', 0)) / (1024 * 1024)  # Convertendo para MB
    print(f"Tamanho do arquivo: {file_size:.2f} MB")
    
    print(f"Baixando: {url}")
    urllib.request.urlretrieve(url, output_path)
    print(f"Extraindo: {output_path}")
    with zipfile.ZipFile(output_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# URLs oficiais
base_url = "http://images.cocodataset.org"
train_zip_url = f"{base_url}/zips/train2017.zip"
ann_zip_url = f"{base_url}/annotations/annotations_trainval2017.zip"

# Criação de diretórios
os.makedirs('coco_data', exist_ok=True)

# Download e extração
download_and_extract(train_zip_url, 'coco_data/train2017.zip', 'coco_data')
download_and_extract(ann_zip_url, 'coco_data/annotations.zip', 'coco_data')

# Caminhos para os arquivos extraídos
coco_annotation_file = 'coco_data/annotations/instances_train2017.json'
images_dir = 'coco_data/train2017'
output_dir = 'yolo_dataset'
selected_classes = ['dog', 'person']

# Criação das pastas
os.makedirs(f'{output_dir}/images', exist_ok=True)
os.makedirs(f'{output_dir}/labels', exist_ok=True)

# Carregando anotações COCO
coco = COCO(coco_annotation_file)

# IDs das classes selecionadas
class_ids = coco.getCatIds(catNms=selected_classes)
class_id_map = {id: i for i, id in enumerate(class_ids)}  # Reindexa: dog = 0, person = 1

# Processar cada anotação
image_ids = coco.getImgIds(catIds=class_ids)
for img_id in image_ids:
    img_info = coco.loadImgs(img_id)[0]
    file_name = img_info['file_name']
    
    # Copia imagem para pasta YOLO
    src = os.path.join(images_dir, file_name)
    dst = os.path.join(output_dir, 'images', file_name)
    if not os.path.exists(dst):
        shutil.copy(src, dst)
    
    # Carrega anotações (bounding boxes)
    ann_ids = coco.getAnnIds(imgIds=img_id, catIds=class_ids, iscrowd=None)
    anns = coco.loadAnns(ann_ids)

    # Gerar arquivo .txt no estilo YOLO
    label_file = os.path.join(output_dir, 'labels', file_name.replace('.jpg', '.txt'))
    with open(label_file, 'w') as f:
        for ann in anns:
            cat_id = ann['category_id']
            bbox = ann['bbox']
            x, y, w, h = bbox
            x_center = (x + w / 2) / img_info['width']
            y_center = (y + h / 2) / img_info['height']
            w /= img_info['width']
            h /= img_info['height']
            f.write(f"{class_id_map[cat_id]} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

subprocess.run([
    "yolo", "train",
    "model=yolov8n.pt",
    "data=data.yaml",
    "epochs=50",
    "imgsz=640"
])