# 7. Реализовать генератор с помощью функции с ключевым словом yield, 
# создающим очередное значение. 
# При вызове функции должен создаваться объект-генератор. 
# Функция должна вызываться следующим образом: for el in fact(n). 
# Функция отвечает за получение факториала числа, а в цикле необходимо 
# выводить только первые n чисел, начиная с 1! и до n!.

# Подсказка: факториал числа n — произведение чисел от 1 до n. 
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count
from math import factorial


def fact_gen():
    for el in count(1):
        yield factorial(el)


x =0
for i in fact_gen():
    if x == 15:
        break
    else:
        x +=1
        print(f"Factorial {x} = {i}")

# Вариант решения

def fact_gen(number):
    f_num = 1
    for i in range(number + 1):
        yield f'{i}! = {f_num}'
        f_num += 1 + 1

for el in fact_gen(int(input('Factorial number: '))):
    print(el)
