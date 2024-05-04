def main():
    n = int(input("Nhập số phần tử của list: "))
    danh_sach = list(map(lambda x: int(input(f"Nhập phần tử thứ {x + 1}: ")), range(n)))
    binh_phuong = list(map(lambda x: x ** 2, danh_sach))
    print("List gốc:", danh_sach)
    print("List chứa bình phương của các số hạng:", binh_phuong)
if __name__ == "__main__":
    main()
