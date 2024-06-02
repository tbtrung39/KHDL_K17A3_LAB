def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_nho_hon_n(n):
    for i in range(n):
        if so_nguyen_to(i):
            print(i, end=' ')

n=int(input("Nhập một số n: "))
print("Các số nguyên tố nhỏ hơn n là:")
so_nguyen_to_nho_hon_n(n)
