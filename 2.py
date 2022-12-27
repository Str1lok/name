mas = [int(input("Введите число:")) for i in range(4)]

if mas[:1] == mas[3:]:
    if mas[1:2] == mas[2:3]:
        print("да")
    else:
        print("no")
else:
    print("нет")
