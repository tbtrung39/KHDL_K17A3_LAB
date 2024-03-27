# Câu a
n = int(input('Nhập n: '))
while n <= 0:
    n = int(input("n phải lớn hơn hoặc bằng 0 ! Vui lòng nhập lại n: "))
tong = 0
for i in range(1, n + 1):
    tong += i
print("Tổng của S1 là: ", tong)

# Câu b
n = int(input('Nhập n: '))
while n <= 0:
    n = int(input("n phải lớn hơn hoặc bằng 0 ! Vui lòng nhập lại n: "))
tong = 0
for i in range(1, n + 1, 2):
    tong += i
print("Tổng của S2 là: ", tong)    

# Câu c
n = int(input('Nhập n: '))
while n <= 0:
    n = int(input("n phải lớn hơn hoặc bằng 0 ! Vui lòng nhập lại n: "))
tong = 0
for i in range(2, n + 1, 2):
    tong += i
print("Tổng của S3 là: ", tong)  