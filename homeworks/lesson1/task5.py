# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Enter Your Proceeds  "))
costs = int(input("Enter Your Costs  "))
employee = int(input("Enter number of employees  "))

if proceeds > costs:
    print("Result - Profit:  ", proceeds-costs)
    print(f"Profitability:  {((proceeds-costs)/proceeds)}")
    print("Profit per employee:  ", (proceeds-costs)/employee)
else:
    print("Result - Lesion", costs-proceeds)
