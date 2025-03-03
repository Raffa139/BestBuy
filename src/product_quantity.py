class ProductQuantity:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError(f"Invalid product quantity '{value}'")

        self.value = value

    def is_valid(self, value):
        return value >= 0

    def subtract(self, quantity):
        if self.value < quantity.value:
            raise ValueError(f"Cannot subtract {quantity.value} from {self.value}")

        self.value -= quantity.value
