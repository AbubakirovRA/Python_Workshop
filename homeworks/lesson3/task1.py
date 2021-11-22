# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) 
# и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
# def div(arg1, arg2):
#     if int(arg2)==0: return "Error"
#     else: return int (arg1)/int (arg2)

# print(div(input("Enter first number - "), input("Enter second - ")))

def div(arg1, arg2):
    try:
        arg1, arg2 = int (arg1), int (arg2)
        div_num = arg1/arg2
    except ValueError:
        return "Error"
    except ZeroDivisionError:
        return "Error /0"
    return round(div_num, 4)

print(div(input("Enter first number - "), input("Enter second - ")))