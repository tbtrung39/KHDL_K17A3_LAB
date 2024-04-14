nhat_ky =[]
print("Nhap nhat ky giao dich(Nhap 'done' de ket thuc): ")
while True:
    giao_dich = input().strip()
    if giao_dich.lower() == 'done':
        break
    nhat_ky.append(giao_dich)

so_tien_thuc = 0
for giao_dich in nhat_ky:
    loai_giao_dich, so_tien = giao_dich.split()
    if loai_giao_dich == "D":
        so_tien_thuc += int(so_tien)
    elif loai_giao_dich =="W":
        so_tien_thuc -= int(so_tien)
print('so tien thuc tai khoan ngan hang la:', so_tien_thuc)                    
