n = int(input("Nhập một số nguyên dương n: "))

if n <= 1:
    print("Không có số nguyên tố nhỏ hơn hoặc bằng", n)
else:
    print("Các số nguyên tố bé hơn hoặc bằng", n, "là:")
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
