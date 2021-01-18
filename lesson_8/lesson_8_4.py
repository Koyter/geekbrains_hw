class equipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список - {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, для продолжения - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад - {self.my_store_full}')
            return f'Выход'
        else:
            return equipment.reception(self)


class Printer(equipment):
    def to_print(self):
        return {self.numb}


class Scanner(equipment):
    def to_scan(self):
        return {self.numb}


class Copier(equipment):
    def to_copier(self):
        return {self.numb}


unit_1 = Printer('Принтер', 2500, 1, 12)
unit_2 = Scanner('Сканер', 2000, 5, 11)
unit_3 = Copier('Ксерокс', 1700, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
print(unit_2.to_scan())