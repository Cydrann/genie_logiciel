from src.entite.quote import Quote

class Factory_Quote:
    liste = [] # Variable de classe pour stocker tous les devis

    
    # Fonction pour créer un devis
    @classmethod
    def create_quote(cls, order, order_quantities, limit_date, price):
        quote = Quote(order, order_quantities, limit_date, price)
        cls.liste.append(quote)

        return cls.liste
    

    # Fonction pour supprimer tous les devis
    @classmethod
    def clear(cls):
        cls.liste = []
        print("Tous les devis ont été supprimé du factory")


    # Surcharge du print
    def __str__(self):
        if not Factory_Quote.liste:
            return "Aucun devis n'a été créé."
        
        return "\n\n".join(str(quote) for quote in Factory_Quote.liste)
    
