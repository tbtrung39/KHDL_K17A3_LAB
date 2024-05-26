import package_c11 as b11
def main():
    print("1. Đổi từ hệ 10 sang hệ 2")
    print("2. Đổi từ hệ 10 sang hệ 16")
    lua_chon = input("Chọn tùy chọn (1/2): ")
    
    if lua_chon == "1":
        n = int(input("Nhập số hệ 10: "))
        ket_qua = b11.doi_tu_he_10_sang_he_2(n)
        print(f"Số {n} trong hệ 2 là: {ket_qua}")
    elif lua_chon == "2":
        n = int(input("Nhập số hệ 10: "))
        ket_qua = b11.doi_tu_he_10_sang_he_16(n)
        print(f"Số {n} trong hệ 16 là: {ket_qua}")
    else:
        print("Lựa chọn không hợp lệ")

if __name__ == "__main__":
    main()