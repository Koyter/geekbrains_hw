from itertools import count, cycle

for el in count(int(input('Введите число старта: '))):
    if el == 10:
        break
    print(el)

my_list = [1, 'hello', True, None]
count = 0
for el in cycle(my_list):
    if count >= 10:
        break
    print(el)
    count += 1