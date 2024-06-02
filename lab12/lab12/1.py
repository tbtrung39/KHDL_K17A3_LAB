def tinh_dien_tich_tam_giac(a, b, c):
    # Kiểm tra xem a, b, c có phải là số hay không
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise ValueError("a, b, và c phải là số.")
    # Kiểm tra xem a, b, c có phải là số dương hay không
    if not all(i > 0 for i in [a, b, c]):
        raise ValueError("a, b, và c phải là số dương.")
    # Kiểm tra xem a, b, c có thỏa mãn điều kiện tồn tại tam giác hay không
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("a, b, và c không thỏa mãn điều kiện tồn tại tam giác.")
    # Tính nửa chu vi
    p = (a + b + c) / 2
    # Tính diện tích
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

try:
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))
    print("Diện tích tam giác là:", tinh_dien_tich_tam_giac(a, b, c))
except Exception as e:
    print("Lỗi:", str(e))