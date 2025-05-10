import json
from .db import Data_Base

class Db_Facture(Data_Base):
    def __init__(self, db_name="users.db"):
        super().__init__(db_name)

    
    # Fonction pour créer la table facture
    def init_db(self):
        self.connect()
        self.cur.execute("PRAGMA foreign_keys = ON;")
        
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS facture (
                facture_id INTEGER PRIMARY KEY AUTOINCREMENT,
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



    # Fonction pour ajouter une facture dans la base de données
    def add_receipt(self, order, order_quantities, date_creation, date_limite, price, status):
        from .dao_devis import Db_Devis

        db_devis = Db_Devis()
        client_id = db_devis.get_client_id_by_quote_id(order, order_quantities, date_limite, price, date_creation)

        if client_id is None:
            print("Aucun client trouvé pour ce devis.")
            return
        
        self.connect()
        self.cur.execute("""
            INSERT INTO facture (client_id, order_items, quantities, date_creation, date_limite, price, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,(
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

        print("Facture ajouté à la base de données")


    
    # Fonction pour avoir toutes les factures 
    def get_all_receipt_summary(self):
        self.connect()
        self.cur.execute("""
            SELECT facture_id, client_id, date_creation, price
            FROM facture
        """)
        rows = self.cur.fetchall()
        self.disconnect()

        # Transforme les lignes en dictionnaires lisibles
        summary_list = [
            {
                "facture_id": row[0],
                "client_id": row[1],
                "date_creation": row[2],
                "price": row[3]
            }
            for row in rows
        ]

        return summary_list
    

    # Fonction pour avoir les informations d'une facture en fonction de son ID
    def get_receipt_summary_by_id(self, id_facture):
        self.connect()
        self.cur.execute("""
            SELECT order_items, quantities, date_creation, date_limite, price FROM facture
            WHERE facture_id = ?
            """, (id_facture,))
        
        rows = self.cur.fetchall()
        self.disconnect()

        summary_list = [
            {
                "order_items": row[0],
                "quantities": row[1],
                "date_creation": row[2],
                "date_limite": row[3],
                "price": row[4]
            }
            for row in rows
        ]    

        return summary_list
    

    # Fonction pour avoir l'id d'une facture à partir de ses attributs
    def get_receipt_id_by_summary(self, order_items, quantities, date_creation, date_limite, price):
        self.connect()
        self.cur.execute("""
            SELECT facture_id FROM facture
            WHERE order_items = ? AND quantities = ? AND date_creation = ? AND date_limite = ? AND price = ?
        """, (json.dumps(order_items), json.dumps(quantities), date_creation, date_limite, price))

        result = self.cur.fetchone()
        self.disconnect
        return result[0] if result else None
        

    # Fonction pour supprimer une facture en fonction de son id
    def remove_receipt(self, id_facture):
        self.connect()
        self.cur.execute("""
            DELETE FROM facture WHERE facture_id = ?
            """, (id_facture,))
        
        self.conn.commit()
        self.disconnect()
        print("Facture", id_facture, "supprimé de la base de données")


    # Fonction pour chercher une/des facture(s)
    def search(self, mot_cle):
        self.connect()

        query = """
            SELECT facture_id, client_id, price, date_creation, status
            FROM facture
            WHERE facture_id = ?
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
                    "receipt_id": row[0],
                    "client_id": row[1],
                    "price": row[2],
                    "date_creation": row[3]
                }
                for row in rows
            ]
            return result
        else:
            return None

    
    # Fonction pour supprimer la table facture
    def clear(self):
        from naim.factories.factory_receipt import Factory_Receipt

        self.connect()
        self.cur.execute("DELETE FROM facture")
        self.cur.execute("DELETE FROM sqlite_sequence WHERE name='facture'")
        self.conn.commit()
        self.disconnect()
        print("✅ Toutes les factures ont été supprimées de la base de données")
        Factory_Receipt.clear()

        import os
        import glob

        # Supprimer les fichiers PNG des devis
        dossier_png = os.path.join("naim", "png", "facture")
        fichiers_png = glob.glob(os.path.join(dossier_png, "*.png"))
        for fichier in fichiers_png:
            os.remove(fichier)

        print("Tous les screens des factures ont été supprimé.")

        # Supprimer les fichiers PDF des devis
        dossier_pdf = os.path.join("naim", "pdf", "facture")
        fichiers_pdf = glob.glob(os.path.join(dossier_pdf, "*.pdf"))
        for fichier in fichiers_pdf:
            os.remove(fichier)

        print("Tous les pdf des factures ont été supprimé.")

