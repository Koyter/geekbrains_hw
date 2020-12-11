profit = float(input("Введите прибыль фирмы: "))
cost = float(input("Введите издержки фирмы: "))

if profit > cost:
    print(f"Фирма работает с приболью. Рентабельность выручки = {profit / cost:.2f}")
    work = int(input("Введите колличество сотрудников: "))
    print(f"Прибыль на одного сотрудника = {profit / work:.2f}")
elif profit == cost:
    print("Фирма работает в ноль")
elif profit < cost:
    print("Фирма работает в убыток")