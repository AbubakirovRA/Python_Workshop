# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

len = input("Enter the number of items in the list ")
i = 0
j = 0
result_list = []
while i < int(len):
    print("Enter item №", i)
    result_list.append(input())
    i += 1
print(result_list)
if int(len) % 2 != 0: removed = result_list.pop()
result_list[::2], result_list[1::2] = result_list[1::2], result_list[::2]
if int(len) % 2 != 0: result_list.append(removed)
print(result_list)
