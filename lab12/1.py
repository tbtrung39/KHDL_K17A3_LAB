def nhap_canh_tam_giac():
    while True:
        try:
            a = float(input("Nhập độ dài cạnh a: "))
            b = float(input("Nhập độ dài cạnh b: "))
            c = float(input("Nhập độ dài cạnh c: "))
            if a <= 0 or b <= 0 or c <= 0:
                raise ValueError("Độ dài cạnh phải là số dương lớn hơn 0.")
            if a + b <= c or a + c <= b or b + c <= a:
                raise ValueError("Ba cạnh a, b, c không thỏa mãn điều kiện tồn tại tam giác.")
            return a, b, c
        except ValueError as ve:
            print(f"Lỗi: {ve}")
        except Exception as e:
            print(f"Lỗi nhập liệu: {e}")
def tinh_dien_tich_tam_giac(a, b, c):
    s = (a + b + c) / 2
    dien_tich = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return dien_tich
def main():
    a, b, c = nhap_canh_tam_giac()
    dien_tich = tinh_dien_tich_tam_giac(a, b, c)
    print(f"Diện tích của tam giác có các cạnh {a}, {b}, {c} là: {dien_tich:.2f}")
if __name__ == "__main__":
    main()
