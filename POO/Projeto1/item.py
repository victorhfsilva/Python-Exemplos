import csv


class Item:
    # Class Attribute
    pay_rate = 0.8  # Pay rate after 20% discount
    instances = list()

    def __init__(self, name:str, price: float, quantity:int=0):
        # Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero"
        # Assign arguments to self object
        print(f"A instance of {name} was created.")
        # Instance Attributes and Private Attributes (double underscore)
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        # Append the instance to a list of instances
        Item.instances.append(self)

    # Getters
    @property  # Property = Read-Only Attribute
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    # Setters
    @name.setter
    def name(self, value):
        self.__name = value

    @price.setter
    def price(self, value):
        self.__price = value

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}',{self.__price},{self.__quantity})"

    def calculate_total_price(self):
        return self.__price * self.__quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    # Static Private Method (Abstraction)
    @staticmethod
    def __read_csv(file_name):
        with open(file_name,'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        return items

    # Class Method
    @classmethod
    def instantiate_from_csv(cls):
        items = Item.__read_csv('items.csv')
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    # Static Method
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False