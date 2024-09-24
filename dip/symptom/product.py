
class Product:
    def __init__(self, name, price):
        self.product_id = id(self)
        self.name = name
        self.price = price
