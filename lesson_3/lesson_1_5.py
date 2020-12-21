def sum ():
    sum_number = 0
    is_exit = False
    while True:
        number = input('Введите последовательности числе: ').split()
        for item in number:
            if item == "$":
                is_exit = True
                break
            if not item.isdigit():
                print(f"Это не число {item}")
                break
            sum_number += int(item)
        print(f"Сумма: {sum_number}")
        if is_exit:
            break
my_funk = sum()

print(my_funk)
