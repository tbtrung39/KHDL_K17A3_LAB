def so_nguyen_to(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def in_so_nguyen_to(n):
    for i in range(n):
        if so_nguyen_to(i):
            print(i, end=' ')

n = int(input("Nhập vào một số nguyên: "))
print("Các số nguyên tố nhỏ hơn", n, "là:")
in_so_nguyen_to(n)
