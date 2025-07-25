# Bootcamp DIO - Treinamento -> BairesDev - Machine Learning Training

Este diretório foi criado para disponibilizar as tarefas realizadas no bootcamp **DIO - Treinamento -> BairesDev - Machine Learning Training**, que tem como objetivo capacitar profissionais em técnicas de Machine Learning e Inteligência Artificial.

## Arquivos do Projeto

### 1. **`02_reducao_dimensionalidade.py`**
Este script implementa funções para:
- Converter imagens coloridas em níveis de cinza.
- Converter imagens coloridas em preto e branco (binário).
- Exibir as imagens processadas.
- Criar uma imagem composta com a imagem original, a imagem em níveis de cinza e a imagem binária lado a lado.

### 2. **`02-reducao-dimensionalidade.ipynb`**
Notebook que contém as mesmas funções do script Python, permitindo executar as tarefas de redução dimensionalidade diretamente em um ambiente interativo.

### 3. **`requirements.txt`**
Arquivo que lista as dependências do projeto, facilitando a instalação das bibliotecas necessárias. Para instalar, execute:
```bash
pip install -r requirements.txt
```

### 4. **`.gitignore`**
Arquivo de configuração para ignorar arquivos e diretórios desnecessários no controle de versão, como:
- Cache do Python (`__pycache__`).
- Arquivos temporários de IDEs (`.vscode/`, `.idea/`).
- Imagens temporárias (`*.jpg`, `*.png`).

## Funcionalidades do Projeto

1. **Conversão para níveis de cinza**:
   - Converte uma imagem colorida para tons de cinza utilizando a média dos valores RGB.

2. **Conversão para preto e branco (binário)**:
   - Converte uma imagem colorida para binário utilizando um limiar ajustável.

3. **Exibição de imagens**:
   - Exibe as imagens processadas (níveis de cinza e binário) utilizando a biblioteca `Pillow`.

4. **Criação de imagem composta**:
   - Gera uma imagem composta com a imagem original, a imagem em níveis de cinza e a imagem binária lado a lado.

## Requisitos

- Python 3.7 ou superior
- Instale as dependências do projeto utilizando o arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Como executar

1. Certifique-se de que as dependências estão instaladas conforme descrito acima.

2. Coloque a imagem que deseja processar no diretório do projeto e renomeie-a para `image.jpg`.

3. Execute o script `02_reducao_dimensionalidade.py`:
   ```bash
   python 02_reducao_dimensionalidade.py
   ```

4. O script exibirá:
   - A imagem em níveis de cinza.
   - A imagem em preto e branco.
   - A imagem composta com as três transformações.

## Exemplo de Saída

Após executar o script, você verá:
- A imagem original.
- A imagem convertida para níveis de cinza.
- A imagem convertida para preto e branco.
- Uma imagem composta exibindo as três transformações lado a lado.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).