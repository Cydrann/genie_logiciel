from typing import Optional
from ..entite.user import User

class Factory_user:
    user: Optional[User] = None  # L'utilisateur est stocké ici après création

    # Fonction pour créer un utilisateur
    @classmethod
    def create_user(cls, name, surname, username, mobile_phone, email, postal_address, company, phone, password) -> User:
        if cls.user is not None:
            raise ValueError("Un utilisateur est déjà enregistré.")
        
        if not all([name, surname, username, password, email]):
            raise ValueError("Tous les champs sont obligatoires.")
        
        cls.user = User(name, surname, username, mobile_phone, email, postal_address, company, phone, password)
        return cls.user

    @classmethod
    def get_user(cls) -> Optional[User]:
        return cls.user

    # Fonction pour supprimer l'utilisateur
    @classmethod
    def clear(cls):
        cls.user = None
        print("L'utilisateur a été effacé")

    # Surcharge du print
    def __str__(self):
        if self.user:
            return f"User: {self.user.username} ({self.user.email}), pour la société {self.user.company}"
        return "Aucun utilisateur enregistré."
