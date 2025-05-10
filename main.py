# Importation classes pour les controleurs
from src.ctrl.ctrl_inscri import Ctrl_Inscri
from src.ctrl.ctrl_menu import Ctrl_menu
from src.ctrl.ctrl_accueil import Ctrl_accueil

# Importation classes pour la base de données
from src.dao.db import Data_Base
from src.dao.dao_inscri import Db_Inscri
from src.dao.dao_devis import Db_Devis
from src.dao.dao_client import Db_Client
from src.dao.dao_facture import Db_Facture

#-----------------------------------------MAIN----------------------------------------------------------#
"""



    inscri = Db_Inscri()
    inscri.clear()
    devis = Db_Devis()
    devis.clear()
    client = Db_Client()
    client.clear()
    facture = Db_Facture()
    facture.clear()

"""

def main():
    db = Data_Base()
    db.connect()


    """
    QUAND ON SUPPRIME TOUS LES DEVIS ON SUPPRIME AUSSI LES SCREEN
    QUAND ON SUPPRIME UN DEVIS ON SUPPRIME AUSSI SON SCREEN
    """

    while True:
        ctrl_menu = Ctrl_menu() # On lance la page menu, où on peut se connecter ou s'inscrire

        if ctrl_menu.change_page:
            ctrl_inscri = Ctrl_Inscri() # Si on clique sur le bouton inscription, on affiche la page inscription
        else:
            ctrl_accueil = Ctrl_accueil(ctrl_menu.username)
            break







if __name__ == "__main__":
    main()