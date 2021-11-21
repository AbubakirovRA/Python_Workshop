
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list = [1.2, 2, True, "String:", [2, 3]]
i = 0
while i < len(list):
    print(type(list[i]))
    i+=1
# new_list = [(-1+0j), 1, 2.2, True, None, 'String', [3, 4], 
#             (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10}, 
#             frozenset(), range(11), b'twelve', bytearray(b'thirteen'), 
#             zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]

# for i, item in enumerate(new_list, 1):
#         print(f"{i}) {item} - {type(item)}")
