count = 0
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
money = money_capital + salary - spend

while money >= 0:
    money += salary - spend
    spend *= (1 + increase)
    count += 1

count -= 1 # не включая последний месяц
print("Количество месяцев, которое можно протянуть без долгов:", count)


# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов


