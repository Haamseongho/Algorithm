from dataclasses import dataclass

@dataclass
class Product:
    weight: int = None
    price: float = None

    def status(self):
        return self.weight / self.price

# apple = Product(50,150.0)
# print(apple.status())

class myClass(object):
    def method_a(self):
        pass
    def method_b(self):
        print('test');