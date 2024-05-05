def so_nguyen_to(so):
    if so <= 1:
        return False
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            return False
    return True

def so_nguyen_to_n(n):
    nguyen_to = []
    for i in range(2, n):
        if so_nguyen_to(i):
            nguyen_to.append(i)
    return nguyen_to

try:
    limit = int(input("Nhập giới hạn n: "))
    if limit <= 2:
        print("Không có số nguyên tố nào nhỏ hơn", limit)
    else:
        prime_numbers = so_nguyen_to_n(limit)
        print(f"Các số nguyên tố nhỏ hơn {limit} là:", prime_numbers)
except ValueError:
    print("Vui lòng chỉ nhập số nguyên dương.")
