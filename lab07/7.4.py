chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]
so_hoc_sinh=len(chieu_cao)
print("so hoc sinh:", so_hoc_sinh)
chieu_cao_trung_binh = sum(chieu_cao) / so_hoc_sinh
print("chieu cao trung binh: ", chieu_cao_trung_binh)
chieu_cao_nhom=set(chieu_cao)
print("chieu cao cua nhom: ",chieu_cao_nhom)
chieu_cao_trung_binh_nhom = set(chieu_cao)/so_hoc_sinh
print("chieu cao trung binh nhom :", chieu_cao_trung_binh_nhom)