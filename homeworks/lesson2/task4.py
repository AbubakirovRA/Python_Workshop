# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_word = input("Enter the string:  ")
string_list = list(user_word.split())
i = 0
while i < len(string_list):
    str = string_list[i]
    print(f"{i}. {str[:10]}")
    i += 1
