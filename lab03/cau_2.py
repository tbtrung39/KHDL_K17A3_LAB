n = int(input("Nhập số nguyên dương n: "))
if n <= 2:
    print("Không có số hoàn hảo nhỏ hơn", n)
else:
    print("Các số hoàn hảo nhỏ hơn", n, "là:")
    for num in range(2, n):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        if sum_divisors == num:
            print(num)
