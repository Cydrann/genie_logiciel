import json
from .db import Data_Base

class Db_Devis(Data_Base):
    def __init__(self, db_name="users.db"):
        super().__init__(db_name)


    # Fonction pour créer table devis
    def init_db(self):
        self.connect()
        self.cur.execute("PRAGMA foreign_keys = ON;")

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS devis (
                quote_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                order_items TEXT NOT NULL,
                quantities TEXT NOT NULL,
                date_creation TEXT NOT NULL,
                date_limite TEXT NOT NULL,
                price REAL NOT NULL,
                status INTEGER NOT NULL,
                FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE CASCADE
            )
        """)
        self.conn.commit()
        self.disconnect()


    
    # Fonction pour ajouter un devis
    def add_quote(self, name, surname, phone, email, address,
                order, order_quantities, date_creation, date_limite, price, status):
        from .dao_client import Db_Client

        db_client = Db_Client(self.db_name)
        client_id = db_client.get_client_id(name, surname, phone, email, address)
        if client_id is None:
            print("Client non trouvé, impossible d'ajouter le devis")
            return

        self.connect()
        self.cur.execute("""
            INSERT INTO devis (client_id, order_items, quantities, date_creation, date_limite, price, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            client_id,
            json.dumps(order),                   
            json.dumps(order_quantities),       
            date_creation,
            date_limite,
            price,
            int(status)                         
        ))
        self.conn.commit()
        self.disconnect()

        print("Devis ajouté à la base de donnée")


    # Fonction pour récupérer l'id, le prix et la date de création des devis
    def get_all_quotes_summary(self):
        self.connect()
        self.cur.execute("""
            SELECT quote_id, client_id, price, date_creation, status
            FROM devis
        """)
        rows = self.cur.fetchall()
        self.disconnect()

        # Transforme les lignes en dictionnaires lisibles
        summary_list = [
            {
                "quote_id": row[0],
                "client_id": row[1],
                "price": row[2],
                "date_creation": row[3], 
                "status": row[4]
            }
            for row in rows
        ]

        return summary_list
    

    # Fonction avoir tous les attributs d'un devis à partir de son id
    def get_quote_by_id(self, quote_id):
        self.connect() 
        self.cur.execute("""
            SELECT quote_id, client_id, order_items, quantities, date_limite, price, date_creation 
            FROM devis
            WHERE quote_id = ?
        """, (quote_id,)) 
        row = self.cur.fetchone() 

        self.disconnect()  

        # Vérifie si une ligne a été trouvée
        if row is None:
            print("Il n'existe pas de devis à partir de cet id")
            return None  

        # Transformation des résultats en dictionnaire 
        quote_details = {
            "quote_id": row[0],
            "client_id": row[1],
            "order_items": row[2], 
            "quantities": row[3],  
            "date_limite": row[4],
            "price": row[5],
            "date_creation": row[6]
        }

        return quote_details



    # Fonction pour changer de statut un devis quand on clique sur le bouton valider
    def validate_quote(self, id_devis):
        self.connect()
        self.cur.execute("""UPDATE devis SET status = 1 
                         WHERE quote_id = ?""", (id_devis,))
        self.conn.commit()
        self.disconnect()



    # Fonction pour retourner l'id d'un devis
    def get_quote_id(self, order, order_quantities, date_limite, price, date_creation):
        self.connect()
        self.cur.execute("""
            SELECT quote_id FROM devis
            WHERE order_items = ?
            AND quantities = ?
            AND date_limite = ?
            AND price = ?
            AND date_creation = ?
        """, (json.dumps(order), json.dumps(order_quantities), date_limite, price, date_creation))
        result = self.cur.fetchone()
        self.disconnect()
        return result[0] if result else None
    

    # Fonction pour avoir l'id du client à partir du id du devis
    def get_client_id_by_quote_id(self, order, order_quantities, date_limite, price, date_creation):
        devis_id = self.get_quote_id(order, order_quantities, date_limite, price, date_creation)
        self.connect()
        self.cur.execute("""
            SELECT client_id
            FROM devis
            WHERE order_items = ?
            AND quantities = ?
            AND date_limite = ?
            AND price = ?
            AND date_creation = ?
            """, (order, order_quantities, date_limite, price, date_creation))
        
        result = self.cur.fetchone()
        self.disconnect()

        return result[0] if result else None
    

    # Fonction pour supprimer un devis en fonction de son id
    def remove_quote(self, id_devis):
        self.connect()
        self.cur.execute("""
            DELETE FROM devis WHERE quote_id = ?           
            """, (id_devis,))
        
        self.conn.commit()
        self.disconnect()
        print("Devis", id_devis, "supprimé de la base de données")


    # Fonction pour chercher un/des devis
    def search(self, mot_cle):
        self.connect()

        query = """
            SELECT quote_id, client_id, price, date_creation, status
            FROM devis
            WHERE quote_id = ?
            OR client_id = ?
            OR price LIKE ?
            OR date_creation LIKE ?
        """

        try:
            # On tente de caster price pour éviter erreur sur float
            mot_cle_float = float(mot_cle)
        except ValueError:
            mot_cle_float = None

        params = (mot_cle, mot_cle, mot_cle_float, f"%{mot_cle}%")
        self.cur.execute(query, params)

        rows = self.cur.fetchall()
        self.disconnect()

        if rows:
            result = [
                {
                    "quote_id": row[0],
                    "client_id": row[1],
                    "price": row[2],
                    "date_creation": row[3],
                    "status": row[4]
                }
                for row in rows
            ]
            return result
        else:
            return None




    # Fonction pour supprimer la table devis
    def clear(self):
        from src.factories.factory_quote import Factory_Quote

        self.connect()
        self.cur.execute("DELETE FROM devis")
        self.cur.execute("DELETE FROM sqlite_sequence WHERE name='devis'")  # Réinitialise l'auto-incrément
        self.conn.commit()
        self.disconnect()
        print("✅ Tous les devis ont été supprimés et les IDs réinitialisés.")
        Factory_Quote.clear()

        import os
        import glob

        # Supprimer les fichiers PNG des devis
        dossier_png = os.path.join("src", "png", "devis")
        fichiers_png = glob.glob(os.path.join(dossier_png, "*.png"))
        for fichier in fichiers_png:
            os.remove(fichier)

        print("Tous les screens des Devis ont été supprimé.")

        # Supprimer les fichiers PDF des devis
        dossier_pdf = os.path.join("src", "pdf", "devis")
        fichiers_pdf = glob.glob(os.path.join(dossier_pdf, "*.pdf"))
        for fichier in fichiers_pdf:
            os.remove(fichier)

        print("Tous les pdf des devis ont été supprimé.")

