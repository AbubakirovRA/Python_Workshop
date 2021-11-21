# 6. * Реализовать структуру данных «Товары». 
# Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. 
# В кортеже должно быть два элемента — номер товара и словарь с параметрами 
# (характеристиками товара: название, цена, количество, единица измерения). 
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:

#   [
#   (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#   (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
#   (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#   ]

# Необходимо собрать аналитику о товарах. 
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название, 
# а значение — список значений-характеристик, например список названий товаров.

# Пример:

#   {
#   “название”: [“компьютер”, “принтер”, “сканер”],
#   “цена”: [20000, 6000, 2000],
#   “количество”: [5, 2, 7],
#   “ед”: [“шт.”]
#   }

answer = input("Do you like enter new item's info?")
i = 0
result_list = []
while answer == "y":
    list = []
    list.append(input("Enter Number of Item: "))

    dict_item = {}
    name = (input("Enter Name of Item: "))
    coast = (input("Enter Coast of Item: "))
    quantity = (input("Enter Quantity of Item: "))
    unit = (input("Enter Unit of Item: "))

    dict_items = dict({'название': name, 'цена': coast,
                      'количество': quantity, 'ед.изм.': unit})
    list.append(dict_items)

    result_list.append(list)
    answer = input("Do you like enter new item's info?")
print(result_list)
length=len(result_list)

flag=input("Do You want to see analytical info?")
if flag=="y":
    dict_temp = dict(result_list)
    new_dict = {}
    name_list=[]
    coast_list=[]
    quantity_list=[]
    unit_list=[]
    for key, value in dict_temp.items():
            name_list.append(value['название'])
            coast_list.append(value['цена'])
            quantity_list.append(value['количество'])
            unit_list.append(value['ед.изм.'])
print("Название", name_list)
print("цена", coast_list)
print("количество", quantity_list)
print("ед.изм.", unit_list)