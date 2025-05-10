from src.entite.client import Client

class Factory_client:
    liste = []

    # Fonction pour créer un client
    @classmethod
    def create_client(cls, name, surname, mobile_phone, email, postal_address):
        client = Client(name, surname, mobile_phone, email, postal_address)
        cls.liste.append(client)

        return cls.liste
    

    # Fonction pour supprimer tous les clients
    @classmethod
    def clear(cls):
        cls.liste = []
        print("Tous les clients ont été supprimé")


    # Surcharge du print
    @classmethod
    def __str__(cls):
        if not Factory_client.liste:
            return "Aucun devis n'a été créé."
    
        return "\n\n".join(str(client) for client in Factory_client.liste)