from tkinter import *
import os

class Affiche_Inscription(Tk):
    def __init__(self):
        super().__init__()
        self.title("Inscription")
        self.geometry("1280x800")
        self.resizable(False, False)
        self.config(background="#2A2F4F")
        self.utilisateur_connecte = None
        
        self.inscri_folder = os.path.join("src", "png", "inscri") 
        self.button_folder = os.path.join("src", "png", "bouton") 


        self.images = {
            "i_admail": PhotoImage(file=os.path.join(self.inscri_folder, "adresse_mail.png")),
            "i_adpost": PhotoImage(file=os.path.join(self.inscri_folder, "adresse_postale.png")),
            "i_cmdp": PhotoImage(file=os.path.join(self.inscri_folder, "confirme_mdp.png")),
            "i_mdp": PhotoImage(file=os.path.join(self.inscri_folder, "mdp.png")),
            "i_nom": PhotoImage(file=os.path.join(self.inscri_folder, "nom.png")),
            "i_uti": PhotoImage(file=os.path.join(self.inscri_folder, "nom_uti.png")),
            "i_prenom": PhotoImage(file=os.path.join(self.inscri_folder, "prenom.png")),
            "i_telephone": PhotoImage(file=os.path.join(self.inscri_folder, "telephone.png")),
            "i_societe": PhotoImage(file=os.path.join(self.inscri_folder, "societe.png")),
            "i_ok": PhotoImage(file=os.path.join(self.inscri_folder, "ok.png")),
            "i_confirm": PhotoImage(file=os.path.join(self.inscri_folder, "confirmer.png")),
            "fermer": PhotoImage(file=os.path.join(self.button_folder, "close.png"))


        }

        self.afficher_inscription()

    def afficher_inscription(self):
        self.canvas = Canvas(self, width=1280, height=800, bg="#7894a4", highlightthickness=0)

        self.canvas.pack(fill=BOTH, expand=True)

        # scroll
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)  # Windows / Mac
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)  # Linux scroll up
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)  # Linux scroll down

        self.canvas.create_text(640, 50, text="Projet IHM", font=("Arial", 40, "bold"), fill="white", anchor="center")

    # Champs de textes

    
        self.entry_nom = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 115, window=self.entry_nom)

        self.entry_prenom = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 230, window=self.entry_prenom)

        self.entry_adresse_mail = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 345, window=self.entry_adresse_mail)

        self.entry_adresse_postale = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 460, window=self.entry_adresse_postale)

        self.entry_societe = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 575, window=self.entry_societe)

        self.entry_telephone = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 700, window=self.entry_telephone)

        self.entry_nom_utilisateur = Entry(self, font=("Arial", 14), width=25)
        self.canvas.create_window(320, 815, window=self.entry_nom_utilisateur)

        self.entry_mot_de_passe = Entry(self, font=("Arial", 14), width=25, show="*")
        self.canvas.create_window(320, 930, window=self.entry_mot_de_passe)

        self.entry_confirmer_mdp = Entry(self, font=("Arial", 14), width=25, show="*")
        self.canvas.create_window(320, 1045, window=self.entry_confirmer_mdp)



####################""""
        self.canvas.create_image(100, 115, image=self.images["i_nom"], anchor="center")
        self.canvas.create_image(100, 230, image=self.images["i_prenom"], anchor="center")
        self.canvas.create_image(100, 345, image=self.images["i_admail"], anchor="center")
        self.canvas.create_image(100, 460, image=self.images["i_adpost"], anchor="center")
        self.canvas.create_image(100, 575, image=self.images["i_societe"], anchor="center")
        self.canvas.create_image(100, 700, image=self.images["i_telephone"], anchor="center")
        self.canvas.create_image(100, 815, image=self.images["i_uti"], anchor="center")
        self.canvas.create_image(100, 930, image=self.images["i_mdp"], anchor="center")
        self.canvas.create_image(100, 1045, image=self.images["i_cmdp"], anchor="center")
        self.canvas.create_image(100, 1160, image=self.images["i_confirm"], anchor="center")

        # Bouton OK pour tout vailder
        self.bouton_ok = Button(
            self,
            image=self.images["i_ok"],
            compound="center",
            borderwidth=0,
            command=lambda: print("Nom sélectionné")
        )
        self.canvas.create_window(275, 1160, window=self.bouton_ok)


        bouton_fermer = Button(
            self,
            image=self.images["fermer"],
            compound="center",
            bg="#7894a4",
            borderwidth=0,
            command=self.quit)
        self.canvas.create_window(1250, 30, window=bouton_fermer)

        self.canvas.config(scrollregion=(0, 0, 1280, 1500))


    # Molette Windows / Mac
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(event.delta / 120), "units")

    # Molette Linux
    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(-1, "units")


if __name__ == "__main__":
    app = Affiche_Inscription()
    app.mainloop()