n = int(input("Nhập một số nguyên dương n: "))
print("Các số nguyên tố bé hơn hoặc bằng", n, "là:")
for k in range(2, n + 1):
    z = True
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            z = False
            break
    if z:
        print(k)
