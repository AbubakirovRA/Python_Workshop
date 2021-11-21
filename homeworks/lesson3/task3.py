# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
# и возвращает сумму наибольших двух аргументов.
def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return "Enter only numbers!"



print(my_func(2, 11, -30))


def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3]))
print(my_func(1978, 1, 2))

my_func = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)
print(my_func(8, 7, 9))