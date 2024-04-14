nhat_ky = []
nhap = input("Nhập nhật ký giao dịch (nhập 'OK' để kết thúc):\n")
while nhap != 'OK':
    nhat_ky.append(nhap)
    nhap = input()

so_tien_thuc = 0
for giao_dich in nhat_ky:
    loai_giao_dich, so_tien = giao_dich.split()
    if loai_giao_dich == 'D':
        so_tien_thuc += int(so_tien)
    elif loai_giao_dich == 'W':
        so_tien_thuc -= int(so_tien)

print("Số tiền thực của tài khoản là:", so_tien_thuc)
