'''
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

company_revenue = int(input("Введите сумму выручки: "))
company_costs = int(input("Введите сумму издержек: "))
# revenue = 456
# costs = 123
if company_revenue > company_costs:
    profit = company_revenue - company_costs
    print(f"Прибыль компании составила: {profit}")
    print(f"Рентабельность выручки составляет: {round(profit / company_revenue * 100, 2)}%")
    employees = int(input("Введите количество сотрудников компании: "))
    print(f"Прибыль компании в рассчёте на одного сотрудника составляет: {round(profit / employees, 2)}")
else:
    print(f"К сожалению компания сейчас находится в убытке {company_revenue - company_costs}")