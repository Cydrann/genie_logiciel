import sqlite3
from . import Data_Base

class Db_Inscri(Data_Base):
    def __init__(self, db_name="users.db"):
        super().__init__(db_name)


    # Fonction pour initialiser la table user avec les informations de l'utilisateur
    def init_db(self):
        self.connect()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS user (
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                phone TEXT,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                company TEXT NOT NULL,
                telephone TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()
        self.disconnect()

    # Fonction pour ajouter un utilisateur
    def add_user(self, name, surname, username, phone, email, address, company, telephone, password):
        self.connect()
        self.cur.execute("""
            INSERT INTO user (name, surname, username, phone, email, address, company, telephone, password)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, surname, username, phone, email, address, company, telephone, password))
        self.conn.commit()
        self.disconnect()


    # Fonction pour vérifier si le nom d'utilisateur est déjà pris
    def check_username(self, username):
        self.connect()
        self.cur.execute("""
            SELECT username
            FROM user
            WHERE username = ?
        """, (username,))
        
        result = self.cur.fetchone()
        self.disconnect()

        return result is not None
    

    # Fonction pour vérifier si l'adresse mail est déjà prise
    def check_email(self, email):
        self.connect()
        self.cur.execute("""
            SELECT email
            FROM user
            WHERE email = ?
        """, (email,))
        
        result = self.cur.fetchone()
        self.disconnect()

        return result is not None
    


    # Fonction pour vérifier si le mot de passe est déjà pris
    def check_password(self, password):
        self.connect()
        self.cur.execute("""
            SELECT password
            FROM user
            WHERE password = ?
        """, (password,))
        
        result = self.cur.fetchone()
        self.disconnect()

        return result is not None

    # Fonction pour supprimer la table user
    def clear(self):
        self.connect()
        self.cur.execute("DELETE FROM user")
        self.conn.commit()
        self.disconnect()
        print("✅ Tous les utilisateurs ont été supprimés de la base de données.")
