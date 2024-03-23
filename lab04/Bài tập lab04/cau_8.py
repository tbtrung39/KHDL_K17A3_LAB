def tinh_tong_chu_so(so):
    tong = 0
    for chu_so in str(so):
        tong += int(chu_so)
    return tong

def main():
    try:
        so = int(input("Nhập vào một số nguyên dương: "))
        if so <= 0:
            print("Vui lòng nhập vào một số nguyên dương.")
        else:
            tong = tinh_tong_chu_so(so)
            print("Tổng các chữ số của số vừa nhập là:", tong)
    except ValueError:
        print("Vui lòng chỉ nhập số nguyên dương.")

if __name__ == "__main__":
    main()
