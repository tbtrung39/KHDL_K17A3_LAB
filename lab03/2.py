n = int(input("Nhập số nguyên dương n: "))
if n < 1:
    print("Vui lòng nhập số nguyên dương.")
else:
    print(f"Các số hoàn hảo nhỏ hơn {n}:")
    for number in range(1, n):
        tong = 0
        for i in range(1, number):
            if number % i == 0:
                tong += i
        if tong == number:
            print(number)