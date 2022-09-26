from shopping_cart import ShoppingCart as sc

# Print return annotation - tells what a method should return, but doesn't force the function to return it
print(sc.size.__annotations__['return'])
# Print annotation - tells what a argument should be
print(sc.add.__annotations__['item'])

