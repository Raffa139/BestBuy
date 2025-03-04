class ProductName:
    """
    Represents the name of a product.
    """

    def __init__(self, value):
        """
        Initializes a ProductName object.

        Args:
            value (str): The name of the product.

        Raises:
            ValueError: If the provided value is not a valid product name.
        """
        if not self.is_valid(value):
            raise ValueError(f"Invalid product name '{value}'")

        self.value = value

    def is_valid(self, value):
        """
        Checks if a given value is a valid product name.

        Args:
            value (str): The value to check.

        Returns:
            bool: True if the value is valid, False otherwise.
        """
        return bool(value)
