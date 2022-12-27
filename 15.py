N = int(input("lol: "))
for i in range(1, N + 1):
    s = str(i) # "25"
    y = str(i ** 2) #"625"
    if s == y[len(y) - len(s):]: #"25" == "25"
        print(s)
    
