# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
new_list = [1, 5.45, "python", True, [2, 5]]
length = len(new_list)
i = 0
while i < length:
    print("Element №", i," have the type: ", type(new_list[i]))
    i += 1