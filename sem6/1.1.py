from timeit import timeit


def my_func():
    x = 4
    y = -2
    res = x ** y
    return res

def test_fy_func():
    assert my_func()>0
test_fy_func()




print(f'Результат - {my_func()}')


def my_func2():
    x = 4
    y = -2
    res = 1
    while (y < 0):
        res *= x
        y += 1
    res = 1 / res
    return res


print(f'Результат - {my_func2()}')

print(timeit("my_func()", globals=globals(), number=100000))
print(timeit("my_func2()", globals=globals(), number=100000))

# результат возведения в степень с использованием цикла  достигается быстрей
