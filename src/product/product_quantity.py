class ProductQuantity:
    """
    Represents the quantity of a product.
    """

    def __init__(self, value):
        """
        Initializes a ProductQuantity object.

        Args:
            value (int): The quantity of the product.

        Raises:
            ValueError: If the provided value is not a valid product quantity.
        """
        if not self.is_valid(value):
            raise ValueError(f"Invalid product quantity '{value}'")

        self.value = value

    def is_valid(self, value):
        """
        Checks if a given value is a valid product quantity.

        Args:
            value (int): The value to check.

        Returns:
            bool: True if the value is valid, False otherwise.
        """
        return value >= 0

    def subtract(self, quantity):
        """
        Subtracts a quantity from the current product quantity.

        Args:
            quantity (ProductQuantity): The quantity to subtract.

        Raises:
            ValueError: If the subtraction would result in a negative quantity.
        """
        if self.value < quantity.value:
            raise ValueError(f"Cannot subtract {quantity.value} from {self.value}")

        self.value -= quantity.value
