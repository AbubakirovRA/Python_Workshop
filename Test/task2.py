# С клавиатуры вводится натуральное число. Найти его наибольшую цифру.
num = int(input("Enter the number "))
max = 0
while num > 0:
    if num % 10 > max:
        max = num % 10
    num = num//10
print ("The largest digit in the number is ", max)