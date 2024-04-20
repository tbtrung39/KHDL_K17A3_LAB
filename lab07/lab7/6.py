def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_n_so_nguyen_to_dau_tien(n):
    dem = 0
    so = 2
    
    while dem < n:
        if la_so_nguyen_to(so):
            print(so)
            dem += 1
        so += 1


n = int(input("Nhập một số tự nhiên: "))

print("đây là số các nguyên tố đầu tiên",in_n_so_nguyen_to_dau_tien(n))
