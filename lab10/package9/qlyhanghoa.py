
class MatHang:
    def __init__(self, ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong):
        self.ma_hang=ma_hang
        self.ten_hang=ten_hang
        self.don_vi_tinh=don_vi_tinh
        self.don_gia=don_gia
        self.so_luong=so_luong
        self.thanh_tien=don_gia*so_luong
        self.thue_vat=self.thanh_tien*0.1
    def ___str__(self):
        return f"{self.ma_hang}, {self.ten_hang}, {self.don_vi_tinh}, {self.don_gia}, {self.so_luong}, {self.thanh_tien}, {self.thue_vat}"
def nhap_thong_tin():
    ma_hang=input("Ma hang (4 ky tu): ")
    ten_hang=input("Ten hang: ")
    don_vi_tinh=input("Don vi tinh: ")
    don_gia=float(input("Don gia: "))
    so_luong=int(input("So luong: "))
    return MatHang(ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong)
def nhap_danh_sach_mat_hang():
    return [nhap_thong_tin() for _ in range(int(input("Nhap so luong mat hang: ")))]
def sap_xep_theo_thue(danh_sach):
    return sorted(danh_sach, key=lambda x: x.thue_vat, reverse=True)
def in_danh_sach(danh_sach):
    for mat_hang in danh_sach:
        print(mat_hang)