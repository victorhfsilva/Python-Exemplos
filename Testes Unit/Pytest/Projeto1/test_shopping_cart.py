import pytest
from shopping_cart import ShoppingCart


# Initialize fixture setup
@pytest.fixture
def cart():
    return ShoppingCart(5)


def test_size(cart):
    cart.add("apple")
    assert cart.size() == 1, "The size of the cart don't match."


def test_get_items(cart):
    cart.add("apple")
    assert "apple" in cart.get_items(), "Item is not in the cart."


def test_init_max_items(cart):
    for _ in range(5):
        cart.add("apple")
    # Check if an exception was raised
    with pytest.raises(OverflowError):
        cart.add("apple")


def test_total_price(cart):
    cart.add("orange")
    cart.add("apple")
    price_map ={
        "apple" : 1.0,
        "orange" : 2.0
    }
    assert cart.get_total_price(price_map) == 3.0, "The total price doesn't match."


def test_print_items(cart, capsys):
    cart.add("orange")
    cart.add("apple")
    cart.print_items()
    out, err = capsys.readouterr()
    assert out == "orange\napple\n"
