c =0
def xex(num1, num2):
    global c
    while num1 != 0 and num2 != 0:
        c += 1
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

a = int(input("vvedite cxilo: "))
b = int(input("vvedite chislo: "))

print(xex(a, b), c)
