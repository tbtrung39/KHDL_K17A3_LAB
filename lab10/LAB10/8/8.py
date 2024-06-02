import maTranvuong
n=int(input('Nhập kích thước ma trận vuông: '))
a=maTranvuong.nhap_du_lieu(n)
print(a)
maTranvuong.in_matrix(a)
maTranvuong.ma_tran_chuyen_vi(a)
print(maTranvuong.kiem_tra_doi_xung(a))