def is_triangle(a, b, c):
    # Kiem tra dieu kien cua tam giac
    return a + b > c and a + c > b and b + c > a

def calculate_area(a, b, c):
    # su dung cong thuc Heron, tinh dien tich tg
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def main():
    try:
        # Nhap do dai cac canh
        a = input("Nhap vao canh a: ")
        b = input("Nhap vao canh b: ")
        c = input("Nhap vao canh c: ")

        # kiem tra va chuyen doi cac canh sang float
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except ValueError:
            raise ValueError("Các cạnh tam giác phải là kiểu số.")

        # Kiem tra xem cac canh co phai la so duong hay khong
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Độ dài các cạnh tam giác phải là số dương lớn hơn 0.")

        # Kiểm tra xem ba cạnh có tạo thành một tam giác hợp lệ hay không
        if not is_triangle(a, b, c):
            raise ValueError("Ba cạnh không thỏa mãn điều kiện tồn tại của tam giác.")

        # Tinh dien tich tam giac
        area = calculate_area(a, b, c)
        print(f"Diện tích tam giác là: {area}")

    except ValueError as e:
        print(f"Lỗi: {e}")

    except Exception as e:
        print(f"Lỗi không xác định: {e}")

if __name__ == "__main__":
    main()