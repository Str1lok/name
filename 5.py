from random import randint
x1 = (randint(0,7))
y1 = (randint(0,7))
x2 = (randint(0,7))
y2 = (randint(0,7))
print(x1, y1, x2, y2)
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("Совпадают")
else:
    print("Не совпадают")
