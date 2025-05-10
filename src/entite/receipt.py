from .quote import Quote

class Receipt(Quote):
    def __init__(self, order, order_quantities, limit_date, price):
        super().__init__(order, order_quantities, limit_date, price)
        self.status = False


    def __str__(self):
        order_str = ", ".join(self.order) 
        quantities = ", ".join(map(str, self.order_quantities))
        return f"Prix : {self.price}, liste commande : {order_str}, quantite : {quantities}"
