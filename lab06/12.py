so_du = 0
while True:
    giao_dich = input("Nhập giao dịch: ")
    if not giao_dich:
        break
    loai, so_tien = giao_dich.split()
    so_tien = int(so_tien)
    if loai == 'D':
        so_du += so_tien
    elif loai == 'W':
        so_du -= so_tien

print("Số dư tài khoản là: ", so_du)
