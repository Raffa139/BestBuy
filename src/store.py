class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, prodcut):
        self.products.append(prodcut)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        return sum([product.quantity.value for product in self.products])

    def get_all_active_products(self):
        return [product for product in self.products if product.is_active()]

    def get_product(self, index):
        if index < 0 or index >= len(self.products):
            return None

        return self.products[index]

    def order(self, shopping_list):
        return sum([product.buy(quantity) for product, quantity in shopping_list])
