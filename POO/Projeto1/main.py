from item import Item
from phone import Phone

# Class Method - Has a relationship to the class, usually used to instantiate objects
Item.instantiate_from_csv()

# Instantiate the Phone Class
phone1 = Phone("jscPhonev10", 500, 5, 1)

# Set phone1 name
phone1.name = "Galaxy"
# Get phone1 name
print(phone1.name)

# Static Method - Has relationship to the class, but is not unique per instance
print(Item.is_integer(7.6))

# Print __repr__ strings
print(Item.instances)
print(Phone.instances)

# Calculate items total price
for instance in Item.instances:
    print(instance.name, instance.calculate_total_price())

# Create new instance attributes
Item.instances[1].has_numpad = False
Item.instances[1].pay_rate = 0.9

# Print Class Attribute
print(Item.pay_rate)
# Print Instance Attribute
print(Item.instances[1].pay_rate)

# Print all class attributes
print(Item.__dict__)
# Print all instance attributes
print(Item.instances[1].__dict__)
print(Item.instances[0].__dict__)

# Apply discount to price
Item.instances[1].apply_discount()
print(Item.instances[1].price)

