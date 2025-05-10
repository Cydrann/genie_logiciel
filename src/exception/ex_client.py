from tkinter import messagebox

# Classe qui affiche des messages concernant les clients
class Ex_client:
    """
    Méthode de classe qui affiche un message si un des champs ou on entre les infos. personnels 
    d'un client ne sont pas remplis pendant la création d'un devis
    """
    @staticmethod
    def check_surname():
        messagebox.showerror("Champ manquant", "Veuillez entrer le nom de famille du client.")

    @staticmethod
    def check_name():
        messagebox.showerror("Champ manquant", "Veuillez entrer le prénom du client.")

    @staticmethod
    def check_phone():
        messagebox.showerror("Champ manquant", "Veuillez entrer le numéro de téléphone du client.")

    @staticmethod
    def check_email():
        messagebox.showerror("Champ manquant", "Veuillez entrer l'adresse mail du client.")

    @staticmethod
    def check_address():
        messagebox.showerror("Champ manquant", "Veuillez entrer l'adresse du client.")


    """
    Méthode de classe qui affiche un message pour indiquer que le format des champs
    pour entrer les informations personnelles du clients sont incorrect
    """
    @staticmethod
    def format_name():
        messagebox.showerror("Format de prénom", "Le prénom saisi contient des caractères non autorisés.\nVeuillez utiliser uniquement des lettres (A-Z, a-z), des accents, des espaces ou des tirets.")

    @staticmethod
    def format_surname():
        messagebox.showerror("Format du nom de famille", "Le nom de famille saisi contient des caractères non autorisés.\nVeuillez utiliser uniquement des lettres (A-Z, a-z), des accents, des espaces ou des tirets.")
    
    @staticmethod
    def format_phone():
        messagebox.showerror("Format du numéro de téléphone", "Veuillez entrer un numéro de téléphone au format international valide.\nExemple : +33612345678")

    @staticmethod
    def format_email():
        messagebox.showerror("Format d'adresse email invalide","Veuillez entrer une adresse email valide.\nExemple : nom@example.com")

    """
    Méthode de classe qui affiche un message si le numéro de téléphone ou bien l'@ mail
    a déjà été utilisé pour un client."""
    @staticmethod
    def already_phone():
        messagebox.showerror("Erreur", "Le numéro de téléphone a déjà été utilisé pour un autre client.")

    @staticmethod
    def already_email():
        messagebox.showerror("Erreur", "L'adresse mail a déjà été utilisé pour un autre client.")

    """
    Méthode de classe qui affiche un message d'erreur si la recherche de client de donne rien
    """
    @staticmethod
    def search_error():
        messagebox.showerror("Recherche client", "Aucun résultat ne coresspond à cotre recherche.\nVeuillez réesayer.")

    """
    Méthode de classe qui affiche un message quand on supprime un client
    de l'onglet Client
    """
    @staticmethod
    def remove_client(id_client):
        messagebox.showinfo("Suppression client",f"Le client {id_client} a été supprimé.")

    
    