# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# len = input("Enter the number of items in the list ")
# i = 0
# result_list = []
# while i < int(len):
#     print("Enter item №", i)
#     result_list.append(input())
#     i += 1
# print(result_list)

# if int(len) % 2 != 0:
#     removed = result_list.pop()
# result_list[::2], result_list[1::2] = result_list[1::2], result_list[::2]
# if int(len) % 2 != 0:
#     result_list.append(removed)
# print(result_list)

# new_list = list(input("Enter the numbers without space - "))

# for i in range(1, len(new_list), 2):
#     new_list[i-1], new_list[i] = new_list[i], new_list[i-1]

# print(new_list)


# THIRD SOLUTION
# new_list = input("Enter the numbers with space: ").split()
# print("You enter the list: ", new_list)

# idx = len(new_list) if len(new_list) % 2 == 0 else len(new_list)-1 #TypeError: 'str' object is not callable

# new_list[:idx:2], new_list[1:idx:2] = new_list[1:idx:2], new_list[:idx:2]
# print("Changed list: ", new_list)

# FOURTH SOLUTION
user_list = input("Enter the numbers with space: ").split()

for i in range(1, len(user_list), 2):
    user_list.insert(i-1, user_list.pop(i))

print(user_list)