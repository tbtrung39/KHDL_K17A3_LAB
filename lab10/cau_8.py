from package import matranvuong as vd
n=int(input('nhap kich thuc cua ma tran vuong: '))
a=vd.nhap_du_lieu(n)
print(a)
vd.in_matrix(a)
vd.ma_tran_chuyen_vi(a)
print(vd.kiem_tra_doi_xung(a))