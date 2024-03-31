import math
n = int(input("Nhập vào số nguyên dương n: "))
tong = 0
i = 2
while n<2:
    n=int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
while i <=n:
    tong += 1/(math.sqrt(i))
    i+=1
print("Tổng của dãy số S là: ",tong)        