word = input('Введите несколько слов: ').split()
for index, value in enumerate(word):
    print(index, value[:10])
