money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0

money_capital_new = money_capital + salary
while money_capital_new > spend:
    month += 1
    money_capital_new = money_capital_new - spend + salary
    spend *= (1+increase)
    if money_capital_new < spend:
        break

print("Количество месяцев, которое можно протянуть без долгов:", month)

