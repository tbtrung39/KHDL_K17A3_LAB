sinh_vien = []
while True:
    ma_sv = input("Nhập mã sv: ")
    if ma_sv == '':
        break
    ho_ten = input("Nhập tên sv: ")
    diem_thi = float(input("Nhập điểm thi của sv: "))
    if diem_thi >10:
        break
    sinh_vien.append({
    "Mã SV": ma_sv,
    "Họ tên SV": ho_ten,
    "Điểm thi": diem_thi
})
print(sinh_vien)





class CoSoDuLieuNhanVien:
    def __init__(self):
        self.co_so_du_lieu = {}

    def tao_nhan_vien(self):
        ma = input("Nhập mã nhân viên: ")
        ten = input("Nhập tên nhân viên: ")
        nam_sinh = int(input("Nhập năm sinh nhân viên: "))
        luong = int(input("Nhập lương nhân viên: "))
        self.co_so_du_lieu[ma] = {'Ten': ten, 'Nam Sinh': nam_sinh, 'Luong': luong}
        print(f"Nhan vien {ten} da duoc them.")

    def tim_nhan_vien(self):
        ma = input("Nhập mã nhân viên cần tìm: ")
        nhan_vien = self.co_so_du_lieu.get(ma)
        if nhan_vien:
            print(nhan_vien)
        else:
            print("Khong tim thay nhan vien.")

    def tang_luong(self):
        ma = input("Nhập mã nhân viên cần tăng lương: ")
        so_tien = int(input("Nhập số tiền cần tăng: "))
        nhan_vien = self.co_so_du_lieu.get(ma)
        if nhan_vien:
            nhan_vien['Luong'] += so_tien
            print(f"Luong tang them {so_tien}. Luong moi: {nhan_vien['Luong']}")
        else:
            print("Khong tim thay nhan vien.")

    def xoa_nhan_vien(self):
        ma = input("Nhập mã nhân viên cần xóa: ")
        if ma in self.co_so_du_lieu:
            del self.co_so_du_lieu[ma]
            print("Nhan vien da duoc xoa.")
        else:
            print("Khong tim thay nhan vien.")

    def sap_xep_nhan_vien_theo_nam_sinh(self):
        co_so_du_lieu_da_sap_xep = dict(sorted(self.co_so_du_lieu.items(), key=lambda x: x[1]['Nam Sinh'], reverse=True))
        print(co_so_du_lieu_da_sap_xep)

    def chay_chuong_trinh(self):
        while True:
            print("\n1. Tạo nhân viên")
            print("2. Tìm nhân viên")
            print("3. Tăng lương")
            print("4. Xóa nhân viên")
            print("5. Sắp xếp nhân viên theo năm sinh")
            print("6. Thoát chương trình")
            lua_chon = input("Nhập lựa chọn của bạn (1-6): ")
            if lua_chon == '1':
                self.tao_nhan_vien()
            elif lua_chon == '2':
                self.tim_nhan_vien()
            elif lua_chon == '3':
                self.tang_luong()
            elif lua_chon == '4':
                self.xoa_nhan_vien()
            elif lua_chon == '5':
                self.sap_xep_nhan_vien_theo_nam_sinh()
            elif lua_chon == '6':
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

csdl = CoSoDuLieuNhanVien()
csdl.chay_chuong_trinh()