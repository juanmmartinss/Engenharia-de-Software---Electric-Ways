import sqlite3
import pandas as pd

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("PRAGMA foreign_keys = ON;")

cur.execute(
    '''CREATE TABLE USUARIO (
        id INTEGER NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    );''')

cur.execute(
    '''CREATE TABLE MODELO_VEIC (
        id INTEGER NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        range REAL,
        efic REAL,
        fast_charge REAL,
        bateria REAL,
        ano INTEGER
    );''')

cur.execute(
    '''CREATE TABLE PERFIL_VEIC (
        id INTEGER NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        id_usuario INTEGER NOT NULL,
        id_modelo INTEGER NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES USUARIO(id),
        FOREIGN KEY (id_modelo) REFERENCES MODELO_VEIC(id)
    );''')

cur.execute(
    '''CREATE TABLE LOCAL_FAV (
        id INTEGER NOT NULL PRIMARY KEY,
        id_usuario INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        lat REAL NOT NULL,
        long REAL NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES USUARIO(id)
    );''')

cur.execute(
    '''CREATE TABLE LOCAL_REC (
        id INTEGER NOT NULL PRIMARY KEY,
        id_usuario INTEGER NOT NULL,
        lat REAL NOT NULL,
        long REAL NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES USUARIO(id)
    );''')

cur.execute(
    '''CREATE TABLE PONTO_CARREG (
        id INTEGER NOT NULL PRIMARY KEY,
        lat REAL NOT NULL,
        long REAL NOT NULL,
        tipo_conexoes TEXT,
        num_conexoes INTEGER,
        potencia REAL,
        amperagem REAL,
        voltagem REAL,
        info_uso TEXT,
        info_custo TEXT,
        url TEXT
    );''')

cur.execute(
    '''CREATE TABLE AVALIACAO (
        id_usuario INTEGER NOT NULL UNIQUE,
        id_ponto INTEGER NOT NULL UNIQUE,
        lat REAL NOT NULL,
        long REAL NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES USUARIO(id),
        FOREIGN KEY (id_ponto) REFERENCES PONTO_CARREG(id)
    );''')

df = pd.read_csv('raw/cars_formatado.csv')
df.to_sql('MODELO_VEIC',con,if_exists='replace',index=False)
con.commit()
con.close()