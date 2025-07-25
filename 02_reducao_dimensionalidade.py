# Redução Dimensionalidade de Imagens

from PIL import Image

# Função para converter uma imagem colorida em níveis de cinza
def converter_para_cinza(imagem):
    altura = len(imagem)
    largura = len(imagem[0])
    imagem_cinza = [[0 for _ in range(largura)] for _ in range(altura)]
    
    for i in range(altura):
        for j in range(largura):
            r, g, b = imagem[i][j]
            # Fórmula para converter para cinza: média dos valores RGB
            cinza = int((r + g + b) / 3)
            imagem_cinza[i][j] = cinza
    
    return imagem_cinza

# Função para converter uma imagem colorida em preto e branco (binário)
def converter_para_binario(imagem, limiar=128):
    altura = len(imagem)
    largura = len(imagem[0])
    imagem_binaria = [[0 for _ in range(largura)] for _ in range(altura)]
    
    for i in range(altura):
        for j in range(largura):
            r, g, b = imagem[i][j]
            # Fórmula para converter para cinza: média dos valores RGB
            cinza = int((r + g + b) / 3)
            # Aplicar limiar para binarização
            imagem_binaria[i][j] = 255 if cinza >= limiar else 0
    
    return imagem_binaria

# Função para exibir uma imagem em níveis de cinza
def exibir_imagem_cinza(imagem_cinza):
    altura = len(imagem_cinza)
    largura = len(imagem_cinza[0])
    img = Image.new("L", (largura, altura))  # "L" para imagem em tons de cinza
    
    for i in range(altura):
        for j in range(largura):
            img.putpixel((j, i), imagem_cinza[i][j])
    
    img.show()

# Função para exibir uma imagem binária (preto e branco)
def exibir_imagem_binaria(imagem_binaria):
    altura = len(imagem_binaria)
    largura = len(imagem_binaria[0])
    img = Image.new("1", (largura, altura))  # "1" para imagem binária
    
    for i in range(altura):
        for j in range(largura):
            img.putpixel((j, i), 1 if imagem_binaria[i][j] == 255 else 0)
    
    img.show()

# Função para carregar uma imagem e convertê-la para uma matriz de pixels
def carregar_imagem(caminho):
    img = Image.open(caminho).convert("RGB")
    largura, altura = img.size
    matriz = [[img.getpixel((x, y)) for x in range(largura)] for y in range(altura)]
    return matriz

# Função para criar uma imagem composta
def criar_imagem_composta(imagem_original, imagem_cinza, imagem_binaria):
    altura = len(imagem_original)
    largura = len(imagem_original[0])
    
    # Criar uma nova imagem com largura triplicada para acomodar as três imagens lado a lado
    largura_total = largura * 3
    img_composta = Image.new("RGB", (largura_total, altura))
    
    # Adicionar imagem original
    for i in range(altura):
        for j in range(largura):
            img_composta.putpixel((j, i), imagem_original[i][j])
    
    # Adicionar imagem em níveis de cinza
    for i in range(altura):
        for j in range(largura):
            cinza = imagem_cinza[i][j]
            img_composta.putpixel((j + largura, i), (cinza, cinza, cinza))
    
    # Adicionar imagem binária
    for i in range(altura):
        for j in range(largura):
            binario = 255 if imagem_binaria[i][j] == 255 else 0
            img_composta.putpixel((j + 2 * largura, i), (binario, binario, binario))
    
    img_composta.show()

# Testando as funções
if __name__ == "__main__":

    # Testando as funções com uma imagem real
    # Carregar imagem do diretório
    caminho_imagem = "image.jpg"
    frame = carregar_imagem(caminho_imagem)

    # Converter para níveis de cinza
    imagem_cinza = converter_para_cinza(frame)
    print("Imagem em níveis de cinza processada.")

    # Converter para preto e branco
    imagem_binaria = converter_para_binario(frame, limiar=128)
    print("Imagem em preto e branco processada.")

    # Exibir imagem em níveis de cinza
    exibir_imagem_cinza(imagem_cinza)

    # Exibir imagem em preto e branco
    exibir_imagem_binaria(imagem_binaria)

    # Criar e exibir a imagem composta
    criar_imagem_composta(frame, imagem_cinza, imagem_binaria)
