from src.interface.menu import Affiche_Accueil
from src.interface.accueil import Tableau_Acceuil

from src.ctrl.ctrl_inscri import Ctrl_Inscri
from src.ctrl.ctrl_accueil import Ctrl_accueil

from src.dao.dao_connexion import Db_Connexion
from src.exception.ex_connexion import Ex_conn

from src.globals import *

class Ctrl_menu:
    def __init__(self):
        self.vue = Affiche_Accueil()
        self.vue.register.config(command=self.open_inscription)   # Quand on appuie sur le bouton d'inscription, on ouvre la page inscription
        self.vue.bouton_connexion.config(command=self.check_datas)
        self.vue.language.config(command=self.switch_language)
        self.change_page = False    # Attribut pour changer de page
        self.db = Db_Connexion()

        self.username = self.vue.entry_user.get()

        self.vue.mainloop()

        

    def open_inscription(self):
        self.change_page = True
        self.vue.destroy()

    def check_datas(self):
        username = self.vue.entry_user.get()
        password = self.vue.entry_pass.get()

        if(self.db.check_connexion(username, password)):
            Ex_conn.success(username)
            self.vue.destroy() # On ferme la fenêtre de connexion
            Ctrl_accueil(username) # On lance la page d'accueil
        else:
            Ex_conn.display()

    def switch_language(self):
        global current_language

        if(current_language == "fr"):
            Ex_conn.msg_english()
            current_language = "en"
        
        elif(current_language == "en"):
            Ex_conn.msg_french()
            current_language = "fr"

    