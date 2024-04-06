chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")

chieu_dai_lon_nhat = 0
vi_tri_cuoi_cung = 0

for i in range(len(chuoi_1)):
    for j in range(len(chuoi_2)):
        chieu_dai = 0
        while (i + chieu_dai < len(chuoi_1) and
               j + chieu_dai < len(chuoi_2) and
               chuoi_1[i + chieu_dai] == chuoi_2[j + chieu_dai]):
            chieu_dai += 1
        if chieu_dai > chieu_dai_lon_nhat:
            chieu_dai_lon_nhat = chieu_dai
            vi_tri_cuoi_cung = i + chieu_dai

vi_tri_bat_dau = vi_tri_cuoi_cung - chieu_dai_lon_nhat
chuoi_con_chung = chuoi_1[vi_tri_bat_dau:vi_tri_cuoi_cung]

print("Chuỗi con chung có độ dài cực đại:", chuoi_con_chung)
