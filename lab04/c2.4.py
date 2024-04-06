#S = 1 - 1/2 + 1/3 - 1/4 +...
n = int(input("Nhập số nguyên dương n: "))
tong = 0
i = 1
while n<1:
    n=int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
while i<=n:
    if i % 2 ==0:
        tong -= 1/i
    else:
        tong += 1/i
    i+=1
print("Tổng của dãy số S là: ",tong)
#S = 1/2 + 1/(2*3) + 1/ (3*4) +...
n = int(input("Nhập vào số nguyên dương n: "))
tong = 0
i = 1
while n<1:
    n=int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
while i<=n:
    tong += 1/((i)*(i+1))
    i+=1 
print("Tổng của dãy số S là: ",tong)                    