from src.interface.inscription import Affiche_Inscription

from src.factories.factory_user import Factory_user 
from src.dao.dao_inscri import Db_Inscri

class Ctrl_Inscri:
    def __init__(self):
        self.factory = Factory_user()
        self.vue = Affiche_Inscription()
        self.vue.bouton_ok.config(command=self.get_datas)
        self.db = Db_Inscri()
        self.db.init_db()
        self.vue.mainloop()

    # Fonction qui récupère les infos lors de l'inscription
    def get_datas(self):
        from src.exception.ex_inscri import Ex_inscri

        from src.format.format_inscri import Format_inscri
        """
        On récupère les informations écrites par l'utilisateur
        """
        nom = self.vue.entry_nom.get()
        prenom = self.vue.entry_prenom.get()
        nom_utilisateur = self.vue.entry_nom_utilisateur.get()
        email = self.vue.entry_adresse_mail.get()
        adresse_postale = self.vue.entry_adresse_postale.get()
        entreprise = self.vue.entry_societe.get()
        mot_de_passe = self.vue.entry_mot_de_passe.get()
        telephone = self.vue.entry_telephone.get()

        """
        On vérifie si les informations les plus importantes sont disponibles
        (email, nom utilisateur, téléphone, email)
        """

        if(self.db.check_username(nom_utilisateur)):
            Ex_inscri.already_username()
            return False
        
        if(self.db.check_email(email)):
            Ex_inscri.already_email()
            return False
        
        if(self.db.check_password(mot_de_passe)):
            Ex_inscri.already_password()
            return False
        
        
        """
        On vérifie si les formats des champs sont conformes
        """
        if(Format_inscri.format_surname(nom) == False):
            Ex_inscri.format_surname()
            return None

        if(Format_inscri.format_name(prenom) == False):
            Ex_inscri.format_name()
            return None
        
        if(Format_inscri.format_email(email) == False):
            Ex_inscri.format_email()
            return None
        
        if(Format_inscri.format_phone(telephone) == False):
            Ex_inscri.format_phone()
            return None
        
        if(Format_inscri.format_password(mot_de_passe) == False):
            Ex_inscri.format_password()
            return None

        """
        On vérifie si les champs sont vides
        """
        if(nom == ""):
            Ex_inscri.check_surname()
            return False

        if(prenom == ""):
            Ex_inscri.check_name()
            return False
        
        if(email == ""):
            Ex_inscri.check_email()
            return False
        
        if(adresse_postale == ""):
            Ex_inscri.check_adress()
            return False
        
        if(entreprise == ""):
            Ex_inscri.check_company()
            return False
        
        if(telephone == ""):
            Ex_inscri.check_phone()
            return False
        
        if(nom_utilisateur == ""):
            Ex_inscri.check_username()
            return False

        if(mot_de_passe == ""):
            Ex_inscri.check_password()
            return False
        

        # On vérifie si le mot de passe et la confirmation de mot de passe sont les memes
        if(mot_de_passe != self.vue.entry_confirmer_mdp.get()):
            Ex_inscri.confirm_password()
            return False


        # Création d'un utilisateur via Factory
        fac = Factory_user()
        fac.create_user(prenom, nom, nom_utilisateur,
                        telephone, email, adresse_postale, entreprise, telephone, mot_de_passe)
        
        # On ajoute l'utilisateur à la base de données
        self.db.add_user(prenom, nom, nom_utilisateur, 
                         telephone, email, adresse_postale, entreprise, telephone, mot_de_passe)

        print("Utilisateur créé avec succès !")
        print("Utilisateur ajouté à la base de données")
        print(fac)

        Ex_inscri.msg_valid()
        self.vue.destroy()
        return True
    
