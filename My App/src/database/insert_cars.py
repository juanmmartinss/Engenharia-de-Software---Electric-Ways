import pandas as pd
import sqlite3
df = pd.read_csv('raw/cars_formatado.csv')

conn = sqlite3.connect('database.db')
df.to_sql('MODELO_VEIC',conn,if_exists='replace',index=False)
conn.commit()
conn.close()