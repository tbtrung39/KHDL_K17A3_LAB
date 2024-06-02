def tong_so_n(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n phải là một số nguyên dương.")

    return n * (n + 1) // 2

def tong_binh_phuong_n(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n phải là một số nguyên dương.")

    return n * (n + 1) * (2 * n + 1) // 6

try:
    n = int(input("Nhập n: "))
    tong_1 = tong_so_n(n)
    tong_2 = tong_binh_phuong_n(n)
    print(f"Tổng S1 = 1 + 2 + ... + {n} = {tong_1}")
    print(f"Tổng S2 = 1 + 2^2 + ... + {n}^2 = {tong_2}")
except ValueError as ve:
    print("Lỗi:", ve)
except Exception as e:
    print("Lỗi tính toán:", e)