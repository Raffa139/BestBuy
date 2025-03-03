class ProductPrice:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError(f"Invalid product price '{value}'")

        self.value = value

    def is_valid(self, value):
        return value >= 0
