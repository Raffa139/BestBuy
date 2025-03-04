import pytest
from src.product import Product
from src.product_name import ProductName
from src.product_price import ProductPrice
from src.product_quantity import ProductQuantity


def test_create_product():
    p = Product(ProductName("Test"), ProductPrice(100), ProductQuantity(10))
    assert p.name.value == "Test"
    assert p.price.value == 100
    assert p.quantity.value == 10
    assert p.is_active()


def test_create_invalid_product():
    with pytest.raises(ValueError):
        Product(ProductName(""), ProductPrice(100), ProductQuantity(10))
        Product(ProductName("Test"), ProductPrice(-100), ProductQuantity(10))
        Product(ProductName("Test"), ProductPrice(100), ProductQuantity(-10))


def test_deactivate_product():
    p = Product(ProductName("Test"), ProductPrice(100), ProductQuantity(10))
    p.buy(ProductQuantity(10))
    assert not p.is_active()


def test_purchase_product():
    p = Product(ProductName("Test"), ProductPrice(100), ProductQuantity(10))
    price = p.buy(ProductQuantity(4))
    assert p.quantity.value == 6
    assert price == 100 * 4

    with pytest.raises(ValueError):
        p.buy(ProductQuantity(10))


if __name__ == '__main__':
    pytest.main()
