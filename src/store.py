from product.product import Product
from product.product_quantity import ProductQuantity


class Store:
    """
    Represents a store with a collection of products.
    """

    def __init__(self, products):
        """
        Initializes a Store object.

        Args:
            products (list[Product]): A list of Product objects in the store.
        """
        self.products = products

    def add_product(self, product):
        """
        Adds a product to the store.

        Args:
            product (Product): The Product object to add.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.

        Args:
            product (Product): The Product object to remove.
        """
        self.products.remove(product)

    def get_total_quantity(self):
        """
        Calculates and returns the total quantity of all products in the store.

        Returns:
            int: The total quantity of products.
        """
        return sum([product.quantity.value for product in self.products])

    def get_all_active_products(self):
        """
        Returns a list of all active products in the store.

        Returns:
            list[Product]: A list of active Product objects.
        """
        return [product for product in self.products if product.is_active()]

    def get_product(self, index):
        """
        Retrieves a product from the store by its index.

        Args:
            index (int): The index of the product to retrieve.

        Returns:
            Product or None: The Product object at the given index, or None if the index is invalid.
        """
        if index < 0 or index >= len(self.products):
            return None

        return self.products[index]

    def order(self, shopping_list):
        """
        Processes an order and returns the total payment.

        Args:
            shopping_list (list[tuple[Product, ProductQuantity]]): A list of tuples, where each
            tuple contains a Product object and a ProductQuantity object.

        Returns:
            float: The total payment for the order.
        """
        return sum([product.buy(quantity) for product, quantity in shopping_list])
