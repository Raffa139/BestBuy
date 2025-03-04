from .product import Product
from .product_name import ProductName
from .product_price import ProductPrice
from .product_quantity import ProductQuantity


class StockedProduct(Product):
    """
    Represents a product with a stock quantity, inheriting from Product.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a StockedProduct object.

        Args:
            name (ProductName): The name of the product.
            price (ProductPrice): The price of the product.
            quantity (ProductQuantity): The initial quantity of the product.
        """
        super().__init__(name, price)
        self._quantity = quantity

    @property
    def quantity(self):
        """
        Gets the current quantity of the product.

        Returns:
            ProductQuantity: The quantity of the product.
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of the product.

        Args:
            quantity (ProductQuantity): The new quantity.
        """
        self._quantity = quantity

    def has_enough_quantity(self, quantity):
        """
        Checks if the product has enough quantity to fulfill a purchase.

        Args:
            quantity (ProductQuantity): The requested quantity.

        Returns:
            bool: True if there is enough quantity, False otherwise.
        """
        return self._quantity.value >= quantity.value

    def buy(self, quantity):
        """
        Simulates buying a certain quantity of the product, updating the stock.

        Args:
            quantity (ProductQuantity): The quantity to buy.

        Returns:
            float: The total price of the purchase.
        """
        self._quantity.subtract(quantity)

        if self._quantity.value == 0:
            self.deactivate()

        return self.price.value * quantity.value

    def show(self):
        """
        Returns a string representation of the stocked product.

        Returns:
            str: A string containing the product's name, price, and quantity.
        """
        return f"{self.name.value}, Price: ${self.price.value}, Quantity: {self.quantity.value}"
