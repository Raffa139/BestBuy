from .product_name import ProductName
from .product_price import ProductPrice
from .product_quantity import ProductQuantity


class Product:
    """
    Represents a product with a name and price.
    """

    def __init__(self, name, price):
        """
        Initializes a Product object.

        Args:
            name (ProductName): The name of the product.
            price (ProductPrice): The price of the product.
        """
        self.name = name
        self.price = price
        self.active = True

    def is_active(self):
        """
        Checks if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def buy(self, quantity):
        """
        Simulates buying a certain quantity of the product.

        Args:
            quantity (ProductQuantity): The quantity to buy.

        Returns:
            float: The total price of the purchase.
        """
        return self.price.value * quantity.value

    def show(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string containing the product's name and price.
        """
        return f"{self.name.value}, Price: ${self.price.value}"
