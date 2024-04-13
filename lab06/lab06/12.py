so_luong_giao_dich = int(input("Nhập số lượng giao dịch: "))
so_tien_thuc = 0
for i in range(so_luong_giao_dich):
    loai_giao_dich = input(f"Nhập loại giao dịch thứ {i+1} (D hoặc W): ")
    so_tien = float(input(f"Nhập số tiền của giao dịch thứ {i+1}: "))
    if loai_giao_dich.upper() == 'D':
        so_tien_thuc += so_tien
    elif loai_giao_dich.upper() == 'W':
        so_tien_thuc -= so_tien
print("Số tiền thực của tài khoản là:", so_tien_thuc)
