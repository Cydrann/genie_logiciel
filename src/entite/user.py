import re

class User:
    def __init__(self, name : str, surname : str, username : str, mobile_phone : str, email : str, 
                 postal_adress : str, company : str, phone : str, password : str):
        self.name = name
        self.surname = surname
        self.username = username
        self.mobile_phone = mobile_phone
        self.email = self._validate_email(email)
        self.postal_adress = postal_adress
        self.company = company
        self.phone = self._validate_mobile_phone(phone)
        self.__password = self._validate_password(password)

    # Fonction pour valider le format de l'@ mail
    def _validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Email is not valid")
        return email
    
    # Fonction pour valider le format du numéro de téléphone
    def _validate_mobile_phone(self, mobile_phone):
        phone_regex = r'^\+?[1-9]\d{1,14}$'  # Format international de téléphone
        if not re.match(phone_regex, mobile_phone):
            raise ValueError("Invalid phone number")
        return mobile_phone

    # Fonction pour valider le mot de passe
    def _validate_password(self, password):
        # Vérifie qu'il y a au moins 8 caractères, une majuscule, une minuscule et un chiffre
        if len(password) < 8 or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password):
            raise ValueError("Password is not strong enough")
        return password

    # Accesseur pour le mot de passe
    def get_password(self):
         return self.__password
    

    def to_dict(self):
            return {
                'name': self.name,
                'surname': self.surname,
                'mobile_phone': self.mobile_phone,
                'email': self.email,
                'postal_adress': self.postal_adress
            }

    # Surcharge de l'opérateur print
    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Phone: {self.mobile_phone}"