class ProductPrice:
    """
    Represents the price of a product.
    """

    def __init__(self, value):
        """
        Initializes a ProductPrice object.

        Args:
            value (float or int): The price of the product.

        Raises:
            ValueError: If the provided value is not a valid product price.
        """
        if not self.is_valid(value):
            raise ValueError(f"Invalid product price '{value}'")

        self.value = value

    def is_valid(self, value):
        """
        Checks if a given value is a valid product price.

        Args:
            value (float or int): The value to check.

        Returns:
            bool: True if the value is valid, False otherwise.
        """
        return value >= 0
