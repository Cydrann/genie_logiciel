from .db import Data_Base

class Db_Client(Data_Base):
    def __init__(self, db_name="users.db"):
        super().__init__(db_name)

    
    # Fonction pour initialiser la table client
    def init_db(self):
        self.connect()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS client (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                address REAL NOT NULL
            )
        """)
        self.conn.commit()
        self.disconnect()


    # Fonction pour vérifier si un client est déjà dans la base de données
    def client_exists(self, name, surname, phone, email, address):
        self.connect()
        self.cur.execute("""
            SELECT COUNT(*) FROM client
            WHERE name = ? AND surname = ? AND phone = ? AND email = ? AND address = ?
        """, (name, surname, phone, email, address))
        result = self.cur.fetchone()[0]
        self.disconnect()
        return result > 0


    # Fonction pour ajouter un client dans la base de données
    def add_client(self, name, surname, phone, email, address):
        # Avant d'ajouter un client on vérifie s'il est déjà dans la base de données
        if(self.client_exists(name, surname, phone, email, address) == False):
            self.connect()
            self.cur.execute("""
                INSERT INTO client (name, surname, phone, email, address)
                VALUES (?, ?, ?, ?, ?)
            """, (name, surname, phone, email, address))
            self.conn.commit()
            self.disconnect()

            print("Client ajouté à la base de donnée")


    # Fonction pour vérifier si le numéro de téléphone est déjà présent dans la base de données
    def already_phone(self, phone):
        self.connect()
        self.cur.execute("""
            SELECT phone FROM client
            WHERE phone = ?
            """, (phone,))
        
        result = self.cur.fetchone()
        self.disconnect()
        return result[0] if result else None
    
    
    # Fonction pour vérifier si l'adresse mail est déjà présente dans la base de données
    def already_email(self, email):
        self.connect()
        self.cur.execute("""
            SELECT email FROM client
            WHERE email = ?
            """, (email,))
        
        result = self.cur.fetchone()
        self.disconnect()
        return result[0] if result else None

    
    # Fonctio pour récupérer l'id d'un client
    def get_client_id(self, name, surname, phone, email, address):
        self.connect()
        self.cur.execute("""
            SELECT client_id FROM client
            WHERE name = ? AND surname = ? AND phone = ? AND email = ? AND address = ?
        """, (name, surname, phone, email, address))
        result = self.cur.fetchone()
        self.disconnect()
        return result[0] if result else None


    # Fonction pour récupérer les informations de tous les clients
    def get_all_clients_summary(self):
        self.connect()
        self.cur.execute("""
            SELECT client_id, surname, name, address FROM client
        """)
        rows = self.cur.fetchall()
        self.disconnect()

        # Transforme les lignes en dictionnaires lisibles
        summary_list = [
            {"client_id": row[0], "surname": row[1], "name": row[2], "address": row[3]}
            for row in rows
        ]

        return summary_list
    
    # Fonction pour supprimer un client de la base de données
    def remove_client(self, id_client):
        self.connect()
        self.cur.execute("""
            DELETE FROM client WHERE client_id = ?
            """, (id_client,))
        
        self.conn.commit()
        self.disconnect()
        print("Client", id_client, "supprimé de la base de données")



    # Fonction pour chercher un/des client(s)
    def search(self, mot_cle):
        self.connect()

        query = """
            SELECT client_id, name, surname, address
            FROM client
            WHERE CAST(client_id AS TEXT) = ?
            OR name LIKE ?
            OR surname LIKE ?
            OR address LIKE ?
        """

        # On applique LIKE pour les champs textuels pour permettre une recherche partielle
        like_mot_cle = f"%{mot_cle}%"
        params = (mot_cle, like_mot_cle, like_mot_cle, like_mot_cle)

        self.cur.execute(query, params)
        rows = self.cur.fetchall()
        self.disconnect()

        if rows:
            result = [
                {
                    "client_id": row[0],
                    "name": row[1],
                    "surname": row[2],
                    "address": row[3]
                }
                for row in rows
            ]
            return result
        else:
            return None



    # Fonction pour effacer les clients de la base de données
    def clear(self):
        from src.factories.factory_client import Factory_client

        self.connect()
        self.cur.execute("DELETE FROM client")
        self.cur.execute("DELETE FROM sqlite_sequence WHERE name='client'")  # Réinitialise l'auto-incrément
        self.conn.commit()
        self.disconnect()
        print("✅ Tous les clients ont été supprimés et les IDs réinitialisés.")
        Factory_client.clear()