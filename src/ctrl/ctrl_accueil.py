from src.interface.accueil import Tableau_Acceuil
from src.factories.factory_user import Factory_user
from src.dao.dao_accueil import Db_Accueil
from src.dao.dao_devis import Db_Devis
from src.factories.factory_quote import Factory_Quote
from src.factories.factory_client import Factory_client
from src.entite.quote import Quote

import os

class Ctrl_accueil:
    def __init__(self, username):
        self.vue = Tableau_Acceuil()
        self.db = Db_Accueil()
        self.db_devis = Db_Devis()

        # On affiche le nom de l'utilisateur dans la page d'accueil
        self.vue.nom_utilisateur = username
        self.vue.label_bienvenue.config(text=f"Bienvenue {self.vue.nom_utilisateur}")

        # On appelle la fonction
        self.add_my_infos(username)
        


    # Fonction pour ajouter les informations personnelles de l'utilsateur dans l'onglet "Mes infos"
    def add_my_infos(self, username):

        # Appel de la fonction pour récupérer la table de l'utilisateur en fonction de son nom d'utilisateur
        user_data = self.db.get_user_by_username(username)
        if user_data:
            for i, info in enumerate(user_data):
                self.vue.infos_donnees[i][1] = info
        else:
            print("Utilisateur non trouvé.")


        


    
