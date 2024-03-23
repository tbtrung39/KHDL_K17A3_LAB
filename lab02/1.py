thang = int(input("Nhập vào số tháng (1-12): "))
if thang < 1 or thang > 12:
    print("Tháng không hợp lệ.")
else:
    if thang == 2:
        nam = int(input("Nhập vào năm: "))
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            print(f"Tháng 2 năm {nam} có 29 ngày.")
        else:
            print(f"Tháng 2 năm {nam} có 28 ngày.")
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        print(f"Tháng {thang} có 30 ngày.")
    else:
        print(f"Tháng {thang} có 31 ngày.")
