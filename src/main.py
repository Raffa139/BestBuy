import sys

from product import Product
from product_name import ProductName
from product_price import ProductPrice
from product_quantity import ProductQuantity
from store import Store
from menu import Menu


def list_products(store):
    """
    Lists all active products in the store with their details.

    Args:
        store (Store): The store object.
    """
    for i, product in enumerate(store.get_all_active_products()):
        print(f"{i + 1}. {product.show()}")


def show_total_quantity(store):
    """
    Displays the total quantity of items in the store.

    Args:
        store (Store): The store object.
    """
    print(f"Total of {store.get_total_quantity()} items in store")


def make_order(store):
    """
    Handles the process of making an order from the store.

    This function lists available products, prompts the user for product selection and quantity,
    and then completes the order, displaying the total payment.

    Args:
        store (Store): The store object.
    """
    list_products(store)
    print("\nWhen you want to finish order, enter empty text.")

    shopping_list = []
    while True:
        try:
            product_index = input("Which product # do you want? ")
            quantity = input("What amount do you want? ")

            if not product_index:
                break

            product = store.get_product(int(product_index) - 1)
            product_quantity = ProductQuantity(int(quantity))

            if not product:
                raise ValueError(f"No product for #{product_index} found")

            if not product.has_enough_quantity(product_quantity):
                raise ValueError("Quantity larger than what exists")

            shopping_list.append((product, product_quantity))
            print("\nProduct added to list!\n")
        except ValueError as error:
            print(f"\nError adding product! Details: {error}.\n")

    total_payment = store.order(shopping_list)
    print(f"\nOrder made! Total payment: ${total_payment}")


def start(store):
    """
    Starts the store menu and handles user interactions.

    Args:
        store (Store): The store object.
    """
    menu = Menu("Store Menu")
    menu.add_command("List all products in store", lambda: list_products(store))
    menu.add_command("Show total amount in store", lambda: show_total_quantity(store))
    menu.add_command("Make an order", lambda: make_order(store))
    menu.add_command("Quit", sys.exit)

    menu.run()


def main():
    """
    Initializes the store with products and starts the application.
    """
    product_list = [
        Product(ProductName("MacBook Air M2"), ProductPrice(1450), ProductQuantity(100)),
        Product(ProductName("Bose QuietComfort Earbuds"), ProductPrice(250), ProductQuantity(500)),
        Product(ProductName("Google Pixel 7"), ProductPrice(500), ProductQuantity(250))
    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()
