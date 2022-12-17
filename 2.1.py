from memory_profiler import profile
import copy
import sys
import numpy as np


@profile
def f():
    """создаем список, копируем объект """
    x = list(range(10000))
    y = copy.deepcopy(x)
    return y


@profile
def f1():
    """ Создаем список, копируем объект и удаляем созданный вначале список  """
    x = list(range(10000))
    y = copy.deepcopy(x)
    del x
    return y


@profile
def f2():
    """ Создаем список и отдаем его копию"""
    x = list(range(10000))
    return copy.deepcopy(x)


@profile
def f3():
    """Создаем список, создаем второй список и заполняем его циклом"""
    x = list(range(10000))
    y = list()
    for t in x:
        y.append(t)

    return y




@profile
def f4():
    """ Создаем список циклом и возвращаем его"""
    x = [t for t in range(10000)]
    return x


@profile
def f5():
    """Создаем пустой список и заполняем его циклом"""
    ls = list()
    for i in range(10000):
        ls.append(i)
    return ls


arr = np.array([i for i in range(100)])
arr1 = [i for i in range(100)]
arr2 = (i for i in range(100))
arr3 = {i for i in range(100)}

f()
f1()
f2()
f3()
f4()
f5()

print("Size  = {} bytes".format(sys.getsizeof(f)))
print("Size 1 = {} bytes".format(sys.getsizeof(f1)))
print("Size 2 = {} bytes".format(sys.getsizeof(f2)))
print("Size 3 = {} bytes".format(sys.getsizeof(f3)))
print("Size 4 = {} bytes".format(sys.getsizeof(f4)))
print("Size 5 = {} bytes".format(sys.getsizeof(f5)))

print("Size numpy arr = {} bytes".format(sys.getsizeof(arr)))
print("Size список arr = {} bytes".format(sys.getsizeof(arr1)))
print("Size кортеж arr = {} bytes".format(sys.getsizeof(arr2)))
print("Size словарь arr = {} bytes".format(sys.getsizeof(arr3)))