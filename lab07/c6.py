n = int(input("Nhập số: "))
if n <0:
    print("Không hợp lệ")
for i in range(1,n):
    if n % i !=0:
        print(i)
