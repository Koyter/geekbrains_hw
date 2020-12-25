def wages():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка в час:  '))
        bonus = int(input('Премия:  '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')
    wages()
print(wages())