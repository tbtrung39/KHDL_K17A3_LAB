def check_input():
    try:
        chuoi = input("Nhập chuỗi: ")
        if len(chuoi) == 2 and chuoi[0] == chuoi[1]:
            raise ValueError("Lỗi nhập liệu!!!")
        for i in range(len(chuoi)-3):
            if chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3]:
                raise ValueError("Lỗi nhập lặp lại!!!")
            if chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3] == chuoi[i+4]:
                raise ValueError("Lỗi nhập trùng lặp!!!")
        if not chuoi.isalpha():
            raise ValueError("Lỗi ký tự!!!")
    except ValueError:
        print("Lỗi nhập liệu!!!")
        print("Lỗi ký tự!!!")
        print("Lỗi nhập lặp lại!!!")
        print("Lỗi nhập trùng lặp!!!")

check_input()