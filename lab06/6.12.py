giao_dich = input("Nhập các giao dịch (cách nhau bằng dấu cách): ").split()

if len(giao_dich) == 0:
    print("Không có giao dịch nào được nhập.")
else:
    tong_tien_gui = 0
    tong_tien_rut = 0

    for i in range(0, len(giao_dich), 2):
        if i + 1 >= len(giao_dich):
            print("Định dạng giao dịch không hợp lệ.")
            break

        if giao_dich[i] == 'D':
            tong_tien_gui += int(giao_dich[i+1])
        elif giao_dich[i] == 'W':
            tong_tien_rut += int(giao_dich[i+1])
        else:
            print("Định dạng giao dịch không hợp lệ.")
            continue

    so_tien_thuc = tong_tien_gui - tong_tien_rut
    print(so_tien_thuc)