def tinh_tong_S1(n):
    if n == 1:
        return 1
    return n + tinh_tong_S1(n - 1)
def tinh_tong_S2(n):
    if n == 1:
        return 1
    return n**2 + tinh_tong_S2(n - 1)
def main():
    try:
        n = int(input("Nhập giá trị của n: "))
        if n <= 0:
            raise ValueError("Giá trị của n phải là một số nguyên dương.")
        tong_S1 = tinh_tong_S1(n)
        tong_S2 = tinh_tong_S2(n)
        print(f"Tổng S1 từ 1 đến {n} là: {tong_S1}")
        print(f"Tổng S2 từ 1^2 đến {n}^2 là: {tong_S2}")
    except ValueError as ve:
        print(f"Lỗi: {ve}")
main()