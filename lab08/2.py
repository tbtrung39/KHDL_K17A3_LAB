from math import gcd

def simplify_fraction(numerator, denominator):
    # Tìm ước chung lớn nhất của tử và mẫu
    common_divisor = gcd(numerator, denominator)

    # Rút gọn phân số
    numerator //= common_divisor
    denominator //= common_divisor

    return numerator, denominator

def main():
    # Nhập tử và mẫu của số từ người dùng
    numerator = int(input("Nhập tử số của số phân số: "))
    denominator = int(input("Nhập mẫu số của số phân số: "))

    # Rút gọn phân số
    simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)

    # Hiển thị kết quả
    print("Sau khi rút gọn, phân số là: {}/{}".format(simplified_numerator, simplified_denominator))

if __name__ == "__main__":
    main()
