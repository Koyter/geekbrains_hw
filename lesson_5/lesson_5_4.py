russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open("numbers.txt", 'r', encoding="utf-8") as f_obj:
    for i in f_obj:
        i = i.split(' ', 1)
        new_file.append(russian[i[0]] + '  ' + i[1])
    print(new_file)

with open('numbers_new.txt', 'w', encoding="utf-8") as file_obj_2:
    file_obj_2.writelines(new_file)