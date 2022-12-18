# 1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        if TrafficLight.__color[0] == 'Red' and TrafficLight.__color[1] == 'Yellow' and TrafficLight.__color[
            2] == 'Green':
            i = 0
            while i < 3:
                print(TrafficLight.__color[i])
                if i == 0:
                    time.sleep(7)
                elif i == 1:
                    time.sleep(2)
                elif i == 2:
                    time.sleep(7)
                i += 1
        else:
            print("порядок цветов в списке неправильный")


trafficlight = TrafficLight()
trafficlight.running()
