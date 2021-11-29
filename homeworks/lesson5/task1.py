# 1. Создать программно файл в текстовом формате, 
# записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных свидетельствует пустая строка.

with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Input new string or empty string to done: ')
        if not line:
            break
        print(line, file=f)

print('Введите данные для записи в файл \nДля окончаниия ввода введите пустую строку')
with open('task_1.txt', 'w', encoding='utf-8') as my_file:
    while (line := input()) !='':
        my_file.write(f"{line}\n")

my_file = open("text_1.txt", 'w', encoding='utf-8')
line = " "
while line:
    line = input("пишите или не пишите!: ")
    my_file.write(f"{line}\n") if line != '' else my_file.close()