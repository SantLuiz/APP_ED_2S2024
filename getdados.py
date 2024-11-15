import requests
import sqlite3
import time

# Configurações da API e da região amazônica
NASA_API_URL = "https://api.nasa.gov/planetary/earth/imagery"
API_KEY = "t89C7dsxmbTY6LP475FGoCbfeD70rnLweZe4ftX3"  # Substitua pela sua chave da API
REGIAO_AMAZONIA = {
    "lat_min": -10.0, "lat_max": 5.0,  # Limites de latitude da Amazônia
    "lon_min": -75.0, "lon_max": -45.0  # Limites de longitude da Amazônia
}

#COORDENADAS BAIXADA SANTISTA
# REGIAO_AMAZONIA = {
#     "lat_min": -24.03, "lat_max": -23.83,  
#     "lon_min": -46.46, "lon_max": -46.25  
# }

# Configuração do banco de dados
conn = sqlite3.connect('Amazonia.db')
cursor = conn.cursor()

# Criação da tabela para armazenamento das imagens
cursor.execute('''
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        latitude REAL,
        longitude REAL,
        image BLOB
    )
''')
conn.commit()

# Função para dividir a região amazônica em uma matriz 10x10 de coordenadas
def gerar_coordenadas(lat_min, lat_max, lon_min, lon_max, grid_size=10):
    lat_step = (lat_max - lat_min) / grid_size
    lon_step = (lon_max - lon_min) / grid_size
    coords = []
    for i in range(grid_size):
        for j in range(grid_size):
            lat = lat_min + i * lat_step
            lon = lon_min + j * lon_step
            coords.append((lat, lon))
    return coords

# Função para baixar uma imagem da API da NASA
def baixar_imagem(lat, lon):
    params = {
        "lon": lon,
        "lat": lat,
        #"dim": 0.1,  # Ajuste da dimensão em graus
        "api_key": API_KEY
    }
    response = requests.get(NASA_API_URL, params=params)
    if response.status_code == 200:
        return response.content  # Retorna imagem binária
    else:
        print(f'ERRO NA API, CODIGO: ',{response.status_code})
    return None

# Função para salvar imagem no banco de dados
def salvar_no_banco(lat, lon, image):
    cursor.execute('''
        INSERT INTO images (latitude, longitude, image)
        VALUES (?, ?, ?)
    ''', (lat, lon, image))
    conn.commit()

# Loop para baixar e armazenar a matriz 10x10 de imagens
def baixar_e_armazenar_imagens():
    coords = gerar_coordenadas(REGIAO_AMAZONIA["lat_min"], REGIAO_AMAZONIA["lat_max"],
                               REGIAO_AMAZONIA["lon_min"], REGIAO_AMAZONIA["lon_max"])
    x = 1
    for lat, lon in coords:
        print(f"{x}. Baixando imagem para coordenadas: Latitude {lat}, Longitude {lon}")
        x+=1
        image = baixar_imagem(lat, lon)
        if image:
            salvar_no_banco(lat, lon, image)
        else:
            print("NÃO É IMAGEM")
        time.sleep(1)  # Pausa para evitar sobrecarga na API

# Executa o script
baixar_e_armazenar_imagens()
print("Finalizado")
# Fechando conexão com o banco de dados
conn.close()
