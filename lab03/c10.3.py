def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

num = int(input("Nhập vào một số nguyên dương: "))
if num <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    print(f"Dạng phân tích thừa số nguyên tố của {num} là: {prime_factors(num)}")