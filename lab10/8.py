from package import matranvuong as md
n=int(input('nhap kich thuc cua ma tran vuong: '))
a=md.nhap_du_lieu(n)
print(a)
md.in_matrix(a)
md.ma_tran_chuyen_vi(a)
print(md.kiem_tra_doi_xung(a))
