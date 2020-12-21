def extent (b, n):
    if n == 0:
        return 1
    return b*extent(b, n-1)

print(extent(int(input('Введите первое число: ')), int(input('Введите второе число: '))))
