class DATA:
    def __init__(self, data):
        self.data = str(data)
    @classmethod
    def extract (cls, data):
        my_date = []
        for i in data.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Всё норм'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {DATA.extract(self.data)}'


today = DATA('16 - 01 - 2021')
print(today)
print(DATA.valid(12, 11, 2012))
print(today.valid(18, 13, 2015))
print(DATA.extract('16 - 12 - 2013'))
print(today.extract('16 - 01 - 2021'))
print(DATA.valid(1, 11, 2000))