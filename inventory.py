from product import Product 

class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

inventory=Inventory()
testproduct=Product("P009", "Test", 12000, 15)
inventory.add_product(testproduct)
inventory.display_all()
found = inventory.search_product("P009")
found.display_information()

print(inventory.search_product("P999"))
