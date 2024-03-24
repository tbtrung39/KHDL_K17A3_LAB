# Câu a
n = int(input('Nhập n: '))
while n <= 0:
    n = int(input("n phải lớn hơn hoặc bằng 0 ! Vui lòng nhập lại n: "))
tong = 0 
for i in range(1, n + 1):
    tong += i ** 2
print("Tổng của S4 là: ", tong)

# Câu b
n = int(input('Nhập n: '))
while n <= 0:
    n = int(input("n phải lớn hơn hoặc bằng 0 ! Vui lòng nhập lại n: "))
tong = 0 
for i in range(1, n + 1, 2):
    tong += i ** 3
print("Tổng của S5 là: ", tong)

# Câu c
n = int(input('Nhập n: '))
while n <= 0:
    n = int(input("n phải lớn hơn hoặc bằng 0 ! Vui lòng nhập lại n: "))
tong = 0 
for i in range(2, n + 1, 2):
    tong += i ** 4
print("Tổng của S6 là: ", tong)
