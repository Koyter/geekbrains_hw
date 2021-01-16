def summary():
    try:
        with open('numbers_5.txt', 'w+') as f_obj:
            line = input('Введите цифры через пробел \n')
            f_obj.writelines(line)
            numb = line.split()

            print(f'Сумма введённых вами сисле равна {sum(map(int, numb))}')
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()
