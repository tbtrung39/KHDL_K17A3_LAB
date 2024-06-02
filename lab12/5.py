def sum_series_1(n):
    if n < 0:
        raise ValueError("Giá trị n không hợp lệ. Vui lòng nhập một số nguyên không âm.")
    elif n == 0:
        return 0
    else:
        return n + sum_series_1(n - 1)

def sum_series_2(n):
    if n < 0:
        raise ValueError("Giá trị n không hợp lệ. Vui lòng nhập một số nguyên không âm.")
    elif n == 0:
        return 0
    else:
        return n**2 + sum_series_2(n - 1)

try:
    n = int(input("Nhập giá trị n: "))
    result_s1 = sum_series_1(n)
    result_s2 = sum_series_2(n)
    print(f"Tổng S1 từ 1 đến {n} là: {result_s1}")
    print(f"Tổng S2 từ 1 đến {n} là: {result_s2}")
except ValueError:
    print("Lỗi: Giá trị n không hợp lệ. Vui lòng nhập một số nguyên không âm.")
except RecursionError:
    print("Lỗi: Đã xảy ra lỗi tính toán. Vui lòng kiểm tra lại giá trị n.")
