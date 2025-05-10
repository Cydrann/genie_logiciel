from tkinter import *
import shutil
from datetime import datetime
from PIL import Image, ImageTk, ImageGrab
import img2pdf
import os
from PIL import Image, ImageTk, ImageDraw, ImageFont

class Tableau_Acceuil(Tk):
    def __init__(self):
        super().__init__()
        self.title("Accueil post connexion")
        self.geometry("1280x800")
        self.resizable(False, False)
        self.config(background="#2A2F4F")

        self.nom_utilisateur = ""
        self.page_actuelle = None

        """"❌", "✅" """

        self.devis_donnees = [
            ["ID", "Client", "Total", "Date", "Valider"],
            [" ", " ", " ", " ", " "]
        ]

        self.factures_donnees = [
            ["ID", "Client", "Total", "Date"],
            [" ", " ", " ", " "]
        ]

        self.clients_donnees = [
            ["ID", "Nom", "Prénom","Adresse"],
            [" ", " ", " "," "]
        ]
#Aggrandir un peu
        self.infos_donnees = [
            ["Prénom", " "],
            ["Nom", " "],
            ["Adresse mail", " "],
            ["Adresse postale", " "],
            ["Societe", " "],
            ["Numéro de téléphone", " "],
            ["Nom  d'utilisateur", " "]
        ]

        # Page d'acceuil -> canvas + frame scrollable
        self.canvas = Canvas(self, width=1280, height=800, bg="#7894a4")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.frame_contenu = Frame(self.canvas, bg="#7894a4", width=1280, height=800)
        self.canvas.create_window((0, 0), window=self.frame_contenu, anchor="nw")
        self.frame_contenu.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Molette
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)
        
        self.afficher_menu_onglets()


    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(event.delta / 120), "units")
        

    def _on_mousewheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")


#Le problème avec les switch c'est que je risque de superposer plusieurs frame par dessus donc là je supprime et en affiche une etc.. 
#https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame

    def clear_contenu(self):
        for widget in self.frame_contenu.winfo_children():
            widget.destroy()
    
######### ONGLETS #########

    def afficher_menu_onglets(self):

        onglet_devis = Button(
            self,
            text="Mes Devis",
            bg="#2A2F4F",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            command=self.devis
        ).place(x=140, y=167)

        
        onglet_factures = Button(
            self,
            text="Mes Factures",
            bg="#2A2F4F",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            command=self.factures
        ).place(x=320, y=167)

        onglet_clients = Button(
            self,
            text="Mes Clients",
            bg="#2A2F4F",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            command=self.clients
        ).place(x=500, y=167)

        onglet_infos = Button(
            self,
            text="Mes infos",
            bg="#2A2F4F",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            command=self.infos
        ).place(x=680, y=167)

        self.label_bienvenue = Label(self.frame_contenu, 
                                     text=f"Bienvenue {self.nom_utilisateur}",
                                     font=("Arial", 16, "bold"), 
                                     bg="#dddddd", fg="#2A2F4F")
        self.label_bienvenue.place(x=50, y=30)

######### DEVIS ######### 


    def afficher_page_devis(self):
        self.clear_contenu()
        self.page_actuelle = "devis"
        self.afficher_menu_onglets()

        filtres = Frame(self.frame_contenu, bg="#dddddd", bd=2, relief=RIDGE, width=1000, height=80)
        filtres.place(x=140, y=200)
        filtres.pack_propagate(False)

        Button(filtres, text="Chercher", command=self.chercher_devis).pack(side=LEFT, padx=10)
        self.bouton_nouveau = Button(filtres, text="Nouveau", command=self.ajouter_devis)
        self.bouton_nouveau.pack(side=LEFT, padx=10)

        Label(self.frame_contenu, text="Devis", font=("Arial", 16, "bold"), bg="#dddddd", fg="#2A2F4F").place(x=800, y=210)

        table = Frame(self.frame_contenu, bg="#eeeeee", bd=1, relief=SOLID)
        table.place(x=140, y=270, width=1000, height=500)

        for i in range(len(self.devis_donnees)):
            for j in range(len(self.devis_donnees[0])):
                cell = Entry(table, width=18, fg='black', font=('Arial', 12))  
                cell.grid(row=i, column=j)
                cell.insert(END, self.devis_donnees[i][j])  
                cell.config(state="readonly") 

            if i > 1:
                id_devis = self.devis_donnees[i][0]
                bouton_afficher_devis = Button(table, text="Afficher", command=lambda id=id_devis: self.afficher_image_devis(id))
                bouton_afficher_devis.grid(row=i, column=len(self.devis_donnees[0])) 

                bouton_valider_devis = Button(table, text="Valider ", command=lambda id=id_devis: self.valider_devis(id))
                bouton_valider_devis.grid(row=i, column=len(self.devis_donnees[0][1])) 

                bouton_supprimer_devis = Button(table, text="Supprimer", command=lambda id=id_devis: self.supprimer_devis(id))
                bouton_supprimer_devis.grid(row=i, column=len(self.devis_donnees[0][1]) + 2)

    def ajouter_devis(self):
        self.fenetre_devis = Toplevel(self.frame_contenu)
        self.fenetre_devis.title("Nouveau devis")
        self.fenetre_devis.geometry("900x600")
        self.fenetre_devis.resizable(False, False)

        # Informations client
        self.nom = StringVar()
        self.prenom = StringVar()
        self.telephone = StringVar()
        self.email = StringVar()
        self.adresse = StringVar()

        # Dates
        self.date_creation = StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        self.date_limite = StringVar()

        self.lignes_devis = []
        self.total_ht_var = StringVar(value="Total HT : 0.00 €")
        self.total_ttc_var = StringVar(value="Total TTC : 0.00 €")

        self.creer_interface_devis()

    def creer_interface_devis(self):
        Label(self.fenetre_devis, text="Informations clients", font=("Arial", 16, "bold")).pack(pady=10)

        client_frame = Frame(self.fenetre_devis)
        client_frame.pack(pady=10)

        champs = [("Nom", self.nom), ("Prénom", self.prenom), ("Téléphone", self.telephone),
                ("Email", self.email), ("Adresse", self.adresse)]
        for i, (label, var) in enumerate(champs):
            Label(client_frame, text=label + " :").grid(row=i // 2, column=(i % 2) * 2, padx=10)
            Entry(client_frame, textvariable=var, width=30).grid(row=i // 2, column=(i % 2) * 2 + 1, padx=10)

        date_frame = Frame(self.fenetre_devis)
        date_frame.pack(pady=10)

        Label(date_frame, text="Date de création :").pack(side="left", padx=5)
        Entry(date_frame, textvariable=self.date_creation, width=15, state="readonly").pack(side="left")

        Label(date_frame, text="Date limite de paiement :").pack(side="left", padx=10)
        Entry(date_frame, textvariable=self.date_limite, width=15).pack(side="left")

        Label(self.fenetre_devis, text="Informations du devis", font=("Arial", 14, "bold")).pack(pady=10)

        self.canvas_frame = Frame(self.fenetre_devis)
        self.canvas_frame.pack(fill="both", expand=True, pady=10)

        self.canvas = Canvas(self.canvas_frame, height=200)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_devis = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_devis, anchor="nw")

        self.frame_devis.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Entêtes colonnes
        Label(self.frame_devis, text="Description", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=2)
        Label(self.frame_devis, text="Quantité", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10, pady=2)
        Label(self.frame_devis, text="Prix", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10, pady=2)

        self.ajouter_ligne()

        # Totaux
        total_frame = Frame(self.fenetre_devis)
        total_frame.pack(pady=10)

        Label(total_frame, textvariable=self.total_ht_var, font=("Arial", 12, "bold")).pack()
        Label(total_frame, textvariable=self.total_ttc_var, font=("Arial", 12, "bold")).pack()

        bouton_frame = Frame(self.fenetre_devis)
        bouton_frame.pack(pady=15)

        Button(bouton_frame, text="Ajouter une ligne", command=self.ajouter_ligne).grid(row=0, column=0, padx=10)
        self.bouton_creation_devis = Button(bouton_frame, text="Créer le devis", command=self.quitter_page_devis)
        self.bouton_creation_devis.grid(row=0, column=1, padx=10)

    def capturer_devis(self, id_devis):
        # Capture d'écran de toute la zone de l'écran
        screenshot = ImageGrab.grab()  # Sans bbox, cela capture tout l'écran

        # Spécifier le chemin où vous voulez sauvegarder la capture d'écran
        dossier = os.path.join("src", "png", "devis")
        self.button_folder = os.path.join("src", "png", "bouton")

        # Créer le chemin complet du fichier avec le nom de fichier basé sur la date et l'heure
        filename = f"Devis_{id_devis}.png"
        chemin_complet = os.path.join(dossier, filename)

        # Sauvegarder la capture d'écran dans le fichier
        screenshot.save(chemin_complet)
        print(f"✅ Capture d'écran du devis sauvegardée sous : {chemin_complet}")





    def quitter_page_devis(self):
        res = []

        from src.factories.factory_quote import Factory_Quote
        from src.factories.factory_client import Factory_client

        client_data, devis_data = self.recuperer_donnees_devis()
        
        if client_data is None or devis_data is None:
            print("Erreur : données non récupérées.")
            return

        print("=== Données client ===")

        nom = client_data["nom"]
        prenom = client_data["prenom"]
        telephone = client_data["telephone"]
        email = client_data["email"]      
        adresse = client_data["adresse"]
            

        fac1 = Factory_client()

        fac1.create_client(prenom, nom, telephone, email, adresse)
        print("✅ Client généré :", fac1)

        from src.dao.dao_client import Db_Client
        self.db1 = Db_Client()
        self.db1.init_db()
        self.db1.add_client(
            prenom,
            nom,
            telephone, 
            email,
            adresse
        )

        res.append(fac1)

        

        print("\n=== Lignes du devis ===")
        descriptions = []
        quantites = []

        lignes = devis_data["lignes_devis"]

        # Vérifie si aucune ligne de devis n'a été ajoutée

        for ligne in lignes:
            desc = ligne["description"]
            qte = ligne["quantite"]
            prix = ligne["prix"]

            print(f"- {desc} (Quantité: {qte}, Prix: {prix})")

            quantites.append(int(qte))


            descriptions.append(desc)

        


        print("\nCréation du devis avec TVA 10%...\n")

        total_ttc = self.mettre_a_jour_totaux()
        date_limite = devis_data["date_limite"]
            
        
        date_creation = datetime.now().strftime("%Y-%m-%d")
        fac = Factory_Quote()

        fac.create_quote(descriptions, quantites, date_limite, total_ttc)
        print("✅ Devis généré :", fac)

        from src.dao.dao_devis import Db_Devis
        self.db = Db_Devis()
        self.db.init_db()
        self.db.add_quote(
            prenom,
            nom,  
            telephone, 
            email, 
            adresse,
            descriptions,
            quantites,
            date_creation,  # date_creation au format texte
            date_limite,
            total_ttc,
            False  # status initial (non validé)
        )

        res.append(fac)

        devis_id = self.db.get_quote_id(descriptions, quantites, date_limite, total_ttc, datetime.now().strftime("%Y-%m-%d"))

        self.capturer_devis(devis_id)
        

        self.fenetre_devis.destroy()

        from src.exception.ex_devis import Ex_devis
        Ex_devis.quote_succes()

        return res


    def ajouter_ligne(self):
        row = len(self.lignes_devis) + 1
        desc_var = StringVar()
        qte_var = StringVar()
        prix_var = StringVar()

        qte_var.trace_add("write", lambda *args: self.mettre_a_jour_totaux())
        prix_var.trace_add("write", lambda *args: self.mettre_a_jour_totaux())

        Entry(self.frame_devis, textvariable=desc_var, width=40).grid(row=row, column=0, padx=10, pady=2)
        Entry(self.frame_devis, textvariable=qte_var, width=10).grid(row=row, column=1, padx=10, pady=2)
        Entry(self.frame_devis, textvariable=prix_var, width=10).grid(row=row, column=2, padx=10, pady=2)

        self.lignes_devis.append((desc_var, qte_var, prix_var))
        self.mettre_a_jour_totaux()

    def mettre_a_jour_totaux(self):
        total_ht = 0.0
        for _, qte_var, prix_var in self.lignes_devis:
            try:
                quantite = float(qte_var.get())
                prix = float(prix_var.get())
                total_ht += quantite * prix
            except ValueError:
                continue
        total_ttc = total_ht * 1.2
        self.total_ht_var.set(f"Total HT : {total_ht:.2f} €")
        self.total_ttc_var.set(f"Total TTC : {total_ttc:.2f} €")

        return total_ttc

    def recuperer_donnees_devis(self):
        from src.exception.ex_client import Ex_client
        from src.exception.ex_devis import Ex_devis

        from src.dao.dao_client import Db_Client

        from src.format.format_devis import Format_devis
        from src.format.format_client import Format_client

        db = Db_Client()

        if(self.prenom.get().lower() == ""):
            Ex_client.check_name()
            self.fenetre_devis.destroy()
            return None
        
        if(Format_client.format_name(self.prenom.get()) == False):
            Ex_client.format_name()
            self.fenetre_devis.destroy()
            return None
        
        if(self.nom.get().lower() == ""):
            Ex_client.check_surname()
            self.fenetre_devis.destroy()
            return None
        
        if(Format_client.format_surname(self.nom.get()) == False):
            Ex_client.format_surname()
            self.fenetre_devis.destroy()
            return None
        
        if(self.telephone.get() == ""):
            Ex_client.check_phone()
            self.fenetre_devis.destroy()
            return None
        
        if(Format_client.format_phone(self.telephone.get()) == False):
            Ex_client.format_phone()
            self.fenetre_devis.destroy()
            return None
        
        if(db.already_phone(self.telephone.get())):
            Ex_client.already_phone()
            self.fenetre_devis.destroy()
            return None
        
        if(self.email.get().lower() == ""):
            Ex_client.check_email()
            self.fenetre_devis.destroy()
            return None
        
        if(Format_client.format_email(self.email.get()) == False):
            Ex_client.format_email()
            self.fenetre_devis.destroy()
            return None
        
        if(db.already_email(self.email.get())):
            Ex_client.already_email()
            self.fenetre_devis.destroy()
            return None
        
        if(self.adresse.get() == ""):
            Ex_client.check_email()
            self.fenetre_devis.destroy()
            return None
        
        if(self.date_limite.get() == ""):
            Ex_devis.check_date()
            self.fenetre_devis.destroy()
            return None
        
        if(self.date_limite.get() < self.date_creation.get()):
            Ex_devis.date_limite()
            self.fenetre_devis.destroy()
            return None
        
        if(Format_devis().format_date(self.date_limite.get()) == False):
            Ex_devis.format_date()
            self.fenetre_devis.destroy()
            return None
        

        client_data = {
            "nom": self.nom.get(),
            "prenom": self.prenom.get(),
            "telephone": self.telephone.get(),
            "email": self.email.get(),
            "adresse": self.adresse.get()
        }

        devis_data = {
            "date_creation": self.date_creation.get(),
            "date_limite": self.date_limite.get(),
            "lignes_devis": []
        }

        for desc_var, qte_var, prix_var in self.lignes_devis:
            if(len(self.lignes_devis) == 0):
                Ex_devis.check_all()
                self.fenetre_devis.destroy()
                return None
            
            if(desc_var.get() == ""):
                Ex_devis.check_order()
                self.fenetre_devis.destroy()
                return None
            else:
                description = desc_var.get()
           
            if(qte_var.get() == ""):
                Ex_devis.check_order_quantities()
                self.fenetre_devis.destroy()
                return None
            elif(Format_devis().format_quantities(qte_var.get()) == False):
                Ex_devis.format_quantities()
                self.fenetre_devis.destroy()
                return None
            else:
                quantite = float(qte_var.get())

            if(prix_var.get() == ""):
                Ex_devis.check_price()
                self.fenetre_devis.destroy()
                return None
            elif(Format_devis.format_price(prix_var.get()) == False):
                Ex_devis.format_price()
                self.fenetre_devis.destroy()
                return None
            else:
                prix = float(prix_var.get())
        
            devis_data["lignes_devis"].append({
                "description": description,
                "quantite": quantite,
                "prix": prix
            })

        return client_data, devis_data


######### FACTURES #########

    def afficher_page_factures(self):
        self.clear_contenu()
        self.page_actuelle = "factures"
        self.afficher_menu_onglets()

        filtres = Frame(self.frame_contenu, bg="#dddddd", bd=2, relief=RIDGE, width=1000, height=80)
        filtres.place(x=140, y=200)
        filtres.pack_propagate(False)

        Button(filtres, text="Chercher", command=self.chercher_facture).pack(side=LEFT, padx=10)
        Label(self.frame_contenu, text="Factures",font=("Arial", 16, "bold"), bg="#dddddd", fg="#2A2F4F").place(x=800, y=210)
        
        table = Frame(self.frame_contenu, bg="#eeeeee", bd=1, relief=SOLID)
        table.place(x=140, y=270, width=1000, height=500)

        for i in range(len(self.factures_donnees)):
            for j in range(len(self.factures_donnees[0])):
                cell = Entry(table, width=18, fg='black', font=('Arial', 12))  
                cell.grid(row=i, column=j)
                cell.insert(END, self.factures_donnees[i][j])  
                cell.config(state="readonly") 

            if i > 1: #si ya au moins une donnée 
                id_facture = self.factures_donnees[i][0]
                bouton = Button(table, text="Afficher", command=lambda id1=id_facture: self.afficher_image_facture(id1))
                bouton.grid(row=i, column=len(self.factures_donnees[0]))

                bouton_supprimer = Button(table, text="Supprimer", command=lambda id=id_facture: self.supprimer_facture(id))
                bouton_supprimer.grid(row=i, column=len(self.factures_donnees[0][1]))

######### CLIENTS #########

    def afficher_page_clients(self):
        self.clear_contenu()
        self.page_actuelle = "clients"
        self.afficher_menu_onglets()

        filtres = Frame(self.frame_contenu, bg="#dddddd", bd=2, relief=RIDGE, width=1000, height=80)
        filtres.place(x=140, y=200)
        filtres.pack_propagate(False)

        Button(filtres, text="Chercher", command=self.chercher_client).pack(side=LEFT, padx=10)
        Button(filtres, text="Carte", command=self.carte).pack(side=LEFT, padx=10)

        Label(self.frame_contenu, text="Clients",font=("Arial", 16, "bold"), bg="#dddddd", fg="#2A2F4F").place(x=800, y=210)

        table = Frame(self.frame_contenu, bg="#eeeeee", bd=1, relief=SOLID)
        table.place(x=140, y=270, width=1000, height=500)

        for i in range(len(self.clients_donnees)):
            for j in range(len(self.clients_donnees[0])):
                cell = Entry(table, width=18, fg='black', font=('Arial', 12))  
                cell.grid(row=i, column=j)
                cell.insert(END, self.clients_donnees[i][j])  
                cell.config(state="readonly") 

            if i > 1:
                id_client = self.clients_donnees[i][0]

                bouton_supprimer = Button(table, text="Supprimer", command=lambda id=id_client: self.supprimer_client(id))
                bouton_supprimer.grid(row=i, column=len(self.clients_donnees[0]))

######### INFOS #########

    def afficher_page_infos(self):
        self.clear_contenu()
        self.page_actuelle = "infos"
        self.afficher_menu_onglets()

        filtres = Frame(self.frame_contenu, bg="#dddddd", bd=2, relief=RIDGE, width=1000, height=80)
        filtres.place(x=140, y=200)
        filtres.pack_propagate(False)

        Label(self.frame_contenu, text="Infos",font=("Arial", 16, "bold"), bg="#dddddd", fg="#2A2F4F").place(x=800, y=210)

        table = Frame(self.frame_contenu, bg="#eeeeee", bd=1, relief=SOLID)
        table.place(x=140, y=270, width=1000, height=500)

        for i in range(len(self.infos_donnees)):
            for j in range(len(self.infos_donnees[0])):
                cell = Entry(table, width=18, fg='black', font=('Arial', 23))  
                cell.grid(row=i, column=j)
                cell.insert(END, self.infos_donnees[i][j])  
                cell.config(state="readonly") 


######### CLIC SUR UN ONGLETS ######### 

    def devis(self):
        from src.dao.dao_devis import Db_Devis

        self.afficher_page_devis()

        self.db = Db_Devis()
        res = self.db.get_all_quotes_summary()

        self.devis_donnees = [
            ["ID", "Client", "Total", "Date", "Valider"],
            [" ", " ", " ", " ", " "]
        ]

        for quote in res:

            status = "✅" if quote["status"] == 1 else "❌"
            datas = [
                quote["quote_id"],
                quote["client_id"],
                quote["price"],
                quote["date_creation"],
                status 
            ]
            self.devis_donnees.append(datas)
        print("OK def devis")

    def factures(self):
        from src.dao.dao_facture import Db_Facture

        self.afficher_page_factures()

        self.db = Db_Facture()
        res = self.db.get_all_receipt_summary()

        self.factures_donnees = [
            ["ID", "Client", "Total", "Date"],
            [" ", " ", " ", " "]
        ]

        for client in res:
            datas = [
                client["facture_id"],
                client["client_id"],
                client["price"],
                client["date_creation"]
            ]
            self.factures_donnees.append(datas)
        
        print("OK def facture")


    def clients(self):
        from src.dao.dao_client import Db_Client

        self.afficher_page_clients()

        self.db1 = Db_Client()
        res1 = self.db1.get_all_clients_summary()

        self.clients_donnees = [
            ["ID", "Nom", "Prénom","Adresse"],
            [" ", " ", " "," "]
        ]

        for client in res1:
            datas1 = [
                client["client_id"],
                client["surname"],
                client["name"],
                client["address"]
            ]
            self.clients_donnees.append(datas1)

    def infos(self):
        self.afficher_page_infos()


######### GERER LES DONNEES ######### 





######### GERER LES DONNEES DEVIS######### 
    
    def afficher_image_devis(self, id_devis):

        Label(self.frame_contenu, text="Facture", font=("Arial", 16, "bold"), bg="#dddddd", fg="#2A2F4F").place(x=50, y=30)

        # Chemin correct vers l'image
        chemin_image = os.path.join("src", "png", "devis", f"Devis_{id_devis}.png")

        if not os.path.exists(chemin_image):
            print(f"Devis {id_devis} introuvable : {chemin_image}")
            return

        # Ouverture de la fenêtre popup
        popup = Toplevel(self)
        popup.title(f"Devis {id_devis}")
        popup.geometry("600x450")
        popup.configure(bg="#2A2F4F")

        # Ouverture de l'image
        image = Image.open(chemin_image).convert("RGBA")
        image = image.resize((580, 400), Image.LANCZOS)

        # Dessin du texte "FACTURE"
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", size=36)
        except IOError:
            font = ImageFont.load_default()
        

        # Conversion pour Tkinter
        self.image_tk = ImageTk.PhotoImage(image)
        Label(popup, image=self.image_tk, bg="#2A2F4F").pack(pady=20)



    def valider_devis(self, id_devis):
        # Mettre à jour le statut en mémoire
        for devis in self.devis_donnees:
            if devis[0] == id_devis:
                devis[4] = "✅"
                break

        # Mettre à jour en base
        from src.dao.dao_devis import Db_Devis
        db = Db_Devis()
        db.validate_quote(id_devis)
        print(f"Le devis {id_devis} a été validé ✅")

        self.afficher_page_devis()

        # Générer un PDF du devis (sans modification)

        image_path = os.path.abspath(f"src/png/devis/Devis_{id_devis}.png")
        output_folder = os.path.abspath("src/pdf/devis")
        os.makedirs(output_folder, exist_ok=True)

        pdf_path = os.path.join(output_folder, f"Devis_{id_devis}.pdf")
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_path))

        print(f"✅ PDF du devis généré : {pdf_path}")

        
        # Création de la facture à partir du devis
        from src.factories.factory_receipt import Factory_Receipt
        from src.dao.dao_facture import Db_Facture
        from src.exception.ex_facture import Ex_facture
        import ast

        fac = Factory_Receipt()
        devis_datas = db.get_quote_by_id(id_devis)
        order_items = ast.literal_eval(devis_datas["order_items"])
        order_quantities = ast.literal_eval(devis_datas["quantities"])
        fac.create_receipt(order_items, order_quantities, devis_datas["date_limite"], devis_datas["price"])
        print("✅ Facture générée :", fac)

        db2 = Db_Facture()
        db2.init_db()
        db2.add_receipt(
            devis_datas["order_items"], 
            devis_datas["quantities"], 
            devis_datas["date_creation"], 
            devis_datas["date_limite"], 
            devis_datas["price"],
            False)
        
        id_facture = db2.get_receipt_id_by_summary(devis_datas["order_items"],
                                                   devis_datas["quantities"],
                                                   datetime.now().strftime("%Y-%m-%d"),
                                                   devis_datas["date_limite"],
                                                   devis_datas["price"])
        
        Ex_facture.validate_receipt()
        
        from shutil import copyfile

        Label(self.frame_contenu, text="Facture", font=("Arial", 16, "bold"), bg="#dddddd", fg="#2A2F4F").place(x=50, y=30)

        chemin_devis = os.path.join("src", "png", "devis", f"Devis_{id_devis}.png")
        dossier_facture_png = os.path.join("src", "png", "facture")
        dossier_facture_pdf = os.path.join("src", "pdf", "facture")

        if not os.path.exists(chemin_devis):
            print(f"Image du devis {id_devis} introuvable : {chemin_devis}")
            return

        os.makedirs(dossier_facture_png, exist_ok=True)
        os.makedirs(dossier_facture_pdf, exist_ok=True)

        # Chemins complets
        chemin_facture = os.path.join(dossier_facture_png, f"Facture_{id_facture}.png")
        pdf_path = os.path.join(dossier_facture_pdf, f"Facture_{id_facture}.pdf")

        # Copier l'image du devis en facture
        copyfile(chemin_devis, chemin_facture)
        print(f"Facture générée : {chemin_facture}")

        # Enregistrer en PDF
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(os.path.abspath(chemin_facture)))

        print(f"✅ PDF de la facture généré : {pdf_path}")
        

    def supprimer_devis(self, id_devis):
        # Enlever le devis de l'affichage
        for i, devis in enumerate(self.devis_donnees):
            if devis[0] == id_devis:
                self.devis_donnees.pop(i)
                break
            
        # Enlever la facture de la base de données
        from src.dao.dao_devis import Db_Devis
        db = Db_Devis()
        db.remove_quote(id_devis)

        # Affichage du message de suppression
        from src.exception.ex_devis import Ex_devis
        Ex_devis.remove_quote(id_devis)

        print("Devis", id_devis, "supprimé de l'onglet Devis")


    def mise_a_jour_liste_devis(self, champ, listbox):
        from src.dao.dao_devis import Db_Devis
        from src.exception.ex_devis import Ex_devis

        mot_cle = champ.get().strip()
        db_devis = Db_Devis()

        resultats = db_devis.search(mot_cle)
        if(resultats == None):
            Ex_devis.search_error()

        listbox.delete(0, END)

        listbox.ids = []

        for row in resultats:
            quote_id = row["quote_id"]
            client_id = row["client_id"]
            price = row["price"]
            date_creation = row["date_creation"]
            status = row["status"]

            texte = f"ID: {quote_id} | Client: {client_id} | Date: {date_creation} | Prix: {price:.2f} € | Statut: {'Validé' if status else 'En attente'}"
            listbox.insert(END, texte)
            listbox.ids.append(quote_id)


    def chercher_devis(self):
        fenetre_recherche = Toplevel(self)
        fenetre_recherche.title("Recherche de devis")
        fenetre_recherche.geometry("600x400")
        fenetre_recherche.configure(bg="#2A2F4F")
        fenetre_recherche.transient(self)
        fenetre_recherche.grab_set()

        # Champ de texte + bouton OK
        frame_haut = Frame(fenetre_recherche, bg="#2A2F4F")
        frame_haut.pack(pady=10)

        champ_recherche = Entry(frame_haut, font=("Arial", 14), width=40)
        champ_recherche.pack(side=LEFT, padx=5)

        bouton_ok = Button(
            frame_haut,
            text="OK",
            command=lambda: self.mise_a_jour_liste_devis(champ_recherche, listbox)
        )

        bouton_ok.pack(side=LEFT)

        # Frame pour la liste + scrollbar
        frame_liste = Frame(fenetre_recherche, bg="#2A2F4F")
        frame_liste.pack(fill=BOTH, expand=True, padx=10, pady=10)

        scrollbar = Scrollbar(frame_liste)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(frame_liste, font=("Arial", 12), yscrollcommand=scrollbar.set, width=80, height=15)
        listbox.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar.config(command=listbox.yview)
                
######### GERER LES DONNEES FACTURE######### 

    def afficher_image_facture(self, id_facture):
        dossier_facture_png = os.path.join("src", "png", "facture")
        dossier_facture_pdf = os.path.join("src", "pdf", "facture")

        os.makedirs(dossier_facture_png, exist_ok=True)
        os.makedirs(dossier_facture_pdf, exist_ok=True)

        # Chemins complets
        chemin_facture = os.path.join(dossier_facture_png, f"Facture_{id_facture}.png")
        pdf_path = os.path.join(dossier_facture_pdf, f"Facture_{id_facture}.pdf")

        if not os.path.exists(chemin_facture):
            print(f"Image de la facture {id_facture} introuvable : {chemin_facture}")
            return

        # Affichage dans une fenêtre popup
        popup = Toplevel(self)
        popup.title(f"Facture {id_facture}")
        popup.geometry("600x450")
        popup.configure(bg="#2A2F4F")

        image = Image.open(chemin_facture).convert("RGBA")
        image = image.resize((580, 400), Image.LANCZOS)

        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", size=36)
        except IOError:
            font = ImageFont.load_default()
        draw.text((20, 20), "FACTURE", fill="red", font=font)

        self.image_tk = ImageTk.PhotoImage(image)
        Label(popup, image=self.image_tk, bg="#2A2F4F").pack(pady=20)

        # Enregistrer en PDF
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(os.path.abspath(chemin_facture)))

        print(f"✅ PDF de la facture généré : {pdf_path}")



    def supprimer_facture(self, id_facture):
        # Enlever la facture de l'affichage
        for i, facture in enumerate(self.factures_donnees):
            if facture[0] == id_facture:
                self.factures_donnees.pop(i)
                break

        
        # Enlever la facture de la base de données
        from src.dao.dao_facture import Db_Facture
        db = Db_Facture()
        db.remove_receipt(id_facture)

        # Affichage du message de suppression
        from src.exception.ex_facture import Ex_facture
        Ex_facture.remove_receipt(id_facture)

        print("Facture",id_facture,"supprimé de l'onglet Facture")


    def mise_a_jour_liste_facture(self, champ, listbox):
        from src.dao.dao_facture import Db_Facture
        from src.exception.ex_facture import Ex_facture

        mot_cle = champ.get().strip()
        db_devis = Db_Facture()

        resultats = db_devis.search(mot_cle)
        if(resultats == None):
            Ex_facture.search_error()

        listbox.delete(0, END)

        listbox.ids = []

        for row in resultats:
            receipt_id = row["receipt_id"]
            client_id = row["client_id"]
            price = row["price"]
            date_creation = row["date_creation"]

            texte = f"ID: {receipt_id} | Client: {client_id} | Date: {date_creation} | Prix: {price:.2f} €"
            listbox.insert(END, texte)
            listbox.ids.append(receipt_id)


    def chercher_facture(self):
        fenetre_recherche = Toplevel(self)
        fenetre_recherche.title("Recherche de devis")
        fenetre_recherche.geometry("600x400")
        fenetre_recherche.configure(bg="#2A2F4F")
        fenetre_recherche.transient(self)
        fenetre_recherche.grab_set()

        # Champ de texte + bouton OK
        frame_haut = Frame(fenetre_recherche, bg="#2A2F4F")
        frame_haut.pack(pady=10)

        champ_recherche = Entry(frame_haut, font=("Arial", 14), width=40)
        champ_recherche.pack(side=LEFT, padx=5)

        bouton_ok = Button(
            frame_haut,
            text="OK",
            command=lambda: self.mise_a_jour_liste_facture(champ_recherche, listbox)
        )

        bouton_ok.pack(side=LEFT)

        # Frame pour la liste + scrollbar
        frame_liste = Frame(fenetre_recherche, bg="#2A2F4F")
        frame_liste.pack(fill=BOTH, expand=True, padx=10, pady=10)

        scrollbar = Scrollbar(frame_liste)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(frame_liste, font=("Arial", 12), yscrollcommand=scrollbar.set, width=80, height=15)
        listbox.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

######### GERER LES DONNEES CLIENT######### 

    # Fonction pour supprimer un client
    def supprimer_client(self, id_client):
        # Enlever le client de l'affichage
        for i, client in enumerate(self.clients_donnees):
            if client[0] == id_client:
                self.clients_donnees.pop(i)
                break

        # Enlever le client de la base de données
        from src.dao.dao_client import Db_Client
        db = Db_Client()
        db.remove_client(id_client)

        # Affichage du message de suppression
        from src.exception.ex_client import Ex_client
        Ex_client.remove_client(id_client)

        print("Client", id_client, "supprimé de l'onglet Client")


    def mise_a_jour_liste_client(self, champ, listbox):
        from src.dao.dao_client import Db_Client
        from src.exception.ex_client import Ex_client

        mot_cle = champ.get().strip()
        db_devis = Db_Client()

        resultats = db_devis.search(mot_cle)
        if(resultats == None):
            Ex_client.search_error()

        listbox.delete(0, END)

        listbox.ids = []

        for row in resultats:
            client_id = row["client_id"]
            name = row["name"]
            surname = row["surname"]
            address = row["address"]

            texte = f"ID: {client_id} | Nom: {surname} | Prenom: {name} | Adresse: {address}"
            listbox.insert(END, texte)
            listbox.ids.append(client_id)


    def chercher_client(self):
        fenetre_recherche = Toplevel(self)
        fenetre_recherche.title("Recherche de devis")
        fenetre_recherche.geometry("600x400")
        fenetre_recherche.configure(bg="#2A2F4F")
        fenetre_recherche.transient(self)
        fenetre_recherche.grab_set()

        # Champ de texte + bouton OK
        frame_haut = Frame(fenetre_recherche, bg="#2A2F4F")
        frame_haut.pack(pady=10)

        champ_recherche = Entry(frame_haut, font=("Arial", 14), width=40)
        champ_recherche.pack(side=LEFT, padx=5)

        bouton_ok = Button(
            frame_haut,
            text="OK",
            command=lambda: self.mise_a_jour_liste_client(champ_recherche, listbox)
        )

        bouton_ok.pack(side=LEFT)

        # Frame pour la liste + scrollbar
        frame_liste = Frame(fenetre_recherche, bg="#2A2F4F")
        frame_liste.pack(fill=BOTH, expand=True, padx=10, pady=10)

        scrollbar = Scrollbar(frame_liste)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(frame_liste, font=("Arial", 12), yscrollcommand=scrollbar.set, width=80, height=15)
        listbox.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

    # Fonction pour afficher tous les clients sur une carte
    def carte(self):
        from tkinter import Toplevel
        from tkintermapview import TkinterMapView
        from geopy.geocoders import Nominatim
        from src.dao.dao_client import Db_Client

        db = Db_Client()

        # Fenêtre pour la carte
        fenetre_carte = Toplevel(self.master)
        fenetre_carte.title("Carte des clients")
        fenetre_carte.geometry("800x600")

        # Carte initialisée
        map_widget = TkinterMapView(fenetre_carte, width=800, height=600, corner_radius=0)
        map_widget.pack(fill="both", expand=True)

        # Force l'utilisation du tile server d'OpenStreetMap
        map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")

        # Centrer sur Paris
        map_widget.set_position(48.8566, 2.3522)
        map_widget.set_zoom(2)

        # Géocodeur
        geolocator = Nominatim(user_agent="map_client_locator")

        # Récupération des clients
        clients = db.get_all_clients_summary()
        for client in clients:
            adresse = client["address"]
            nom = f'{client["surname"]} {client["name"]}'

            try:
                location = geolocator.geocode(adresse)
                if location:
                    marker = map_widget.set_marker(location.latitude, location.longitude, text=nom)
                    marker.drag_disabled = True  # Désactive le déplacement (au cas où)
                    print(f"✅ {nom} localisé à {location.latitude}, {location.longitude}")
                else:
                    print(f"❌ Adresse non trouvée pour {nom} : {adresse}")
            except Exception as e:
                print(f"⚠️ Erreur pour {nom} ({adresse}) : {e}")

    
    


if __name__ == "__main__":
    app = Tableau_Acceuil()
    app.mainloop()