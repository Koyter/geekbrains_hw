class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                stop = input(f'Введите stop чтобы выйти или введите continue чтобы продолжить - ')

                if stop == 'continue' or stop == 'Continue':
                    print(try_except.my_input())
                elif stop == 'stop' or stop == 'Stop':
                    return f'Вы вышли'

try_except = Error(1)
print(try_except.my_input())