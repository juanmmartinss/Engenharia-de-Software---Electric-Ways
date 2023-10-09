import sqlite3
import pandas as pd
import json

con = sqlite3.connect("database.db")
cur = con.cursor()

# INSERIR VEÍCULOS
""" df = pd.read_csv('raw_data/cars_formatado.csv')
df.drop('id', axis=1, inplace=True)
df.to_sql('MODELO_VEIC',con,if_exists='append',index=False) """


#INSERIR PONTOS (INCOMPLETO)
with open('raw_data/points_formatado.json', 'r', encoding="utf8") as arquivo:
    dados_raw = json.load(arquivo)

df = pd.json_normalize(dados_raw)
df = df.rename(columns={
    'AddressInfo.Latitude': 'lat',
    'AddressInfo.Longitude': 'long',
    'UsageType.Title': 'info_uso',
    'UsageCost': 'info_custo',
    'AddressInfo.RelatedURL': 'url'
})

df = df[['lat', 'long', 'info_uso', 'info_custo', 'url']]
df.to_sql('PONTO_CARREG',con,if_exists='append',index=False)
con.commit()
con.close()