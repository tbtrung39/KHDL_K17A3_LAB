def is_triangle(a, b, c):
    # Kiểm tra điều kiện tồn tại của tam giác
    return a + b > c and a + c > b and b + c > a

def calculate_area(a, b, c):
    # Sử dụng công thức Heron để tính diện tích tam giác
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def main():
    try:
        # Nhập độ dài các cạnh tam giác
        a = input("Nhập cạnh a: ")
        b = input("Nhập cạnh b: ")
        c = input("Nhập cạnh c: ")

        # Kiểm tra và chuyển đổi các cạnh sang kiểu float
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except ValueError:
            raise ValueError("Các cạnh tam giác phải là kiểu số.")
        
        # Kiểm tra xem các cạnh có phải là số dương hay không
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Độ dài các cạnh tam giác phải là số dương lớn hơn 0.")
        
        # Kiểm tra xem ba cạnh có tạo thành một tam giác hợp lệ hay không
        if not is_triangle(a, b, c):
            raise ValueError("Ba cạnh không thỏa mãn điều kiện tồn tại của tam giác.")
        
        # Tính diện tích tam giác
        area = calculate_area(a, b, c)
        print(f"Diện tích tam giác là: {area}")

    except ValueError as e:
        print(f"Lỗi: {e}")

    except Exception as e:
        print(f"Lỗi không xác định: {e}")

if __name__ == "__main__":
    main()