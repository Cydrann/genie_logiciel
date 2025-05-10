import re

class Format_inscri:
    """
    Méthodes de classe qui vérifie le format des informations du client
    """
    @staticmethod
    def format_name(name):
        if not isinstance(name, str):
            return False

        pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s\-']+$"
        return bool(re.fullmatch(pattern, name.strip()))


    @staticmethod
    def format_surname(surname):
        if not isinstance(surname, str):
            return False

        pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s\-']+$"
        return bool(re.fullmatch(pattern, surname.strip()))


    @staticmethod
    def format_phone(phone):
        cleaned = re.sub(r"[ \-()]", "", phone)
        phone_regex = r'^\+?[1-9]\d{1,14}$'
        return bool(re.match(phone_regex, cleaned))


    @staticmethod
    def format_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))
    

    @staticmethod
    def format_password(password):
        if (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password)
        ):
            return True
        return False
