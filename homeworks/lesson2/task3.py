# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = input("Enter the Month - ")
num = int(month)
list = ["Winter", "Spring", "Summer", "Autumn"]
if num == 1 or num == 2 or num == 12:
    print(list[0])
elif num == 4 or num == 5 or num == 6:
    print(list[1])
elif num == 7 or num == 8 or num == 9:
    print(list[2])
else:
    print(list[3])

dict = {1: "Winter", 2: "Winter", 12: "Winter", 3: "Spring", 4: "Spring", 5: "Spring",
        6: "Summer", 7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn"}
print(dict.pop(int(month)))
