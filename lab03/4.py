n = int(input("Nhập số n: "))
print("Các số nguyên tố bé hơn hoặc bằng", n, "là:")

for i in range(2, n + 1):
    so_nt = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            so_nt = False
            break
    if so_nt:
        print(i)