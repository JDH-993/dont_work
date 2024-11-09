from fileinput import close
from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

        print(str(self))
    def __str__(self):
        return f"{self.name} , {self.weight} , { self.category}"

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, "w")
        file.close()
    def add(self, *args):
        file = open(self.__file_name, "w")
        file1 = open(self.__file_name, "r")
        print(file1.read())
        for i in range(len(args)):
            with open('products.txt', 'r') as f:
                pprint(f.read())
                if f.read() == f'{args[i]}':
                    print(f'Продукт {args[i]} уже есть в магазине')
            file.write(f'{str(args[i])}\n')

        file.seek(0)

        file.close()
        file1.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

#print(s1.get_products())