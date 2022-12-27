mas = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = int(input("Введите день: "))
m = int(input("Введите месяц: "))
s = 365
for i in range(0, m - 1):
    s -= mas[i]

print(s - d)
