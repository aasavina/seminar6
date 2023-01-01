# Задание 3.
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivisionError(Exception):
    def __str__(self):
        return f'не делите на ноль'


class Del:
    def __init__(self, ch, zn):
        self.ch = ch
        self.zn = zn

    def dell(self):
        if self.zn == 0:
            raise ZeroDivisionError
        else:
            return self.ch / self.zn


d = Del(5, 0)
try:
    print(d.dell())
except ZeroDivisionError as exeption:
    print("не делите на ноль")
