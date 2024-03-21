#a
n = int(input("Nhập vào n: "))
tong = 0
if n <=0:
    print("Chương trình kết thúc")
else:
    for i in range (0, n+1):
        tong += i
    print("Tổng của dãy số S1 là: ",tong)
#b  
n = int(input("Nhập vào n: "))
tong = 0
if n <=0:
    print("Chương trình kết thúc")
else:
    for i in range (0, n+1):
        tong +=(2*i +1)
    print("Tổng của dãy số S2 là: ",tong)       
# #c
n = int(input)
tong = 0
if n <=0:
    print("Chương trình kết thúc")
else:
    for i in range (0, n+1):
        tong += 2*i
    print("Tổng của dãy số S3 là: ",tong)