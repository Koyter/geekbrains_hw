time = int(input("Введите время в секундах: "))

m = (time // 60) % 60
h = str(time // 3600)
s = time % 60
if s<10:
    s = '0'+str(s)
else:
    s = str(s)
if m<10:
    m = '0'+str(m)
else:
    m = str(m)

print(h+ ':' +m+ ':' +s)


