import sys

from product import Product
from product_name import ProductName
from product_price import ProductPrice
from product_quantity import ProductQuantity
from store import Store
from menu import Menu


def list_prodcuts(store):
    print("List all products in store")


def show_total_quantity(store):
    print("Show total amount in store")


def make_order(store):
    print("Make an order")


def start(store):
    menu = Menu("Store Menu")
    menu.add_command("List all products in store", lambda: list_prodcuts(store))
    menu.add_command("Show total amount in store", lambda: show_total_quantity(store))
    menu.add_command("Make an order", lambda: make_order(store))
    menu.add_command("Quit", sys.exit)

    menu.run()


def main():
    product_list = [
        Product(ProductName("MacBook Air M2"), ProductPrice(1450), ProductQuantity(100)),
        Product(ProductName("Bose QuietComfort Earbuds"), ProductPrice(250), ProductQuantity(500)),
        Product(ProductName("Google Pixel 7"), ProductPrice(500), ProductQuantity(250))
    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()
