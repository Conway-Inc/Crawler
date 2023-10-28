import requests
from json import loads
from time import sleep
from datetime import datetime
from urllib3 import PoolManager
import mysql.connector
import csv

conexao = mysql.connector.connect(
    user='user_conway', password='urubu100', host='localhost', database='ConWay', auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()

if conexao.is_connected():
    print("A Conexão ao MySql foi iniciada ")
else:
    print("Houve erro ao conectar")

API_KEY = "52342194d84cfe4bc6b3c191eae44334"

latitude = -23.6263212
longitude = -46.6595853


arquivo = r"C:\Users\chenr\OneDrive\Documents\Crawler Temperatura\tempAeroporto.csv"
#criando o a vari´´avel que será identificada para o arquivo .csv

def get_temperature(latitude, longitude):
        link = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"
        requisicao = requests.get(link)
        requisicao_dick = requisicao.json()

        temperatura = requisicao_dick['main']['temp'] - 273.15
        temperatura_format = f"{temperatura:.2f}"
        return temperatura_format

try:
    with open(arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        
        escritor_csv.writerow(["Temperatura de Congonhas", "Data Temperatura"])

        with PoolManager() as pool:
            while True:
                tempAeroporto = get_temperature(latitude, longitude)
                data_hora = datetime.now()
                dataFormat = data_hora.strftime('%Y-%m-%d %H:%M:%S')

                msgDados = f"""
               ---------------------------------------------------
               | #          ==>     Temperatura Congonhas (SP)   |     
               |Temperatura ==>       {tempAeroporto}                      |               
               ---------------------------------------------------
               
               """
   
                print(msgDados)

                escritor_csv.writerow([tempAeroporto, dataFormat])

                # Verifica se os dados estão realmente escritos no arquivo
                arquivo_csv.flush()
                with open(arquivo, mode='r') as arquivo_leitura:
                    conteudo = arquivo_leitura.read()
                print("Conteúdo do arquivo CSV:")
                print(conteudo)

            
                cursor.execute(
                "INSERT INTO temperaturaAeroporto (temperatura, graus, fkAeroporto, dataHora) VALUES (%s, %s, %s, %s);",
                (tempAeroporto, '°C', 1, dataFormat)
                )

                conexao.commit()
                print("Dados inseridos com sucesso no banco!")

                sleep(1)
except Exception as e:
    print(f"Erro: {e}")
