salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_expenses = 0
current_spend = spend

for _ in range(months):
    total_expenses += current_spend
    current_spend *= (1 + increase)

total_income = salary * months
money_capital = total_expenses - total_income


money_capital = max(0, round(money_capital))

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")
