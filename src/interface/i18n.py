# i18n.py

        #self.label_bienvenue = Label(self.frame_contenu, 
                                     #text=f"Bienvenue {self.nom_utilisateur}",
                                     #font=("Arial", 16, "bold"), 
                                     #bg="#dddddd", fg="#2A2F4F")
        #self.label_bienvenue.place(x=50, y=30)


        #bienvenue_texte = tr("welcome_user").format(user=self.nom_utilisateur)
        #self.label_bienvenue = Label(
            #self.frame_contenu,
            #text=bienvenue_texte,
            #font=("Arial", 16, "bold"), bg="#dddddd", fg="#2A2F4F")
        #self.label_bienvenue.place(x=50, y=30)               


#######################################

#f"ID: {quote_id} | Client: {client_id} | Date: {date_creation} | Prix: {price:.2f} € | Statut: {'Validé' if status else 'En attente'}"

#statut_texte = tr("status_validated") if status else tr("status_pending")
#texte = tr("devis_ligne").format(
#    id=quote_id,
#    client=client_id,
#    date=date_creation,
#    price=price,
#    status=statut_texte
#)

##########################################

#f"ID: {receipt_id} | Client: {client_id} | Date: {date_creation} | Prix: {price:.2f} €"

#texte = tr("receipt_line").format(
#    id=receipt_id,
#    client=client_id,
#    date=date_creation,
#    price=price
#)

###########################################

#f"ID: {client_id} | Nom: {surname} | Prenom: {name} | Adresse: {address}"

#texte = tr("client_line").format(
#    id=client_id,
#    surname=surname,
#    name=name,
#    address=address
#)

#texte = tr("client_line").format(
#    id=client_id,
#    surname=surname,
#    name=name,
#    address=address
#)

LANGUE_ACTIVE = "FR"

I18N = {
    "FR": {
        "Mes_Devis": "Mes Devis",
        "Mes_Factures": "Mes Factures",
        "Mes_Clients": "Mes Clients",
        "Bienvenue_user": "Bienvenue {user}",
        "Chercher": "Chercher",
        "Nouveau": "Nouveau",
        "Devis": "Devis",
        "Afficher": "Afficher",
        "Valide_verif": "Validé ?",
        "Supprimer": "Supprimer",
        "Info_clients": "Informations clients",
        "Date_Creation": "Date de création :",
        "Date_Paiement": "Date limite de paiement :",
        "Info_Devis": "Informations du devis",
        "Description": "Description",
        "Quantite": "Quantité",
        "Prix": "Prix",
        "Ajouter_Ligne": "Ajouter une ligne",
        "Creer_Devis": "Créer le devis",
        "Factures": "Factures",
        "Carte": "Carte",
        "Clients": "Clients",
        "Infos": "Infos",
        "Facture": "Facture",
        "devis_line": "ID: {id} | Client: {client} | Date: {date} | Prix: {price:.2f} € | Statut: {status}",
        "facture_line": "ID: {id} | Client: {client} | Date: {date} | Prix: {price:.2f} €",
        "client_line": "ID: {id} | Nom: {surname} | Prénom: {name} | Adresse: {address}",
        "nom": "nom",
        "OK": "OK",
        "FACTURE": "FACTURE",
        "Enregistrer_Devis": "Enregistrer Devis",
        "Connexion": "Connexion",
        "Informations_Clients": "Informations clients",
        "Informations_Devis": "Informations du devis"
    },

    "UK": {
        "Mes_Devis": "My Quotes",
        "Mes_Factures": "My Invoices",
        "Mes_Clients": "My Clients",
        "Bienvenue_user": "Welcome {user}",
        "Chercher": "Search",
        "Nouveau": "New",
        "Devis": "Quote",
        "Afficher": "Display",
        "Valide_verif": "Validated?",
        "Supprimer": "Delete",
        "Info_clients": "Client information",
        "Date_Creation": "Creation date:",
        "Date_Paiement": "Payment deadline:",
        "Info_Devis": "Quote information",
        "Description": "Description",
        "Quantite": "Quantity",
        "Prix": "Price",
        "Ajouter_Ligne": "Add line",
        "Creer_Devis": "Create quote",
        "Factures": "Invoices",
        "Carte": "Map",
        "Clients": "Clients",
        "Infos": "Information",
        "Facture": "Invoice",
        "devis_line": "ID: {id} | Client: {client} | Date: {date} | Price: €{price:.2f} | Status: {status}",
        "facture_line": "ID: {id} | Client: {client} | Date: {date} | Price: €{price:.2f}",
        "client_line": "ID: {id} | Last Name: {surname} | First Name: {name} | Address: {address}",
        "nom": "name",
        "OK": "OK",
        "FACTURE": "INVOICE",
        "Enregistrer_Devis": "Save quote",
        "Connexion": "Login",
        "Informations_Clients": "Client information",
        "Informations_Devis": "Quote information"
    }
}

def tr(key):
    return I18N.get(LANGUE_ACTIVE, {}).get(key, key)

def set_langue(code):
    global LANGUE_ACTIVE
    LANGUE_ACTIVE = code
