from PIL import Image
import sqlite3
import io

# Função para dividir uma imagem escolhida qualquer em uma grade de 10x10
def dividir_imagem(imagem_caminho, grid_size=10):
    imagem = Image.open(imagem_caminho)
    largura, altura = imagem.size
    largura_pedaço = largura // grid_size
    altura_pedaço = altura // grid_size

    pedaços = []
    for linha in range(grid_size):
        for coluna in range(grid_size):
            # Define as coordenadas do pedaço
            esquerda = coluna * largura_pedaço
            superior = linha * altura_pedaço
            direita = esquerda + largura_pedaço
            inferior = superior + altura_pedaço

            # Recorta o pedaço
            pedaço = imagem.crop((esquerda, superior, direita, inferior))

            # Armazena o pedaço como bytes
            buffer = io.BytesIO()
            pedaço.save(buffer, format="JPEG")
            pedaço_bytes = buffer.getvalue()
            buffer.close()

            # Adiciona o pedaço à lista com sua posição
            pedaços.append((linha, coluna, pedaço_bytes))

    return pedaços

# Função para salvar os pedaços no banco de dados
def salvar_pedaços_no_db(pedaços, db_caminho='IMGMANAUS.db'):
    conn = sqlite3.connect(db_caminho)
    cursor = conn.cursor()

    # Cria a tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grid_imagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            linha INTEGER,
            coluna INTEGER,
            imagem BLOB
        )
    ''')

    # Insere cada pedaço no banco de dados
    for linha, coluna, pedaço_bytes in pedaços:
        cursor.execute('''
            INSERT INTO grid_imagens (linha, coluna, imagem)
            VALUES (?, ?, ?)
        ''', (linha, coluna, pedaço_bytes))

    # Salva as alterações e fecha a conexão
    conn.commit()
    conn.close()

# Caminho da imagem de entrada
imagem_caminho = 'MANAUS.jpg'

# Divide a imagem em pedaços
pedaços = dividir_imagem(imagem_caminho)

# Salva os pedaços no banco de dados
salvar_pedaços_no_db(pedaços)
