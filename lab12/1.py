def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def main():
    try:
        a = input('Nhập cạnh a: ')
        b = input('Nhập cạnh b: ')
        c = input('Nhập cạnh c: ')

        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except ValueError:
            raise ValueError('Các cạnh tam giác phải là số.')

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Độ dài các cạnh tam giác phải là số dương.')

        if not is_triangle(a, b, c):
            raise ValueError('Ba cạnh không thỏa mãn điều kiện tồn tại của tam giác.')

        area = calculate_area(a, b, c)
        print(f'Diện tích tam giác là: {area}')

    except ValueError as e:
        print(f'Lỗi: {e}')

    except Exception as e:
        print(f'Lỗi không xác định: {e}')

if __name__ == '__main__':
    main()
