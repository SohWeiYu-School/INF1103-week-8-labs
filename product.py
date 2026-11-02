class Product:

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def update_stock(self, quantity):
        if quantity < 0:
            print("Quantity must be 0 or more")
            return
        self.__stock = quantity

    def get_product_id(self):
        return self.__product_id
        

product1 = Product("P004", "testproduct", 400, 2)
product1.display_information()
product1.update_stock(40)
product1.display_information()

product1.update_stock(-5)
product1.display_information()

print(product1.get_product_id())

