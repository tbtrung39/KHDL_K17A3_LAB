import package1.Matranvuong as t
N = int(input("Nhập kích thước của ma trận: "))
matran = t.nhap_matran(N)
print("Ma trận vừa nhập:")
t.in_matran(matran)
print("Ma trận chuyển vị:")
t.in_matran(t.tinh_chuyen_vi(matran))
print("Ma trận có đối xứng không?", t.kiem_tra_doi_xung(matran))