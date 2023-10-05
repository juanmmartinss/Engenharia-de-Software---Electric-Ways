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


def get_profile(id):
        db = SQLiteDB()
        db.connect()

        cmd = "SELECT nome, email FROM USUARIO WHERE id = ?"
        results = db.execute_query(cmd, (id,))

        db.close()
        return results


def get_vehicles(id):
        db = SQLiteDB()
        db.connect()

        cmd = """SELECT pv.nome, mv.nome, pv.placa, pv.cor, mv.range
                FROM PERFIL_VEIC AS pv
                LEFT JOIN MODELO_VEIC AS mv ON mv.id = pv.id_modelo
                WHERE pv.id_usuario = ?"""
        results = db.execute_query(cmd, (id,))

        db.close()
        return results


def get_vehicle_count(id):
        db = SQLiteDB()
        db.connect()

        cmd = """SELECT COUNT(*) FROM PERFIL_VEIC WHERE id_usuario = ?"""
        results = db.execute_query(cmd, (id,))

        db.close()
        return results


def add_user(username, email, password):
        db = SQLiteDB()
        db.connect()

        cmd = "INSERT INTO USUARIO (nome, email, senha) VALUES (?, ?, ?)"
        db.execute_query(cmd, (username, email, password))

        db.close()