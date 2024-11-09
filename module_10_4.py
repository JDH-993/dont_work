from threading import Thread
from random import randint
from time import sleep

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.run()

    def run(self):
        a = randint(1, 10)
        sleep(a)


class Cafe:
    def __init__(self, *args):






# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
# Создание гостей
guests = [Guest(name) for name in guests_names]
print(tables)
print(guests)
# Заполнение кафе столами
#cafe = Cafe(*tables)
# Приём гостей
#cafe.guest_arrival(*guests)
# Обслуживание гостей
#cafe.discuss_guests()
