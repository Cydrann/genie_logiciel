from datetime import datetime
import re

class Format_devis:

    """
    Méthode de classe qui vérifie les formats pour la création de devis
    """
    @staticmethod
    def format_date(date, format="%Y-%m-%d"):
        try:
            datetime.strptime(date, format)
            return True
        except ValueError:
            return False
            

    @staticmethod
    def format_quantities(quantities):
        try:
            quantities = float(quantities)
            if quantities > 0:
                return True
            else:
                return False
        except ValueError:
            return False


    @staticmethod
    def format_price(price):
        try:
            price = float(price)
            if price > 0:
                return True
            else:
                return False
        except ValueError:
            return False



