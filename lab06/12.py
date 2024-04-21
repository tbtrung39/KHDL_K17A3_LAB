nhat_ky_giao_dich = []
tien = 0
while True:
    giao_dich = input("Nhập giao dịch (D/W/X để kết thúc): ").strip().upper()
    if giao_dich == 'X':
        break
    for i in giao_dich:
        if i == 'D':
            tien += 100
        if i == 'W':
            tien -= 200
print("Số tiền thực của tài khoản:", tien)