money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count = 0  # cчет месяцев

while True:
    money = spend - salary
    if money > money_capital:
        break
    count += 1
    money_capital -= money
    spend = spend * (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", count)
