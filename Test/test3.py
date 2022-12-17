# Создать массив из 20 элементов в диапазоне (случайным образом) значений от -15 до 14
# включительно. Определить количество элементов по модулю больших, чем максимальный.

def get_Array():
    import random
    Array = [random.randint(-15, 14) for i in range(20)]
    return Array

def max_elem(Array):
    max  = 0
    for i in Array:
        if i > max:
            max = i
    return max

def num_max_elem(Max_elem, Array):
    num = 0
    for j in Array:
        if abs(j) > Max_elem:
            num += 1
    return num


Array = get_Array()
print('source array: ', Array)

Max_elem = max_elem(Array)
print('maximum: ', Max_elem)

print('the number of elements modulo greater than the maximum: ', num_max_elem(Max_elem, Array))

