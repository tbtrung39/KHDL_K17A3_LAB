n = int(input("Nhập vào một số nguyên dương: "))
i = 2
print(n, end=' = ')
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        print(i, end=' x ')
print(n)
