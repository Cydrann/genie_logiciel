import datetime

class Quote:
    def __init__(self, order, order_quantities, limit_date, price):
        if not isinstance(order, list) or not all(isinstance(item, str) for item in order):
            raise ValueError("Order must be a list of strings.")
        
        if not isinstance(order_quantities, list) or not all(isinstance(quantity, int) for quantity in order_quantities):
            raise ValueError("Order quantities must be a list of integers.")
        
        if len(order) != len(order_quantities):  # Vérifie que les listes ont la même longueur
            raise ValueError("Order and order_quantities must have the same length.")
        
        self.order = order
        self.order_quantities = order_quantities
        self.date = datetime.date.today()
        self.limit_date = limit_date
        self.price = price
        self.status = False

    
    def update_status(self):
        if(self.status == False):
            self.status = True
        else:
            self.status = False

    def __str__(self):
        order_str = ", ".join(self.order)  # Crée une liste avec les éléments de la commande
        quantities = ", ".join(map(str, self.order_quantities)) # Crée une liste avec les quantitées des éléments de la commande
        return f"Date création : {self.date}, date limite paiement : {self.limit_date}, commande : {order_str}, quantités : {quantities}"


    