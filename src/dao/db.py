import sqlite3

class Data_Base:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.conn = None
        self.curs = None

    # Fonction qui fait une connexion avec la base de données
    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        print("Connexion établie à la base de données.")

    
    
    # Fonction pour se déconnecter de la base de données
    def disconnect(self):
        if self.cur:
            self.cur.close()
            print("Curseur fermé.")
        if self.conn:
            self.conn.close()
            print("Connexion à la base de données fermé.")


