n = 5
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print("", end = " ")
    for k in range(1, i+1):
        if(i == n or k == 1 or k == i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()