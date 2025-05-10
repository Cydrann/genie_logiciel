from tkinter import messagebox
from src.interface.inscription import Affiche_Inscription

# Classe qui permet d'afficher des messages d'erreur sur la page d'inscription
class Ex_inscri:

    """
    Méthode de classe qui affiche un message si un champ est vide
    """
    @staticmethod
    def check_surname():
        messagebox.showerror("Erreur", "Veuillez entrer votre nom.")

    @staticmethod
    def check_name():
        messagebox.showerror("Erreur", "Veuillez entrer votre prénom.")

    @staticmethod
    def check_email():
        messagebox.showerror("Erreur", "Veuillez entrer votre email.")

    @staticmethod
    def check_adress():
        messagebox.showerror("Erreur", "Veuillez entrer votre adresse postale.")
    
    @staticmethod
    def check_company():
        messagebox.showerror("Erreur", "Veuillez entrer votre entreprise.")

    @staticmethod
    def check_phone():
        messagebox.showerror("Erreur", "Veuillez entrer votre numéro de téléphone.")
    
    @staticmethod
    def check_username():
        messagebox.showerror("Erreur", "Veuillez entrer votre nom d'utilisateur.")

    @staticmethod
    def check_password():
        messagebox.showerror("Erreur", "Veuillez entrer votre mot de passe.")


    """
    Méthode de classe qui affiche un message si un champ ne respecte pas le format
    """
    @staticmethod
    def format_surname():
        messagebox.showerror("Format du nom de famille", "Le nom de famille saisi contient des caractères non autorisés.\nVeuillez utiliser uniquement des lettres (A-Z, a-z), des accents, des espaces ou des tirets.")
    
    @staticmethod
    def format_name():
        messagebox.showerror("Format de prénom", "Le prénom saisi contient des caractères non autorisés.\nVeuillez utiliser uniquement des lettres (A-Z, a-z), des accents, des espaces ou des tirets.")

    @staticmethod
    def format_phone():
        messagebox.showerror("Format du numéro de téléphone", "Veuillez entrer un numéro de téléphone au format international valide.\nExemple : +33612345678")

    @staticmethod
    def format_email():
        messagebox.showerror("Format d'adresse email invalide","Veuillez entrer une adresse email valide.\nExemple : nom@example.com")

    @staticmethod
    def format_password():
        messagebox.showerror("Format du mot de passe","Le mot de passe doit contenir au minimum :\n- 8 caractères\n- Une lettre majuscule (A-Z)\n- Une lettre minuscule (a-z)\n- Un chiffre (0-9)")

    """
    Méthode de classe qui envoie un message si le mot de passe n'est pas confirmé
    """
    @staticmethod
    def confirm_password():
        messagebox.showerror("Erreur", "Veuillez confirmer votre mot de passe.")



    """
    Méthode de classe qui affiche un message si un des champs importants est déjà dans la base de données
    (email, username, téléphone, mot de passe)
    """
    @staticmethod
    def already_username():
        messagebox.showerror("Erreur", "Le nom d'utilisateur est déjà pris.")

    @staticmethod
    def already_email():
        messagebox.showerror("Erreur", "L'adresse mail est déjà prise.")

    @staticmethod
    def already_password():
        messagebox.showerror("Erreur", "Le mot de passe est déjà pris.")


    """
    Méthode de classe qui affiche un message de validation quand on crée un compte
    """
    @staticmethod
    def msg_valid():
        messagebox.showinfo("Succès", "Votre compte a été crée avec succès.")
