from timeit import timeit

print("first")
print(timeit("""for el in count(10):
    if el > 25:
        break
    else:
        print(el)
""", globals=globals(), number=10))

print("second")
print(timeit("""for el in range(10,100):
    if el > 25:
        break
    else:
        print(el)
""", globals=globals(), number=10))

# Вывод 25 значений чисел в интервале от 10  с использованием встроенной функции count проводится  быстрее, чем из интервала с большим значением элементов
