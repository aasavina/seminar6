class Condition:

    def __set__(self, instance, value):
        if type(value) != int :
            raise TypeError(f'Введите цифры')

        if value < 0:
            raise ValueError(f'Введите положительное значение')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    length = Condition()
    width = Condition()

    weight = 30
    thickness = 10

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def material_amount(self):
        res = self.length * self.width * self.weight * self.thickness / 1000
        print(f'нужно {res} тонн асфальта')


a = Road(10, 2000)
a.material_amount()


