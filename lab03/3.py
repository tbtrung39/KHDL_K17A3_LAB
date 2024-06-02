n = int(input("Nhập số n:"))
z = True
if n <= 1:
    z = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            z = False
            break
if z:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")
    k = 0
    for c in range(n - 1, 1, -1):
        z = True
        for i in range(2, int(c ** 0.5) + 1):
            if c % i == 0:
                z = False
                break
        if z:
            k = c
            break

    print("Số nguyên tố gần nhất với", n, "là:", k)
