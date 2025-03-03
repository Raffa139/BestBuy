from product import Product
from product_name import ProductName
from product_price import ProductPrice
from product_quantity import ProductQuantity


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


def main():
    product_list = [
        Product(ProductName("MacBook Air M2"), ProductPrice(1450), ProductQuantity(100)),
        Product(ProductName("Bose QuietComfort Earbuds"), ProductPrice(250), ProductQuantity(500)),
        Product(ProductName("Google Pixel 7"), ProductPrice(500), ProductQuantity(250))
    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_active_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], ProductQuantity(1)), (products[1], ProductQuantity(2))]))


if __name__ == '__main__':
    main()
