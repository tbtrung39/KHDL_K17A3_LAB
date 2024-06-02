def sum_S1(n):
    if n < 1:
        raise ValueError("Giá trị của n phải là số nguyên dương")
    elif n == 1:
        return 1
    else:
        return n + sum_S1(n - 1)
def sum_S2(n):
    if n < 1:
        raise ValueError("Giá trị của n phải là số nguyên dương")
    elif n == 1:
        return 1
    else:
        return n**2 + sum_S2(n - 1)
try:
    n = int(input("Nhập giá trị của n: "))
    S1 = sum_S1(n)
    S2 = sum_S2(n)
    print(f"S1 = {S1}")
    print(f"S2 = {S2}")
except ValueError as ve:
    print(f"Lỗi: {ve}")
except RecursionError:
    print("Lỗi: Quá nhiều lần đệ quy, hãy nhập một giá trị n nhỏ hơn.")
except Exception as e:
    print(f"Lỗi không mong muốn: {e}")
