n = int(input("nhập số nguyên dương n là: "))

for num in range(2, n):
    if sum(i for i in range(1, num) if num % i == 0) == num:
        print(num)