x = int(input("nhập vào một số nguyên x: "))
cosx = 1
while cosx > 0:
    for i in range(1,x+1):
        if i % 2 == 0:
            cosx = -x**2 / ((2*x - 1) * (2*x))
            print(cosx)
    break