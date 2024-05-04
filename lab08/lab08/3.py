def la_so_nguyen_to(m):
    if m <= 1:
        return False
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            return False
    return True
def in_so_nguyen_to(n):
    for i in range(2, n):
        if la_so_nguyen_to(i):
            print(i)
n = int(input("Nhập số nguyên dương n: "))
print("Các số nguyên tố nhỏ hơn", n, "là:")
in_so_nguyen_to(n)
