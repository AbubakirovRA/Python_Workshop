# Вводится целое число, обозначающее код символа по таблице ASCII. Определить, это код английской
# буквы или какой-либо иной символ.
num = int(input("Enter the number "))
if (65 <= num <= 90) or (97 <= num <= 122):
    print("The number", num, "is English letter")
else:
    print("The number", num, "is another symbol")