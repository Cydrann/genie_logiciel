import sqlite3
from . import Data_Base

class Db_Connexion(Data_Base):
    def __init__(self, db_name="users.db"):
        super().__init__(db_name)

    # Fonction pour vérifier le nom d'utilisateur et le mot de passe
    def check_connexion(self, username, password):
        self.connect()
        self.cur.execute("""
            SELECT * FROM user WHERE username = ? AND password = ?
        """, (username, password))
        
        result = self.cur.fetchone()
        
        self.disconnect()
        return result is not None
