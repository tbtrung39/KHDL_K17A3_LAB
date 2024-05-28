from package_8 import mod1 as md
n = int(input('nhap kich thuoc cua ma tran vuonng:'))
a = md.nhap_du_lieu(n)
print(a)
md.in_matrix(a)
md.ma_tran_chuyen_vi(a)
print(md.kiem_tra_doi_xung(a))