# Пользователь последовательно вводит с клавиатуры числа в консоль. Как только пользователь ввел
# «пустую строку» вывести на экран сумму введенных чисел и завершить работу программы.

Summ = 0
while True:
    try:
        num = float(input('enter number '))
        Summ += num
    except ValueError:
        print("Entered empty or wrong value\nSumm of entered digits = ", Summ)
        break
