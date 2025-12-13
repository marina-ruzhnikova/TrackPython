salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
need_money = 0
time = 0
while months != 0:
    need_money += (spend - salary)
    months -= 1
    time += 1
    spend *= (1+increase)
    if months == 0:
        break
print(f"Подушка безопасности, чтобы протянуть {time} месяцев без долгов:", round(need_money))
