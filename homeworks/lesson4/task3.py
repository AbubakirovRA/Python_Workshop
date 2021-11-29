# 3. Создать текстовый файл (не программно), 
# построчно записать фамилии сотрудников и величину их окладов. 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., 
# вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.
with open('text_3.txt','r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n' f'Employees with salary less than 20k {[e[8] for e in employees_dict.items() if e[1] < 20000]}')

    def task_3():
        wages = {}
        try:
            with open('task_3.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    wages[line.split()[0]] = float(line.split()[1])
            print('Меньше 20000 получают:')
            for name, wage in wages.items():
                if wage < 20000:
                    print(name)
            print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}') 
        except IOError:
            print('Бухгалтер сбежал с ведомостью. Зарплаты не будет')
        except:
            print('Что-то пошло не так')
task_3()
print('Итого как всегда меньше всех работал и больше всех получает )))')