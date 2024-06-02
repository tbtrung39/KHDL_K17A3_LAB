def next_integer(num):
    next_num = num + 1
    return next_num

def main():
    # Nhập số nguyên từ người dùng
    num = int(input("Nhập số nguyên: "))

    # Tính số kế tiếp
    next_num = next_integer(num)

    # Hiển thị số kế tiếp
    print("Số kế tiếp của", num, "là:", next_num)

if __name__ == "__main__":
    main()