c = 0
while (x := input("vedite chislo: ")) != "0":
    if len(x) == 2:
        if x[-1] == "3":
            c += 1
print("Кол-во двузначных чисел оканчивающихся на 3 = ",c)
