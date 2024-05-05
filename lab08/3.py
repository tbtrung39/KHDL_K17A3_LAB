def la_so_nguyen_to(so):
    if so <= 1:
        return False
    for i in range(2, so):
        if so % i == 0:
            return False
    return True

def so_nguyen_to_nho_hon_n(n):
    so_nguyen_to = []
    for i in range(2, n):
        if la_so_nguyen_to(i):
            so_nguyen_to.append(i)
    return so_nguyen_to

n = int(input("Nhập số nguyên n: "))

print("Các số nguyên tố nhỏ hơn", n, "là:", so_nguyen_to_nho_hon_n(n))
