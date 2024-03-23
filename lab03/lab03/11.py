n = int(input("Nhập số hàng của tam giác: "))
#a
for i in range(n-1):
    print(" " *(n-i-1)+"*",end="")
    if i>0:
        print(" " *(2*i-1)+"*", end="")
    print()
print("*" *(2*n-1))
#b
for i in range(n-1):
    print(" " *(n-i-1)+"*", end="")
    if i > 0:
        print(" " *(2*i-1)+"*", end="")
    print()
print("* " *(n-1)+ "*")
#c
for i in range(n+1):
    for j in range(1,n+1-i):
        print("",end= " ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()