# 6. Реализовать функцию int_func(), 
# принимающую слово из маленьких латинских букв и возвращающую его же, 
# но с прописной первой буквой. 
# Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. 
# В программу должна попадать строка из слов, разделенных пробелом. 
# Каждое слово состоит из латинских букв в нижнем регистре. 
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
# Необходимо использовать написанную ранее функцию int_func().
def int_func():
    for word in input("Enter words with a space(lower latin script):\n").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - only small English letters!")
int_func()

def int_func(word):
    latin_char = "qwertyuiopasdfghjklzxcvbnm"
    return word.title() if not set(word).difference(latin_char) else False

words = input("Введите строку из слов раделенных пробелом: ").split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')

int_func = lambda word: word.title() if word.islower() and ascii(word)[1:-1].isalpha() else ''
print(' _ '.join(map(int_func, input("Enter phrase: ").split())))
