import copy

from memory_profiler import profile


@profile
def f():
    x = list(range(10000))
    y = copy.deepcopy(x)
    return y


@profile
def f1():
    x = list(range(10000))
    y = copy.deepcopy(x)
    del x
    return y


@profile
def f2():
    x = list(range(10000))
    return copy.deepcopy(x)


@profile
def f3():
    x = list(range(10000))
    y = list()
    for t in x:
        y.append(t)

    return y


f()

# Функция, которая максимально загружает память из представленный выше -f3, остальные загружают одинаково
