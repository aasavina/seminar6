"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 4
Введите второе число: 4
1.0

Введите первое число: 4
Введите второе число: 0
Пытаетесь делить на 0!

Введите первое число: 4
Введите второе число: g
Пожалуйста, вводите только числа
"""


def division(first_obj, second_obj):
    try:
        return first_obj*second_obj
    except ZeroDivisionError:
        return "Пытаетесь делить на 0!"

try:
    first_numb = int(input("Введите первое число: "))
    second_numb = int(input("Введите второе число: "))
    print(division(first_numb, second_numb))
except ValueError:
    print("Пожалуйста, вводите только числа")



def assert_na_nol():
    """Сравнение чисел"""
    assert division(first_numb, second_numb)==first_numb/second_numb,"ошибка в функции"


assert_na_nol()