input_list_1 = int(input("Введите колличество элементов списка: "))
list_1 = []
a = 0
el = 0
while a < input_list_1:
    list_1.append(int(input("Введите элемент списка: ")))
    a += 1

    for elem in range(int(len(list_1) / 2)):
        list_1[el], list_1[el + 1] = list_1[el + 1], list_1[el]
        el += 2
    print(list_1)
print(list_1)
