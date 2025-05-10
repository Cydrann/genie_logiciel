from tkinter import *
import os
from i18n import tr, set_langue, LANGUE_ACTIVE

class Affiche_Accueil(Tk):
    def __init__(self):
        super().__init__()
        self.title("Projet Génie Logiciel")
        self.geometry("1280x800")
        self.resizable(False, False)
        self.config(background="#2A2F4F")
        self.utilisateur_connecte = None

        self.button_folder = os.path.join("res", "image")        


        lang = "fr" if LANGUE_ACTIVE == "FR" else "en"

        self.images = {
            "connexion": PhotoImage(file=os.path.join(self.image, "button_1_cyan.png")),
            "mdp": PhotoImage(file=os.path.join(self.image, "button_1_mallow_grand.png")),
            "fermer": PhotoImage(file=os.path.join(self.image, "close_.png")),
            "lock": PhotoImage(file=os.path.join(self.image, "cadenas.png")),
            "explain": PhotoImage(file=os.path.join(self.image, f"explain_screen_{lang}.png")),
            "condi": PhotoImage(file=os.path.join(self.image, f"conditions_button_{lang}.png")),
            "language": PhotoImage(file=os.path.join(self.image, "language_button.png")),
            "help_button": PhotoImage(file=os.path.join(self.image, f"help_{lang}.png")),
            "register_button":PhotoImage(file=os.path.join(self.image, f"register_{lang}.png"))
        }


        self.afficher_connexion()


    def afficher_connexion(self):

        self.canvas = Canvas(self, width=1280, height=800, bg="#2A2F4F", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)

        # scroll
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)  # Windows / Mac
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)  # Linux scroll up
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)  # Linux scroll down


        self.canvas.create_text(640, 50, text="Projet IHM", font=("Arial", 40, "bold"), fill="white", anchor="center")

        self.canvas.create_image(90, 380, image=self.images["connect"], anchor="center")
        self.canvas.create_image(430, 380, image=self.images["lock"], anchor="center")
        self.canvas.create_image(350, 600, image=self.images["explain"], anchor="center")


        self.entry_user = Entry(self, font=("Arial", 14), width=25)
        self.entry_pass = Entry(self, font=("Arial", 14), width=25, show="*")
        self.canvas.create_window(250, 380, window=self.entry_user)
        self.canvas.create_window(600, 380, window=self.entry_pass)


        self.bouton_connexion = Button(
            self,
            image=self.images["connexion"],
            text=tr("Connexion"),
            compound="center",
            font=("Arial", 20),
            bg="#2A2F4F",
            fg="black",
            borderwidth=0)
        self.canvas.create_window(800, 380, window=self.bouton_connexion)


        self.register = Button(
            self,
            image=self.images["register_button"],
            text=" ",
            compound="center",
            font=("Arial", 20),
            bg="#2A2F4F",
            fg="black",
            borderwidth=0)
        self.canvas.create_window(200, 200, window=self.register)

        bouton_fermer = Button(
            self,
            image=self.images["fermer"],
            text=" ",
            compound="center",
            font=("Arial", 20),
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=self.quit)
        self.canvas.create_window(1250, 30, window=bouton_fermer)

        self.language = Button(
            self,
            image=self.images["language"],
            compound="center",
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=self.change_langue
        )
        self.canvas.create_window(1100, 550, window=self.language)

        conditions = Button(
            self,
            image=self.images["condi"],
            compound="center",
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=lambda: print("Conditions"))
        self.canvas.create_window(1100, 660, window=conditions)

        help = Button(
            self,
            image=self.images["help_button"],
            text=" ",
            compound="center",
            font=("Arial", 20),
            bg="#2A2F4F",
            fg="black",
            borderwidth=0,
            command=lambda: print("Aide"))
        self.canvas.create_window(1250, 715, window=help)
    


        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # Molette Windows / Mac
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # Molette Linux
    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

    def change_langue(self):
        from i18n import LANGUE_ACTIVE
        new_lang = "UK" if LANGUE_ACTIVE == "FR" else "FR"
        set_langue(new_lang)
        self.destroy()
        Affiche_Accueil().mainloop()


if __name__ == "__main__":
    app = Affiche_Accueil()
    app.mainloop()
