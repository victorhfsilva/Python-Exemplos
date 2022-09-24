from item import Item


# Inheritance
class Phone(Item):

    instances = []

    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones: int = 0):
        # Super Function
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal than zero"
        self.broken_phones = broken_phones

        Phone.instances.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity},{self.broken_phones})"
