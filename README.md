# Bootcamp DIO - BairesDev
## Machine Learning Training

Este diretório foi criado para disponibilizar as tarefas realizadas no bootcamp **DIO - BairesDev - Machine Learning Training**, que tem como objetivo capacitar profissionais em técnicas de Machine Learning e Inteligência Artificial.

## Arquivos do Projeto

### **`01-cats-vs-dogs.ipynb`**
Notebook que implementa um modelo de classificação de imagens para distinguir entre gatos e cachorros. Este projeto utiliza técnicas de pré-processamento de imagens e redes neurais convolucionais (CNNs) para treinar e avaliar o modelo.

### **`02_reducao_dimensionalidade.py`**
Este script implementa funções para:
- Converter imagens coloridas em níveis de cinza.
- Converter imagens coloridas em preto e branco (binário).
- Exibir as imagens processadas.
- Criar uma imagem composta com a imagem original, a imagem em níveis de cinza e a imagem binária lado a lado.

### **`03-calculo-metricas.py`**
Este script realiza a análise de desempenho de modelos de classificação para múltiplas classes. Ele inclui:
- Geração de uma matriz de confusão para múltiplas classes.
- Cálculo de métricas de desempenho (Sensibilidade, Especificidade, Precisão e F-Score) para cada classe.
- Visualização das métricas em um gráfico de barras.
- Plotagem da curva ROC para cada classe, com cálculo do AUC.

### **`04-treinamento-yolo.py`**
Este script realiza o download, extração, preparação dos dados e treinamento de um modelo YOLOv8 utilizando o dataset COCO. Ele inclui:
- Download dos arquivos de imagens (`train2017.zip`) e anotações (`annotations_trainval2017.zip`) do dataset COCO, com exibição do tamanho dos arquivos antes do download.
- Filtragem de imagens e anotações para classes específicas (`dog` e `person`).
- Conversão das anotações para o formato YOLO (`class_id x_center y_center width height`).
- Treinamento do modelo YOLOv8 com parâmetros como modelo base (`yolov8n.pt`), número de épocas (50) e tamanho da imagem (640x640).

### **`04-teste-yolo.py`**
Este script utiliza o modelo YOLOv8 para realizar detecção de objetos em imagens. Ele inclui:
- Busca automática por todas as imagens no diretório atual com extensões válidas (`.jpg`, `.jpeg`, `.png`).
- Realiza a detecção de objetos em cada imagem utilizando o modelo YOLOv8 pré-treinado.
- Exibe as imagens com as detecções rotuladas.
- Imprime no terminal as classes detectadas e suas respectivas confiabilidades.

### **`requirements.txt`**
Arquivo que lista as dependências do projeto, facilitando a instalação das bibliotecas necessárias. Para instalar, execute:
```bash
pip install -r requirements.txt
```

### **`.gitignore`**
Arquivo de configuração para ignorar arquivos e diretórios desnecessários no controle de versão, como:
- Cache do Python (`__pycache__`).
- Arquivos temporários de IDEs (`.vscode/`, `.idea/`).
- Imagens temporárias (`*.jpg`, `*.png`).

## Funcionalidades do Projeto

### Cats vs Dogs
1. **Classificação de imagens**:
   - Treina um modelo para distinguir entre imagens de gatos e cachorros.
   - Utiliza redes neurais convolucionais (CNNs) para o aprendizado.

2. **Pré-processamento de imagens**:
   - Realiza ajustes nas imagens para melhorar o desempenho do modelo.

### Redução Dimensionalidade
1. **Conversão para níveis de cinza**:
   - Converte uma imagem colorida para tons de cinza utilizando a média dos valores RGB.

2. **Conversão para preto e branco (binário)**:
   - Converte uma imagem colorida para binário utilizando um limiar ajustável.

3. **Exibição de imagens**:
   - Exibe as imagens processadas (níveis de cinza e binário) utilizando a biblioteca `Pillow`.

4. **Criação de imagem composta**:
   - Gera uma imagem composta com a imagem original, a imagem em níveis de cinza e a imagem binária lado a lado.

### Cálculo de Métricas
1. **Matriz de Confusão**:
   - Gera e exibe uma matriz de confusão para múltiplas classes.

2. **Cálculo de Métricas**:
   - Calcula métricas como Sensibilidade, Especificidade, Precisão e F-Score para cada classe.

3. **Visualização de Métricas**:
   - Exibe as métricas em um gráfico de barras para facilitar a comparação entre classes.

4. **Curva ROC**:
   - Plota a curva ROC para cada classe, calculando o AUC.

### Treinamento YOLO
1. **Download e extração de dados COCO**:
   - Baixa os arquivos de imagens e anotações do dataset COCO.
   - Exibe o tamanho dos arquivos antes de baixá-los.
   - Extrai os arquivos para a pasta `coco_data`.

2. **Preparação do dataset YOLO**:
   - Filtra imagens e anotações para classes específicas (`dog` e `person`).
   - Converte as anotações para o formato YOLO (`class_id x_center y_center width height`).
   - Salva as imagens e anotações em `yolo_dataset/images` e `yolo_dataset/labels`.

3. **Treinamento YOLO**:
   - Inicia o treinamento do modelo YOLOv8 com os seguintes parâmetros:
     - Modelo base: `yolov8n.pt`.
     - Número de épocas: 50.
     - Tamanho da imagem: 640x640.

### Teste YOLO
1. **Detecção de objetos**:
   - Busca automaticamente todas as imagens no diretório atual.
   - Realiza a detecção de objetos em cada imagem utilizando o modelo YOLOv8.
   - Exibe as imagens com as detecções rotuladas.
   - Imprime no terminal as classes detectadas e suas confiabilidades.

## Requisitos

- Python 3.7 ou superior
- Instale as dependências do projeto utilizando o arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Como executar

1. Certifique-se de que as dependências estão instaladas conforme descrito acima.

2. Para o projeto de cálculo de métricas:
   - Execute o script `03-calculo-metricas.py`:
     ```bash
     python 03-calculo-metricas.py
     ```

3. Para o treinamento YOLO:
   - Execute o script `04-treinamento-yolo.py`:
     ```bash
     python 04-treinamento-yolo.py
     ```

4. Para o teste YOLO:
   - Execute o script `04-teste-yolo.py`:
     ```bash
     python 04-teste-yolo.py
     ```

5. Para os outros projetos, siga as instruções específicas de cada arquivo.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).