giao_dich = input("Nhập các giao dịch: ").split()

tong_tien_gui = 0
tong_tien_rut = 0

for i in range(0, len(giao_dich), 2):
    if giao_dich[i] == 'D':
        tong_tien_gui += int(giao_dich[i+1])
    elif giao_dich[i] == 'W':
        tong_tien_rut += int(giao_dich[i+1])
    else:
        print("Định dạng giao dịch không hợp lệ.")
        break

so_tien_thuc = tong_tien_gui - tong_tien_rut
print(so_tien_thuc)