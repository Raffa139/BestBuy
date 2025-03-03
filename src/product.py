class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name.value}, Price: ${self.price.value}, Quantity: {self.quantity.value}"

    def has_enough_quantity(self, quantity):
        return self.quantity.value >= quantity.value

    def buy(self, quantity):
        self.quantity.subtract(quantity)
        return self.price.value * quantity.value
