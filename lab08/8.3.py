def la_so_nguyen_to(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def in_so_nguyen_to(n):
    for i in range(2, n):
        if la_so_nguyen_to(i):
            print(i, end=" ")

so_n = int(input("Nhập n: "))
print("Các số nguyên tố nhỏ hơn", so_n, "là:")
in_so_nguyen_to(so_n)