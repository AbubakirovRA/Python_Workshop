# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = int(input("Enter your number"))
res = num + (num*10+num)+(num*100+num*10+num)
print("Your number in format n + nn + nnn: ", res)
