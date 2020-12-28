def division():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    if b == 0:
        b = int(input('Введите другое число отличное от нуля: '))
    res = a / b
    return res

enter = division()
print(enter)
