# Создать метакласс для паттерна Синглтон

class MyMetaClass(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyTest(metaclass=MyMetaClass):
    pass


a = MyTest()
b = MyTest()

print('a is b  —', a is b )