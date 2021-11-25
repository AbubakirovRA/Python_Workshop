# 4. Представлен список чисел. 
# Определить элементы списка, не имеющие повторений. 
# Сформировать итоговый массив чисел, соответствующих требованию. 
# Элементы вывести в порядке их следования в исходном списке. 
# Для выполнения задания обязательно использовать генератор.

# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint

my_list = [randint(-10,10) for _ in range(20)]
# uniq_list = [el for el in my_list if my_list.count(el) == 1] 
# print(f"Source list\n{my_list}\nNo repetition list\n{uniq_list}


print(a := [randint(0, 9) for _ in range(20)], [i for i in a if a.count(i) == 1], sep="\n")

my_dict = {i: 0 for i in my_list}

for i in my_list:
    my_dict[i] +=1


print([i for i in my_dict if my_dict[i] ==1])