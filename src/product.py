from product_name import ProductName
from product_price import ProductPrice
from product_quantity import ProductQuantity


class Product:
    """
    Represents a product in a store.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a Product object.

        Args:
            name (ProductName): The name of the product.
            price (ProductPrice): The price of the product.
            quantity (ProductQuantity): The quantity of the product.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """
        Gets the current quantity of the product.

        Returns:
            ProductQuantity: The quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product.

        Args:
            quantity (ProductQuantity): The new quantity.
        """
        self.quantity = quantity

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

    def show(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string containing the product's name, price, and quantity.
        """
        return f"{self.name.value}, Price: ${self.price.value}, Quantity: {self.quantity.value}"

    def has_enough_quantity(self, quantity):
        """
        Checks if the product has enough quantity to fulfill a purchase.

        Args:
            quantity (ProductQuantity): The requested quantity.

        Returns:
            bool: True if there is enough quantity, False otherwise.
        """
        return self.quantity.value >= quantity.value

    def buy(self, quantity):
        """
        Simulates buying a certain quantity of the product.

        Args:
            quantity (ProductQuantity): The quantity to buy.

        Returns:
            float: The total price of the purchase.
        """
        self.quantity.subtract(quantity)

        if self.quantity.value == 0:
            self.deactivate()

        return self.price.value * quantity.value
