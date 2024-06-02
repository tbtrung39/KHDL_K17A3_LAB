import package1.Matranvuong as s
N = int(input("Nhập kích thước của ma trận: "))
matran = s.nhap_matran(N)
print("Ma trận vừa nhập:")
s.in_matran(matran)
print("Ma trận chuyển vị:")
s.in_matran(s.tinh_chuyen_vi(matran))
print("Ma trận có đối xứng không?", s.kiem_tra_doi_xung(matran))