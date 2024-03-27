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