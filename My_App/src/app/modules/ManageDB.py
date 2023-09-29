from modules.SQLiteDB import *

def get_user(email):
        db = SQLiteDB()
        db.connect()

        cmd = "SELECT email, senha FROM USUARIO WHERE email = ?"
        results = db.execute_query(cmd, (email,))

        db.close()
        return results


def get_token(email):
        db = SQLiteDB()
        db.connect()

        cmd = "SELECT id FROM USUARIO WHERE email = ?"
        results = db.execute_query(cmd, (email,))

        db.close()
        return results


def add_user(username, email, password):
        db = SQLiteDB()
        db.connect()

        cmd = "INSERT INTO USUARIO (nome, email, senha) VALUES (?, ?, ?)"
        db.execute_query(cmd, (username, email, password))

        db.close()