class ProductName:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError(f"Invalid product name '{value}'")

        self.value = value

    def is_valid(self, value):
        return bool(value)
