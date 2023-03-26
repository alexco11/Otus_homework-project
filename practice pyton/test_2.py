class Product:
    prod_tytpe = None
    def __init__(self, name, price):
        self.name = name
        self._price = float(price)
        self.__qty = 0
 #       self.prod_tytpe = 'Abstract notebook'

    def make_discount(self, pcnt):
        self._price *= (1-pcnt / 100)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = float(value)

    def __str__(self):
        return f'{self.prod_tytpe}: {self._price}'

class Notebook(Product):
    prod_tytpe = 'notebooook'
    pass
class Smartphone(Product):
    prod_tytpe = 'smart'

    def __init__(self, name, price, screen_size):
        super().__init__(name, price)
        self.screen_size = screen_size


prod_1 = Notebook('Macbook', '5500')
prod_2 = Smartphone('Galaxy S', '20000', 6.2)

prod_1.make_discount(5)
prod_2.make_discount(50)

print(type(prod_1), vars(prod_1))
print(type(prod_2), vars(prod_2))

#rod_1.name = 'MacBook Air'
#prod_1.price = '4000'


#print(prod_1.name)
#print(prod_1._price)
#print(prod_1.price)

print(prod_1)
print(prod_2)

#print(vars(prod_1).keys())
#print(vars(Product).keys())

products = [prod_1, prod_2]
for el in products:
    print(el.price)