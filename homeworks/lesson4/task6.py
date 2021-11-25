# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

# from itertools import count, cycle

# print('Программа генерирует целые числа, начиная с указанного. Для генерации следующего числанеобходимо нажать')
# for i in count(int(input('Введите стартовое число:  '))):
#     print(i, end='')
#     quit = input()
#     if quit == 'q':
#         break

# print(
#     'Программа повторяет элементы списка. Для генерации следующего повторения нажать Enter, для выхода из программы - "q"')
# u_list = input('Введите список, разделяя элементы пробелом:  ').split()
# iter-cycle(u_list)
# quit = None

# while quit !='q':
#     print(next(iter), end='')
#     quit=input()

# Вариант решения

# from itertools import count, cycle

# my_count = count(7)
# my_cycle = cycle("ABC")

# for _ in range(5):
#     print("(my_count, my_cycle) = ({},{})".format(next(my_count), next(my_cycle)))


# Вариант решения
# from itertools import islice, cycle, count


# def unexpected(start_el, stop_el, num_str):
#     try:
#         start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
#         my_list = [el for el in islice(count(), start_el, stop_el + 1)]
#         #  repeat_list = [el for el in islice(cucle(my_list), num_str)]
#         r_list = iter(el for el in cycle(my_list))
#         repeat_list = [next(r_list) for _ in range(num_str)]
#         print(my_list)
#         return repeat_list
#     except ValueErrror:
#         return "Value Error"
#     except TypeError:
#         return "TypeError"

# print(unexpected(input("List starting at - "), input("from to - "), input("Number of repetition - ")))