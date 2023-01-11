class Condition:

    def __set__(self, instance, value):
        if type(value) != str:
            raise TypeError(f'введите тип данных строка')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Car:
    name = Condition()
    color = Condition()

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed


car_1 = Car('Nissan', 'белый', 60)
print(f'{car_1.name} - цвет {car_1.color}')

