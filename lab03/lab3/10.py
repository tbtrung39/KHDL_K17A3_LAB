n = int(input("Nhập vào một số nguyên dương: "))
a = []
for i in range(2, n+1):
    for _ in range(i, n+1, i):
        if n % i == 0:
            a.append(i)
            n = n // i
        if n == 1:
            break
    if n == 1:
        break
print("Thừa số nguyên tố của", n, "là:", a)