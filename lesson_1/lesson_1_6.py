a = int(input("Введите значение бегуна в первый день, км =  "))
b = int(input("Введите желаемое значение бегуна, км = "))

day = 1
while b - a > 0:
    a = a + (a * 0.1)
    day += 1

print("Бегун достигнет желаемого результата на %.d день" %day)
