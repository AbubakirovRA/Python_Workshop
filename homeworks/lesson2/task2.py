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
print(result_list())

while j < int(len)//2:
    result_list.insert(i*2, i*2+1)
    result_list.insert(i*2, temp)
    i += 1
print(result_list)
