import Matranvuong
n=int(input("Nhap kich thuoc cua ma tran (N): "))
print("Nhap ma tran: ")
ma_tran=Matranvuong.nhap_ma_tran(n)
print("Ma tran vua nhap: ")
Matranvuong.in_ma_tran(ma_tran)
print("Ma tran chuyen vi: ")
Matranvuong.in_ma_tran(Matranvuong.chuyen_vi(ma_tran))
if Matranvuong.kiem_tra_doi_xung(ma_tran):
    print("Ma tran doi xung")
else:
    print("Ma tran khong doi xung")