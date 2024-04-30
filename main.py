import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

pasta_imagens = "assets/images"

# Reconhecer todas as imagens da pasta
for imagem in os.listdir(pasta_imagens):
    # Extrair o nome de cada imagem
    nome_imagem, extensao_imagem = os.path.splitext(imagem)

    print(f"Imagem: {nome_imagem} \n")

    # Carregar a imagem
    imagem = Image.open(os.path.join(pasta_imagens, imagem))

    # Usa o pytesseract para realizar OCR na imagem
    texto = pytesseract.image_to_string(imagem)

    # Imprime o texto extraído
    print(texto)