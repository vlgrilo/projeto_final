from PIL import Image
import os

# 1) Criar um dicionário tendo como chave o nome da figurinha, e o valor o nome do arquivo da imagem correspondente;
figurinhas = {}
diretorio_imagens = 'imagens'

for nome_imagem in os.listdir(diretorio_imagens):
    nome_figurinha = os.path.splitext(nome_imagem)[0]
    figurinhas[nome_figurinha] = nome_imagem

# 2) Criar uma lista com o nome de todas as figurinhas e salvar esta lista em um arquivo de texto chamado lista_figurinhas.txt;
nomes_figurinhas = list(figurinhas.keys())

with open('lista_figurinhas.txt', 'w') as arquivo:
    arquivo.write('\n'.join(nomes_figurinhas))

# 3) Criar uma outra lista com os nomes das imagens, e salvar esta outra lista em um arquivo de texto chamado lista_imagens.txt;
nomes_imagens = list(figurinhas.values())

with open('lista_imagens.txt', 'w') as arquivo:
    arquivo.write('\n'.join(nomes_imagens))

# 4) Imprimir na tela a lista com o nome de todas as figurinhas;
for nome_figurinha in nomes_figurinhas:
    print(nome_figurinha)

# 5) Escolher cinco figurinhas;
figurinhas_escolhidas = []
contador = 0

print("Escolha 5 figurinhas:")

while contador < 5:
    figurinha = input(str(contador + 1) + "° figurinha: ")
    
    if figurinha in figurinhas:
        figurinhas_escolhidas.append(figurinha)
        contador += 1
    else:
        print("Figurinha não encontrada. Por favor, escolha novamente.")

#6) Criar uma imagem com estas figurinhas, que foram escolhidas:
imagens_figurinhas = []
largura_total = 0
altura_maxima = 0

for figurinha in figurinhas_escolhidas:
    nome_arquivo = figurinhas[figurinha]
    imagem_figurinha = Image.open(os.path.join(diretorio_imagens, nome_arquivo))
    largura, altura = imagem_figurinha.size
    imagens_figurinhas.append(imagem_figurinha)
    largura_total += largura
    altura_maxima = max(altura_maxima, altura)

imagem_composta = Image.new('RGB', (largura_total, altura_maxima))

x_offset = 0

for imagem_figurinha in imagens_figurinhas:
    imagem_composta.paste(imagem_figurinha, (x_offset, 0))
    x_offset += imagem_figurinha.width

imagem_composta.save('imagem_figurinhas.png')

#7) Criar um arquivo de texto, que tenha uma relação das figurinhas escolhidas
with open('figurinhas_escolhidas.txt', 'w') as arquivo:
    for figurinha in figurinhas_escolhidas:
        arquivo.write(figurinha + '\n')

#8) Mostrar a imagem criada
imagem_composta.show()