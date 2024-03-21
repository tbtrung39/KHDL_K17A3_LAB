#a
n = int(input("Nhập vào n: "))
tong = 0
if n <=0:
    print("Chương trình kết thúc")
else:
    for i in range (0,n+1):
        tong = tong + i**2
    print("Tổng của dãy S4 là: ",tong) 
#b
n = int(input("Nhập vào n: "))
tong = 0
if n <=0:
    print("Chương trình kết thúc")
else:
    for i in range (0,n+1):
        tong = tong + ((2*i+1)**3)
    print("Tổng của dãy S5 là: ",tong)
#c
n = int(input("Nhập vào n: "))
tong = 0
if n <=0:
    print("Chương trình kết thúc")
else:
    for i in range (0,n+1):
        tong = tong + (2*i)**4
    print("Tổng của dãy S6 là: ",tong)