from src.entite.receipt import Receipt

class Factory_Receipt:
    liste = [] # Variable de classe pour stocker les factures


    # Fonction pour créer une facture
    @classmethod
    def create_receipt(cls, order, order_quantities, limit_date, price):
        receipt = Receipt(order, order_quantities, limit_date, price)
        cls.liste.append(receipt)

        return cls.liste
    

    # Fonction pour enlever toutes les factures
    @classmethod
    def clear(cls):
        cls.liste = []
        print("Toutes les factures ont été supprimé du factory")


    # Surcharge du print
    @classmethod
    def __str__(cls):
        if not Factory_Receipt.liste:
            return "Aucun devis n'a été créé."
        
        return "\n\n".join(str(receipt) for receipt in Factory_Receipt.liste)        
    