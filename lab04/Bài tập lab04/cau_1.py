# Câu a
n = int(input('Nhập n: '))
while n <= 0:
    n = int(input("n phải lớn hơn hoặc bằng 0 ! Vui lòng nhập lại n: "))
i = 1
tong = 0
while i <= n:
    tong += i ** 2
    i += 1
print("Tổng của dãy số là:", tong)

# Câu b
n = int(input('Nhập n: '))
while n <= 0:
    n = int(input("n phải lớn hơn hoặc bằng 0 ! Vui lòng nhập lại n: "))
i = 1
tong = 0
dem = 0  
while dem < n:
    if i % 2 == 1:
        tong += i ** 3
        dem += 1
    i += 1
print("Tổng của dãy số là:", tong)

# Câu c
n = int(input('Nhập n: '))
while n <= 0:
    n = int(input("n phải lớn hơn hoặc bằng 0 ! Vui lòng nhập lại n: "))
i = 1
tong = 0
dem = 0  
while dem < n:
    if i % 2 == 0:
        tong += i ** 4
        dem += 1
    i += 1
print("Tổng của dãy số là:", tong)