from product_name import ProductName
from product_price import ProductPrice
from product_quantity import ProductQuantity


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

    def buy(self, quantity):
        self.quantity.subtract(quantity)
        return self.price.value * quantity.value


def main():
    bose = Product(ProductName("Bose QuietComfort Earbuds"), ProductPrice(250),
                   ProductQuantity(500))
    mac = Product(ProductName("MacBook Air M2"), ProductPrice(1450), ProductQuantity(100))

    print(bose.buy(ProductQuantity(50)))
    print(mac.buy(ProductQuantity(100)))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(ProductQuantity(1000))
    print(bose.show())


if __name__ == '__main__':
    main()
