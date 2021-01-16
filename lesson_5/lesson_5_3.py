with open('salary.txt', 'r', encoding="utf-8") as f_obj:
    poor = []
    my_list = f_obj.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) <= 20000:
           poor.append(i[0])
print(f'Оклад меньше 20.000 {poor}')
