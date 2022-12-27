for i in range(100, 1000):
    s = str(i)
    y = int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) ** 3
    if i == y:
        print(i)
