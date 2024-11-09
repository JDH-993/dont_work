

first = 'Мама мыла раму'
second = 'Рамена мало было'
a = list(map(lambda x, y: x==y ,first, second))
print(a)

#замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        a = open(file_name, "a", encoding= 'UTF-8')
        for i in range(len(data_set)):
            a.write(f'{str(data_set[i])}\n')
        return
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# метод call
from random import choice

class MysticBall:
    def __init__(self, *args, words = []):
        self.args = args
        self.words = args

    def __call__(self):
        return choice(self.words)


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())