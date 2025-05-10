from tkinter import messagebox

# Classe qui affiche des messages concernant des factures
class Ex_facture:
    """
    Méthode de classe qui permet d'afficher un message pour informer que l'on a supprimer une facture
    quand on clique sur le bouton Supprimer dans l'onglet Facture.
    """
    @staticmethod
    def remove_receipt(id_facture):
        messagebox.showinfo("Suppression de facture", f"La facture {id_facture} a été supprimé")


    """
    Méthode de classe pour afficher un message quand une facture a été crée
    quand l'utilisateur clique sur le bouton Valider d'un devis
    """
    @staticmethod
    def validate_receipt():
        messagebox.showinfo("Création facture", f"La facture a été créée.")

    
    """
    Méthode de classe pour afficher un message quand la recherche de facture donne rien
    """
    @staticmethod
    def search_error():
        messagebox.showerror("Recherche facture", "Aucun résultat ne coresspond à cotre recherche.\nVeuillez réesayer.")