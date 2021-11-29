# 6. Необходимо создать (не программно) текстовый файл, 
# где каждая строка описывает учебный предмет и наличие лекционных, 
# практических и лабораторных занятий по этому предмету и их количество. 
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
# Вывести словарь на экран.

# Примеры строк файла:

# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:

# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
my_dict = {}
with open("text_6.txt", encoding="utf-8") as fobj:
    for line in fobj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        print(f'{my_dict}')

with open("text_6.txt", 'r', encoding="utf-8") as text_file:
    a = text_file.readlines()
    for s in a:
        new_str = ''.join((i if i in '1234567890' else ' ') for i in s)
        new_2 = [int(1) for i in new_str.split()]
        print(f'{s.split()[0]} {sum(new_2)}')

dic = {}
numbers = '1234567890'
with open("text_6.txt", 'r', encoding="utf-8") as file:
    for line in file:
        head, hours = line.split(":")
        dic[head] = sum(map(int, ''.join([num for num in hours if num in numbers]).split()))
print(dic)

result = {}
with open("text_6.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        lesson_timing = []
        lessons = ([el for el in line.split("")])
        for el in lessons:
            lesson_timing.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(':')[0]] = sum([int(1) for i in lesson_timing if i.isdigit()])
print(result)



