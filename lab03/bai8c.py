#S3 =2 + 4 + 6 +...+ 2n
n = int(input("Nhập vào n: "))
tong = 0
if n<=0:
    print(n,"không phải là số nguyên dương, vui lòng nhập lại")
else:
    for i in range(1, n+1):
        tong +=2*i
        i+=1
print("Tổng của dãy số S3 là:",tong)            