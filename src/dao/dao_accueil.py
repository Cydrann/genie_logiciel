import sqlite3
from . import Data_Base

class Db_Accueil(Data_Base):
    def __init__(self, db_name="users.db"):
        super().__init__(db_name)

    # Fonction pour avoir les informations de l'utilisateur en fonction de son nom d'utilisateur
    def get_user_by_username(self, username):
        self.connect()
        self.cur.execute("""
        SELECT name, surname, email, address, company, phone, username
        FROM user
        WHERE username = ?
        """, (username,))

        result = self.cur.fetchone()

        self.disconnect()
        return result  # retourne un tuple (name, surname, email, ...)