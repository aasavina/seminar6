from timeit import timeit


def my_func():
    x = 4
    y = -2
    res = x ** y
    return res

def test_fy_func():
    assert my_func()>0
test_fy_func()