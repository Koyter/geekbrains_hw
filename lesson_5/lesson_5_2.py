quantity = 0
with open("somestrings.txt", 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        words = line.split()
        print(f'Число слов в строке: {len(words)}')
        quantity += 1

print(f'Количество строк {quantity}')