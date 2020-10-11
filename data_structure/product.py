class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    # property get and set the value
    #price = property(get_price, set_price)


product = Product(50)
print(product.price)
product.price = 2
