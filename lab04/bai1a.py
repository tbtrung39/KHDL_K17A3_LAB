#S4 =1^2 + 2^2 + ... + n^2
n = int(input("Nhập vào số nguyên dương n: "))
tong = 0
i = 1
while n<1:
    n=int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
while i<=n:
    tong +=i**2
    i+=1
print("Tổng của dãy số S4 là: ",tong)    