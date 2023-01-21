"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
SPISOK=["разработка", "администрирование", "protocol","standard"]
for el in SPISOK:
    print(f"'{el}' преобразуем в байты")
    el_bytes=el.encode("UTF-8")
    print(el_bytes)
    print(f" '{el_bytes}' преобразуем в строку")
    el_str=el_bytes.decode("UTF-8")
    print(el_str)