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

latitude_Congonhas = -23.6263212
longitude_Congonhas = -46.6595853

latitude_Luziania = -15.7975154
longitude_Luziania = -47.8918874

latitude_Confins = -19.6340990
longitude_Confins = -43.9653960

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
        
        escritor_csv.writerow(["Temperatura de Congonhas", "Temperatura de Luziania", "Temperatura de Confins", "Data Temperatura"])

        with PoolManager() as pool:
            while True:
                temperatura_Congonhas = get_temperature(latitude_Congonhas, longitude_Congonhas)
                temperatura_Luziania = get_temperature(latitude_Luziania, longitude_Luziania)
                temperatura_Confins = get_temperature(latitude_Confins, longitude_Confins)
                data_hora = datetime.now()
                dataFormat = data_hora.strftime('%Y-%m-%d %H:%M:%S')

                msgDados = f"""
               ---------------------------------------------------
               | #          ==>     Temperatura Congonhas (SP)   |     
               |Temperatura ==>       {temperatura_Congonhas}                      |               
               ---------------------------------------------------
               ---------------------------------------------------
               | #          ==>     Temperatura Luziânia (DF)    |           
               |Temperatura ==>        {temperatura_Luziania}                     |                       
               ---------------------------------------------------
                --------------------------------------------------
               | #          ==>     Temperatura Confins (BH)     |     
               |Temperatura ==>       {temperatura_Confins}                      |               
               ---------------------------------------------------
               
               """
   
                print(msgDados)

                escritor_csv.writerow([temperatura_Congonhas, temperatura_Luziania, temperatura_Confins, dataFormat])

                # Verifica se os dados estão realmente escritos no arquivo
                arquivo_csv.flush()
                with open(arquivo, mode='r') as arquivo_leitura:
                    conteudo = arquivo_leitura.read()
                print("Conteúdo do arquivo CSV:")
                print(conteudo)

            
                cursor.execute(
                "INSERT INTO temperaturaAeroporto (temperatura, graus, fkAeroporto, dataHora) VALUES (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s);",
                (temperatura_Congonhas, '°C', 1, dataFormat, temperatura_Luziania, '°C', 2, dataFormat, temperatura_Confins, '°C', 3, dataFormat)
                )

                conexao.commit()
                print("Dados inseridos com sucesso no banco!")

                sleep(1)
except Exception as e:
    print(f"Erro: {e}")
