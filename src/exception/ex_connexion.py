from tkinter import messagebox


# Classe qui permet d'afficher un message d'erreur pour la connexion
class Ex_conn:
    @staticmethod
    def display():
        messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.\nVeuillez réessayer.")

    @staticmethod
    def success(username):
        messagebox.showinfo("Succès", f"Bonjour {username}")

    @staticmethod
    def msg_english():
        messagebox.showinfo("Language", "You have switched in english.")

    @staticmethod
    def msg_french():
        messagebox.showinfo("Langue", "Vous êtes passé en français.")
