from tkinter import messagebox

# Classe qui affiche des messages concernant des devis
class Ex_devis:
    """
    Méthode de classe qui permet d'afficher un message d'erreur s'il manque un champ
    durant la création d'un devis
    """
    @staticmethod
    def check_date():
        messagebox.showerror("Champ manquant", "Veuillez entrer la date limite du devis.")

    @staticmethod
    def date_limite():
        messagebox.showerror("Problème de date", "La date limite doit être postérieure ou égal à la date de création.")

    @staticmethod
    def check_order():
        messagebox.showerror("Champ manquant", "Veuillez spécifier au moins un article.")

    @staticmethod
    def check_order_quantities():
        messagebox.showerror("Champ manquant", "Veuillez préciser la quantité de l'article.")

    @staticmethod
    def check_price():
        messagebox.showerror("Champ manquant", "Veuillez préciser le prix de l'article.")

    @staticmethod
    def check_all():
        messagebox.showerror("Erreur", "Veuillez indiquer tous les articles, leurs quantités et le prix.")


    """
    Méthode de classe pour vérifier le format des champs
    Ex: que les articles soient seulement des string
    """
    @staticmethod
    def format_date():
        messagebox.showerror("Format de date", "La date limite doit être au format YYYY/MM/JJ.\nLe mois compris entre 1 et 12\nLe jour compris entre 1 et 31\nExemple : 2025/12/31")

    @staticmethod
    def format_quantities():
        messagebox.showerror("Valeur des quantités des articles", "Veuillez entre une quntitié supérieure à 0 et positive.")

    @staticmethod
    def format_price():
        messagebox.showerror("Valeur du prix", "Veuillez entrer un prix supérieure à 0 et et positive.")


    """
    Méthode de classe qui permet d'afficher un message pour informer que l'on a supprimer un devis
    quand on clique sur le bouton Supprimer dans l'onglet Devis.
    """
    @staticmethod
    def remove_quote(id_devis):
        messagebox.showinfo("Suppression devis", f"Le devis {id_devis} a été supprimé.")


    """
    Méthode de classe pour afficher un message d'erreur quand on fait une recherche et rien ne s'affiche
    """
    @staticmethod
    def search_error():
        messagebox.showerror("Recherche devis", "Aucun résultat ne coresspond à cotre recherche.\nVeuillez réesayer.")



    """
    Méthode de classe pour annoncer que la création du devis a réussi
    """
    @staticmethod
    def quote_succes():
        messagebox.showinfo("Réussite", "Le devis a été crée avec succès.")