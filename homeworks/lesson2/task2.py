# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
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

while j < int(len)//2:
    a = result_list[j*2]
    temp = result_list[j*2]
    b = result_list[j*2+1]
    print(a, b)
    result_list.insert(a, b)
    result_list.insert(b, temp)
    j += 1
print(result_list)
