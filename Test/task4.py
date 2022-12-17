# Написать функцию, которая определяет количество разрядов введенного целого числа.
def get_num_dig(digit):
    num = 0
    while digit > 0:
        digit //= 10
        num +=1
    return num

digit = int(input("Enter the number "))
print ("The number of digits is ", get_num_dig(digit))